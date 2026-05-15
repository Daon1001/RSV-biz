"""
메인비즈·이노비즈 AI 마스터 컨설턴트 v2.0
- 컨설턴트 내부용 통합 관리 시스템
- 업종별 상세 진단 문항 + 증빙자료 체크리스트 + 점수 향상 시뮬레이션
"""
import streamlit as st
import anthropic
import json
import requests
from datetime import datetime, date
from typing import Dict, Any, List, Optional

from mainbiz_criteria import get_mainbiz_criteria, calculate_item_score
from innobiz_criteria import (
    get_innobiz_criteria,
    calculate_item_score as calculate_item_score_inno,
    calculate_tech_grade,
    TECH_GRADE_CRITERIA,
)
from rsv_design import (
    inject_css,
    render_hero,
    render_section,
    generate_consulting_report,
    render_guidebook_page,
)

# =====================================================================
# 💰 모델 가격 정보 (2026년 5월 기준, USD per 1M tokens)
# =====================================================================
MODEL_PRICES = {
    "claude-haiku-4-5-20251001": {"input": 1.0, "output": 5.0, "label": "⚡ Haiku 4.5"},
    "claude-sonnet-4-6":         {"input": 3.0, "output": 15.0, "label": "⭐ Sonnet 4.6"},
    "claude-opus-4-7":           {"input": 5.0, "output": 25.0, "label": "👑 Opus 4.7"},
}
USD_TO_KRW = 1380

MODEL_OPTIONS = {
    "⚡ Haiku 4.5 (빠름·저렴)": "claude-haiku-4-5-20251001",
    "⭐ Sonnet 4.6 (균형·기본)": "claude-sonnet-4-6",
    "👑 Opus 4.7 (최고품질·느림)": "claude-opus-4-7",
}

ADMIN_EMAIL = "incheon00@gmail.com"
MAX_MONTHLY_LIMIT = 50  # 일반 사용자 월 사용 한도

def _usage_filename():
    return st.secrets.get("mainnoinno_usage_filename", "mainnoinno_usage.json")

def get_default_usage_db():
    return {"logs": [], "last_updated": datetime.now().isoformat()}

def log_api_usage(email: str, model: str, input_tokens: int, output_tokens: int, action: str):
    """API 호출 시 사용량을 Gist에 기록"""
    try:
        usage_db = gist_load(_usage_filename(), get_default_usage_db)

        price = MODEL_PRICES.get(model, MODEL_PRICES["claude-sonnet-4-6"])
        cost_usd = (input_tokens / 1_000_000 * price["input"] +
                    output_tokens / 1_000_000 * price["output"])

        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "email": email,
            "model": model,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "cost_usd": round(cost_usd, 6),
            "action": action,
        }
        usage_db.setdefault("logs", []).append(log_entry)

        # 사용자 카운트 증가
        users_db = gist_load(_users_filename(), get_default_users_db)
        user = users_db.get("users", {}).get(email)
        if user:
            # 월 리셋
            current_month = date.today().month
            if user.get("last_reset_month") != current_month:
                user["usage_count"] = 0
                user["last_reset_month"] = current_month
            user["usage_count"] = user.get("usage_count", 0) + 1
            gist_save(_users_filename(), users_db)

        gist_save(_usage_filename(), usage_db)
    except Exception as e:
        # 로깅 실패해도 메인 기능은 계속 작동
        print(f"사용량 로깅 실패: {e}")

def check_usage_limit(email: str) -> tuple:
    """사용량 한도 체크. (가능 여부, 남은 횟수) 반환"""
    users_db = gist_load(_users_filename(), get_default_users_db)
    user = users_db.get("users", {}).get(email, {})

    # 관리자는 무제한
    if user.get("is_admin"):
        return True, "무제한"

    # 월 리셋 체크
    current_month = date.today().month
    if user.get("last_reset_month") != current_month:
        return True, MAX_MONTHLY_LIMIT

    used = user.get("usage_count", 0)
    remaining = MAX_MONTHLY_LIMIT - used

    return remaining > 0, max(remaining, 0)

# ── 페이지 설정 ──
st.set_page_config(
    page_title="메인비즈·이노비즈 AI 마스터 컨설턴트",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================================
# 🔒 GitHub Gist DB 시스템
# =====================================================================
def _gist_headers():
    token = st.secrets.get("github_token", "")
    if not token:
        return None
    return {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}

def _gist_id():
    return st.secrets.get("gist_id", "")

def _users_filename():
    return st.secrets.get("mainnoinno_users_filename", "mainnoinno_users.json")

def _companies_filename():
    return st.secrets.get("mainnoinno_companies_filename", "mainnoinno_companies.json")

def get_default_users_db():
    today = date.today().isoformat()
    return {
        "users": {
            "incheon00@gmail.com": {
                "approved": True, "is_admin": True,
                "created_at": today, "usage_count": 0,
                "last_reset_month": date.today().month
            },
        },
        "last_updated": datetime.now().isoformat()
    }

def get_default_companies_db():
    return {"companies": {}, "last_updated": datetime.now().isoformat()}

def gist_load(filename: str, default_factory):
    headers = _gist_headers()
    gist_id = _gist_id()
    if not headers or not gist_id:
        return default_factory()
    try:
        resp = requests.get(f"https://api.github.com/gists/{gist_id}", headers=headers, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            if filename in data.get("files", {}):
                return json.loads(data["files"][filename]["content"])
    except Exception as e:
        st.warning(f"Gist 로드 실패: {e}")
    return default_factory()

def gist_save(filename: str, content: dict):
    headers = _gist_headers()
    gist_id = _gist_id()
    if not headers or not gist_id:
        return False
    try:
        content["last_updated"] = datetime.now().isoformat()
        payload = {"files": {filename: {"content": json.dumps(content, ensure_ascii=False, indent=2)}}}
        resp = requests.patch(
            f"https://api.github.com/gists/{gist_id}",
            headers=headers, json=payload, timeout=10
        )
        return resp.status_code == 200
    except Exception as e:
        st.error(f"Gist 저장 실패: {e}")
        return False

# =====================================================================
# 🔐 인증
# =====================================================================
def init_auth():
    if "user_email" not in st.session_state:
        st.session_state.user_email = None
        st.session_state.is_admin = False

def login_screen():
    render_hero(st,
                "🏆 메인비즈·이노비즈 AI 마스터 컨설턴트",
                "컨설턴트 내부용 통합 관리 시스템 v2.3 · RSV CONSULTING")

    tab_login, tab_signup = st.tabs(["🔑 로그인", "✍️ 회원가입"])
    users_db = gist_load(_users_filename(), get_default_users_db)

    with tab_login:
        email = st.text_input("이메일", key="login_email").strip().lower()
        if st.button("로그인", type="primary", use_container_width=True):
            user = users_db.get("users", {}).get(email)
            if not user:
                st.error("등록되지 않은 이메일입니다. 회원가입을 먼저 진행하세요.")
            elif not user.get("approved"):
                st.warning("⏳ 관리자 승인 대기 중입니다.")
            elif user.get("suspended"):
                st.error("⛔ 정지된 계정입니다. 관리자에게 문의하세요.")
            else:
                st.session_state.user_email = email
                st.session_state.is_admin = user.get("is_admin", False)
                st.rerun()

    with tab_signup:
        st.markdown("**✋ 신규 사용자 승인 신청**")
        st.caption("관리자 승인 후 이용 가능합니다. 모든 항목을 입력해 주세요.")

        with st.form("signup_form"):
            new_email = st.text_input("이메일 *", placeholder="example@company.com")
            col_n, col_c = st.columns(2)
            with col_n:
                new_name = st.text_input("이름 *", placeholder="홍길동")
            with col_c:
                new_company = st.text_input("회사명 *", placeholder="(주)RSV컨설팅")
            new_purpose = st.text_area("사용 목적", placeholder="메인비즈/이노비즈 컨설팅 업무용")

            if st.form_submit_button("📨 승인 요청 보내기", type="primary", use_container_width=True):
                if not new_email or "@" not in new_email:
                    st.error("올바른 이메일을 입력하세요.")
                elif not new_name or not new_company:
                    st.error("이름과 회사명은 필수입니다.")
                elif new_email in users_db.get("users", {}):
                    st.warning("이미 가입된 이메일입니다.")
                else:
                    users_db.setdefault("users", {})[new_email] = {
                        "approved": False, "is_admin": False,
                        "name": new_name,
                        "company": new_company,
                        "purpose": new_purpose,
                        "created_at": date.today().isoformat(),
                        "usage_count": 0,
                        "last_reset_month": date.today().month,
                    }
                    if gist_save(_users_filename(), users_db):
                        st.success("📩 가입 신청 완료! 관리자 승인 후 이용 가능합니다.")
                        st.balloons()

# =====================================================================
# 📊 메인비즈 상세 진단 (핵심 화면)
# =====================================================================
def mainbiz_assessment_page():
    st.header("📊 메인비즈 자가진단")

    # 고객사 선택
    companies_db = gist_load(_companies_filename(), get_default_companies_db)
    company_list = ["[새 진단 - 저장 안 됨]"] + list(companies_db.get("companies", {}).keys())

    col_co, col_ind = st.columns([2, 1])
    with col_co:
        selected_company = st.selectbox("고객사 선택", company_list, key="mb_company")
    with col_ind:
        default_industry = "manufacturing"
        if selected_company != "[새 진단 - 저장 안 됨]":
            co_data = companies_db["companies"].get(selected_company, {})
            default_industry = co_data.get("industry_code", "manufacturing")

        industry = st.selectbox(
            "업종",
            options=["manufacturing", "service", "construction", "it"],
            format_func=lambda x: {"manufacturing": "🏭 제조업",
                                   "service": "💼 서비스업",
                                   "construction": "🏗️ 건설업",
                                   "it": "💻 IT/소프트웨어업"}[x],
            index=["manufacturing", "service", "construction", "it"].index(default_industry),
            key="mb_industry"
        )

    criteria = get_mainbiz_criteria(industry)

    st.caption(f"평가지표 버전: **{criteria['version']}** | "
               f"자가진단 통과: **{criteria['self_pass']}점** | "
               f"현장평가 통과: **{criteria['field_pass']}점**")

    # 기존 답변 로드
    saved_answers = {}
    if selected_company != "[새 진단 - 저장 안 됨]":
        co_data = companies_db.get("companies", {}).get(selected_company, {})
        saved = co_data.get("mainbiz_assessment", {})
        if saved.get("industry") == industry:
            saved_answers = saved.get("answers", {})

    st.divider()

    # 분야별 탭 표시
    tabs = st.tabs([f"📋 {cat['name']}" for cat in criteria["categories"]])

    all_answers = saved_answers.copy()
    category_scores = {}

    for tab, cat in zip(tabs, criteria["categories"]):
        with tab:
            cat_score = 0
            cat_max = 0

            for item_id in cat["items"]:
                item = criteria["items"][item_id]

                st.subheader(f"{item['name']} ({item['max']}점)")

                item_answers = {}

                for q in item["questions"]:
                    q_id = q["id"]

                    if q["type"] == "single":
                        labels = [f"{opt['label']} ({opt['score']}점)" for opt in q["options"]]
                        default_idx = saved_answers.get(q_id, 0)
                        if not isinstance(default_idx, int) or default_idx >= len(labels):
                            default_idx = 0

                        selected = st.radio(
                            q["text"],
                            options=range(len(labels)),
                            format_func=lambda i, lbls=labels: lbls[i],
                            index=default_idx,
                            key=f"mb_{q_id}",
                        )
                        item_answers[q_id] = selected
                        all_answers[q_id] = selected

                    elif q["type"] == "multi":
                        st.write(f"**{q['text']}** (중복 선택 가능)")
                        default_selected = saved_answers.get(q_id, [])
                        if not isinstance(default_selected, list):
                            default_selected = []

                        selected_indices = []
                        cols = st.columns(min(len(q["options"]), 3))
                        for idx, opt in enumerate(q["options"]):
                            with cols[idx % len(cols)]:
                                if st.checkbox(
                                    f"{opt['label']} (+{opt['score']}점)",
                                    value=(idx in default_selected),
                                    key=f"mb_{q_id}_{idx}"
                                ):
                                    selected_indices.append(idx)
                        item_answers[q_id] = selected_indices
                        all_answers[q_id] = selected_indices

                # 항목 점수 계산 및 표시
                item_score = calculate_item_score(item, item_answers)
                pct = item_score / item["max"] * 100

                col_s, col_b = st.columns([1, 4])
                with col_s:
                    if pct >= 80:
                        st.success(f"**{item_score} / {item['max']}점**")
                    elif pct >= 60:
                        st.info(f"**{item_score} / {item['max']}점**")
                    else:
                        st.warning(f"**{item_score} / {item['max']}점**")
                with col_b:
                    st.progress(pct / 100)

                # 증빙자료 안내
                with st.expander("📎 필요 증빙자료"):
                    for ev in item["evidences"]:
                        st.write(f"- {ev}")

                cat_score += item_score
                cat_max += item["max"]
                st.divider()

            category_scores[cat["id"]] = {
                "name": cat["name"], "score": cat_score, "max": cat_max
            }

    # 최종 결과
    st.divider()
    total_score = sum(c["score"] for c in category_scores.values())
    total_max = sum(c["max"] for c in category_scores.values())

    st.subheader("🎯 최종 진단 결과")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("총점", f"{total_score} / {total_max}")
    col2.metric("자가진단 600점", f"{total_score - 600:+d}",
                delta_color="normal" if total_score >= 600 else "inverse")
    col3.metric("현장평가 700점", f"{total_score - 700:+d}",
                delta_color="normal" if total_score >= 700 else "inverse")
    col4.metric("달성률", f"{total_score / total_max * 100:.1f}%")

    # 분야별 점수
    st.write("**분야별 점수 분포**")
    for cid, c in category_scores.items():
        pct = c["score"] / c["max"] * 100
        st.write(f"- {c['name']}: {c['score']}/{c['max']}점 ({pct:.1f}%)")
        st.progress(pct / 100)

    # 판정
    if total_score >= criteria["field_pass"]:
        st.success(f"✅ **현장평가 통과 기준({criteria['field_pass']}점) 충족!** 신청 가능 상태입니다.")
    elif total_score >= criteria["self_pass"]:
        st.warning(f"⚠️ 자가진단은 통과({criteria['self_pass']}점)했으나 현장평가 기준 미달."
                   f" 추가 필요: **{criteria['field_pass'] - total_score}점**")
    else:
        st.error(f"❌ 자가진단 통과 기준({criteria['self_pass']}점) 미달. 신청 불가."
                 f" 추가 필요: **{criteria['self_pass'] - total_score}점**")

    # 점수 향상 우선순위
    st.divider()
    st.subheader("💡 점수 향상 우선순위 (취약 항목 TOP 5)")

    item_gaps = []
    for item_id, item in criteria["items"].items():
        item_specific_answers = {q["id"]: all_answers.get(q["id"], 0) for q in item["questions"]}
        current = calculate_item_score(item, item_specific_answers)
        gap = item["max"] - current
        if gap > 0:
            item_gaps.append({
                "id": item_id, "name": item["name"],
                "category": item["category_name"],
                "current": current, "max": item["max"], "gap": gap
            })

    item_gaps.sort(key=lambda x: x["gap"], reverse=True)

    for i, gap_info in enumerate(item_gaps[:5], 1):
        st.write(f"**{i}. [{gap_info['category']}] {gap_info['name']}** "
                 f"→ 현재 {gap_info['current']}/{gap_info['max']}점 "
                 f"(개선 가능 **+{gap_info['gap']}점**)")

    # 저장 & AI 분석
    st.divider()
    col_save, col_ai = st.columns(2)

    with col_save:
        if selected_company != "[새 진단 - 저장 안 됨]":
            if st.button("💾 진단 결과 저장", type="primary", use_container_width=True):
                companies_db["companies"][selected_company]["mainbiz_assessment"] = {
                    "industry": industry,
                    "version": criteria["version"],
                    "answers": all_answers,
                    "total_score": total_score,
                    "category_scores": category_scores,
                    "evaluated_at": datetime.now().isoformat(),
                    "evaluator": st.session_state.user_email
                }
                if gist_save(_companies_filename(), companies_db):
                    st.success("✅ 저장 완료!")
        else:
            st.info("저장하려면 먼저 고객사를 등록하세요.")

    with col_ai:
        # 모델 선택
        selected_model_label = st.selectbox(
            "AI 모델 선택",
            options=list(MODEL_OPTIONS.keys()),
            index=1,  # 기본 Sonnet
            key="mb_model_select",
            help="Haiku는 빠르고 저렴 / Sonnet은 균형 / Opus는 최고 품질"
        )
        selected_model = MODEL_OPTIONS[selected_model_label]

        # 사용량 한도 체크
        can_use, remaining = check_usage_limit(st.session_state.user_email)

        if not can_use:
            st.error(f"❌ 월 사용량 한도({MAX_MONTHLY_LIMIT}회) 초과. 관리자에게 문의하세요.")
        else:
            if isinstance(remaining, int):
                st.caption(f"💎 이번 달 남은 횟수: {remaining}회 / {MAX_MONTHLY_LIMIT}회")
            else:
                st.caption(f"💎 사용 가능: {remaining}")

            if st.button("🤖 AI 컨설팅 리포트 생성", type="secondary", use_container_width=True):
                with st.spinner("Claude가 분석 중... (10~20초)"):
                    report = generate_ai_report(
                        selected_company, industry, criteria,
                        category_scores, total_score, item_gaps[:5],
                        model=selected_model,
                        user_email=st.session_state.user_email
                    )
                    st.session_state["mb_ai_report"] = report
                st.rerun()

    if "mb_ai_report" in st.session_state:
        st.divider()
        st.subheader("🤖 AI 컨설팅 리포트")
        st.markdown(st.session_state["mb_ai_report"])

    # 📥 보고서 다운로드
    st.divider()
    render_section(st, "📥 컨설팅 보고서 다운로드")
    st.caption("진단 결과를 RSV 디자인의 PDF형 HTML 보고서로 다운로드합니다. "
               "브라우저에서 열어 인쇄(Ctrl+P) → PDF로 저장 가능합니다.")

    # 증빙자료 매핑
    evidences_per_category = {}
    for cat in criteria["categories"]:
        evs = []
        for item_id in cat["items"]:
            item = criteria["items"][item_id]
            for ev in item.get("evidences", []):
                if ev not in evs:
                    evs.append(ev)
        evidences_per_category[cat["name"]] = evs

    co_display = selected_company if selected_company != "[새 진단 - 저장 안 됨]" else "신규 진단 기업"

    report_html = generate_consulting_report(
        cert_type="메인비즈",
        company_name=co_display,
        industry_name=criteria["industry_name"],
        total_score=total_score,
        self_pass=criteria["self_pass"],
        field_pass=criteria["field_pass"],
        category_scores=category_scores,
        top_gaps=item_gaps[:5],
        ai_report_md=st.session_state.get("mb_ai_report", ""),
        evidences_per_category=evidences_per_category,
    )

    filename = f"메인비즈_컨설팅보고서_{co_display}_{datetime.now().strftime('%Y%m%d')}.html"
    st.download_button(
        label="📥 메인비즈 컨설팅 보고서 다운로드 (HTML)",
        data=report_html.encode("utf-8"),
        file_name=filename,
        mime="text/html",
        use_container_width=True
    )

# =====================================================================
# 🤖 Claude AI 컨설팅 리포트
# =====================================================================
def get_claude_client():
    api_key = st.secrets.get("anthropic_api_key", "")
    if not api_key:
        st.error("Claude API 키가 설정되지 않았습니다.")
        return None
    return anthropic.Anthropic(api_key=api_key)

def generate_ai_report(company: str, industry: str, criteria: dict,
                        cat_scores: dict, total: int, top_gaps: list,
                        model: str = "claude-sonnet-4-6",
                        user_email: str = "") -> str:
    client = get_claude_client()
    if not client:
        return "API 키 미설정으로 분석 불가."

    cat_summary = "\n".join([
        f"- {v['name']}: {v['score']}/{v['max']}점 ({v['score']/v['max']*100:.1f}%)"
        for v in cat_scores.values()
    ])

    gap_summary = "\n".join([
        f"- {g['category']} / {g['name']}: {g['current']}/{g['max']}점 (개선여지 +{g['gap']}점)"
        for g in top_gaps
    ])

    pass_status = (
        "현장평가 통과 가능" if total >= criteria["field_pass"]
        else "자가진단만 통과 (현장평가 미달)" if total >= criteria["self_pass"]
        else "자가진단 미달 (신청 불가)"
    )

    prompt = f"""당신은 메인비즈 인증 컨설팅 전문가입니다.

[고객사] {company if company != '[새 진단 - 저장 안 됨]' else '신규 진단'}
[업종] {criteria['industry_name']}
[총점] {total} / 1000
[현재 상태] {pass_status}

[분야별 점수]
{cat_summary}

[우선 개선 항목 TOP 5]
{gap_summary}

다음 형식으로 컨설팅 리포트를 작성하세요. 업종({criteria['industry_name']})의 특성을 반영하여 구체적으로 작성하세요.

## 1. 종합 진단
현재 상태를 2-3문장으로 요약. 어느 분야가 강하고 약한지.

## 2. 강점 분야 분석
점수가 높은 분야의 구체적 강점과, 현장평가 시 어떻게 어필할지

## 3. 우선 개선 과제 (TOP 3)
가장 효과적으로 점수를 올릴 수 있는 3가지 실행 과제. 각 과제마다:
- 무엇을 (구체적 액션)
- 어떻게 (실행 방법)
- 효과 (예상 점수 향상)
- 소요 기간

## 4. 증빙자료 준비 가이드
현장평가 통과를 위해 반드시 준비해야 할 증빙자료 우선순위 5가지

## 5. 신청 전략
신청 시점, 평가기관 선택(신보/기보/KPC), 주의사항
"""

    try:
        response = client.messages.create(
            model=model,
            max_tokens=2500,
            messages=[{"role": "user", "content": prompt}]
        )

        # 사용량 로깅
        if user_email:
            log_api_usage(
                email=user_email,
                model=model,
                input_tokens=response.usage.input_tokens,
                output_tokens=response.usage.output_tokens,
                action="메인비즈_AI리포트"
            )

        return response.content[0].text
    except Exception as e:
        return f"AI 분석 실패: {e}"

# =====================================================================
# 🏢 고객사 관리
# =====================================================================
def companies_page():
    st.header("🏢 고객사 관리")

    companies_db = gist_load(_companies_filename(), get_default_companies_db)
    companies = companies_db.get("companies", {})

    tab_list, tab_add = st.tabs(["📋 고객사 목록", "➕ 신규 등록"])

    with tab_add:
        with st.form("add_company"):
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("회사명 *")
                biz_no = st.text_input("사업자등록번호")
                industry_code = st.selectbox(
                    "업종 *",
                    options=["manufacturing", "service", "construction", "it"],
                    format_func=lambda x: {"manufacturing": "🏭 제조업",
                                           "service": "💼 서비스업",
                                           "construction": "🏗️ 건설업",
                                           "it": "💻 IT/소프트웨어업"}[x]
                )
                industry_detail = st.text_input("업종 상세 (예: 전자부품 제조)")

            with col2:
                est_year = st.number_input("설립연도", min_value=1950,
                                           max_value=date.today().year, value=2020)
                ceo = st.text_input("대표자")
                contact = st.text_input("담당자 연락처")
                emp_count = st.number_input("임직원 수", min_value=0, value=10)

            target_certs = st.multiselect(
                "진행 예정 인증",
                ["메인비즈", "이노비즈", "벤처기업", "기업부설연구소"],
                default=["메인비즈"]
            )
            memo = st.text_area("메모")

            if st.form_submit_button("등록", type="primary"):
                if not name:
                    st.error("회사명은 필수입니다.")
                elif name in companies:
                    st.error("이미 등록된 회사명입니다.")
                else:
                    companies[name] = {
                        "biz_no": biz_no,
                        "industry_code": industry_code,
                        "industry_detail": industry_detail,
                        "est_year": est_year, "ceo": ceo,
                        "contact": contact, "emp_count": emp_count,
                        "target_certs": target_certs, "memo": memo,
                        "created_at": datetime.now().isoformat(),
                        "created_by": st.session_state.user_email,
                    }
                    companies_db["companies"] = companies
                    if gist_save(_companies_filename(), companies_db):
                        st.success(f"✅ {name} 등록 완료!")
                        st.rerun()

    with tab_list:
        if not companies:
            st.info("등록된 고객사가 없습니다.")
        else:
            for name, co in companies.items():
                industry_emoji = {"manufacturing": "🏭", "service": "💼", "construction": "🏗️", "it": "💻"}.get(
                    co.get("industry_code", ""), "📋"
                )
                with st.expander(f"{industry_emoji} **{name}** ({co.get('industry_detail', '-')})"):
                    col1, col2, col3 = st.columns(3)
                    col1.write(f"**대표**: {co.get('ceo', '-')}")
                    col1.write(f"**설립**: {co.get('est_year', '-')}년")
                    col1.write(f"**임직원**: {co.get('emp_count', 0)}명")
                    col2.write(f"**사업자번호**: {co.get('biz_no', '-')}")
                    col2.write(f"**연락처**: {co.get('contact', '-')}")
                    col3.write(f"**진행 인증**: {', '.join(co.get('target_certs', [])) or '-'}")

                    mb = co.get("mainbiz_assessment", {})
                    if mb.get("total_score"):
                        st.divider()
                        col_score, col_status = st.columns(2)
                        col_score.metric(
                            "메인비즈 최근 진단",
                            f"{mb['total_score']}점",
                            help=f"평가일: {mb.get('evaluated_at', '')[:10]}"
                        )
                        if mb["total_score"] >= 700:
                            col_status.success("✅ 현장평가 통과 가능")
                        elif mb["total_score"] >= 600:
                            col_status.warning("⚠️ 자가진단만 통과")
                        else:
                            col_status.error("❌ 자가진단 미달")

                    ib = co.get("innobiz_assessment", {})
                    if ib.get("total_score"):
                        col_score2, col_status2 = st.columns(2)
                        col_score2.metric(
                            "이노비즈 최근 진단",
                            f"{ib['total_score']}점",
                            help=f"평가일: {ib.get('evaluated_at', '')[:10]}"
                        )
                        if ib["total_score"] >= 700:
                            col_status2.success("✅ 현장평가 통과 가능")
                        elif ib["total_score"] >= 650:
                            col_status2.warning("⚠️ 자가진단만 통과")
                        else:
                            col_status2.error("❌ 자가진단 미달")

                    tg = co.get("innobiz_tech_grade", {})
                    if tg.get("grade"):
                        col_tg1, col_tg2 = st.columns(2)
                        col_tg1.metric(
                            "이노비즈 기술등급",
                            tg["grade"],
                            help=f"평가일: {tg.get('evaluated_at', '')[:10]}"
                        )
                        if tg.get("passed"):
                            col_tg2.success(f"✅ B 이상 통과")
                        else:
                            col_tg2.error(f"❌ B 미달")

                    if co.get("memo"):
                        st.caption(f"💬 {co['memo']}")

# =====================================================================
# 📊 이노비즈 상세 진단
# =====================================================================
def innobiz_assessment_page():
    st.header("📊 이노비즈 자가진단")

    companies_db = gist_load(_companies_filename(), get_default_companies_db)
    company_list = ["[새 진단 - 저장 안 됨]"] + list(companies_db.get("companies", {}).keys())

    col_co, col_ind = st.columns([2, 1])
    with col_co:
        selected_company = st.selectbox("고객사 선택", company_list, key="ib_company")
    with col_ind:
        default_industry = "manufacturing"
        if selected_company != "[새 진단 - 저장 안 됨]":
            co_data = companies_db["companies"].get(selected_company, {})
            default_industry = co_data.get("industry_code", "manufacturing")

        industry = st.selectbox(
            "업종",
            options=["manufacturing", "service", "construction", "it"],
            format_func=lambda x: {"manufacturing": "🏭 제조업",
                                   "service": "💼 서비스업",
                                   "construction": "🏗️ 건설업",
                                   "it": "💻 IT/소프트웨어업"}[x],
            index=["manufacturing", "service", "construction", "it"].index(default_industry),
            key="ib_industry"
        )

    criteria = get_innobiz_criteria(industry)

    st.caption(f"평가지표 버전: **{criteria['version']}** | "
               f"자가진단 통과: **{criteria['self_pass']}점** | "
               f"현장평가 통과: **{criteria['field_pass']}점** | "
               f"기술등급: **{criteria['tech_grade_min']}** 이상")

    st.warning("⚠️ 이노비즈는 **시스템 평가 700점 + 기술등급 B 이상**을 동시 통과해야 인증됩니다. "
               "기술등급은 별도 메뉴('🎓 이노비즈 기술등급 평가')에서 진행하세요.")

    # 기존 답변 로드
    saved_answers = {}
    if selected_company != "[새 진단 - 저장 안 됨]":
        co_data = companies_db.get("companies", {}).get(selected_company, {})
        saved = co_data.get("innobiz_assessment", {})
        if saved.get("industry") == industry:
            saved_answers = saved.get("answers", {})

    st.divider()

    # 분야별 탭 표시
    tabs = st.tabs([f"📋 {cat['name']}" for cat in criteria["categories"]])

    all_answers = saved_answers.copy()
    category_scores = {}

    for tab, cat in zip(tabs, criteria["categories"]):
        with tab:
            cat_score = 0
            cat_max = 0

            for item_id in cat["items"]:
                item = criteria["items"][item_id]

                st.subheader(f"{item['name']} ({item['max']}점)")

                item_answers = {}

                for q in item["questions"]:
                    q_id = q["id"]

                    if q["type"] == "single":
                        labels = [f"{opt['label']} ({opt['score']}점)" for opt in q["options"]]
                        default_idx = saved_answers.get(q_id, 0)
                        if not isinstance(default_idx, int) or default_idx >= len(labels):
                            default_idx = 0

                        selected = st.radio(
                            q["text"],
                            options=range(len(labels)),
                            format_func=lambda i, lbls=labels: lbls[i],
                            index=default_idx,
                            key=f"ib_{q_id}",
                        )
                        item_answers[q_id] = selected
                        all_answers[q_id] = selected

                    elif q["type"] == "multi":
                        st.write(f"**{q['text']}** (중복 선택 가능)")
                        default_selected = saved_answers.get(q_id, [])
                        if not isinstance(default_selected, list):
                            default_selected = []

                        selected_indices = []
                        cols = st.columns(min(len(q["options"]), 3))
                        for idx, opt in enumerate(q["options"]):
                            with cols[idx % len(cols)]:
                                if st.checkbox(
                                    f"{opt['label']} (+{opt['score']}점)",
                                    value=(idx in default_selected),
                                    key=f"ib_{q_id}_{idx}"
                                ):
                                    selected_indices.append(idx)
                        item_answers[q_id] = selected_indices
                        all_answers[q_id] = selected_indices

                # 항목 점수 계산
                item_score = calculate_item_score_inno(item, item_answers)
                pct = item_score / item["max"] * 100

                col_s, col_b = st.columns([1, 4])
                with col_s:
                    if pct >= 80:
                        st.success(f"**{item_score} / {item['max']}점**")
                    elif pct >= 60:
                        st.info(f"**{item_score} / {item['max']}점**")
                    else:
                        st.warning(f"**{item_score} / {item['max']}점**")
                with col_b:
                    st.progress(pct / 100)

                # 증빙자료 안내
                with st.expander("📎 필요 증빙자료"):
                    for ev in item["evidences"]:
                        st.write(f"- {ev}")

                cat_score += item_score
                cat_max += item["max"]
                st.divider()

            category_scores[cat["id"]] = {
                "name": cat["name"], "score": cat_score, "max": cat_max
            }

    # 최종 결과
    st.divider()
    total_score = sum(c["score"] for c in category_scores.values())
    total_max = sum(c["max"] for c in category_scores.values())

    st.subheader("🎯 최종 진단 결과")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("총점", f"{total_score} / {total_max}")
    col2.metric("자가진단 650점", f"{total_score - 650:+d}",
                delta_color="normal" if total_score >= 650 else "inverse")
    col3.metric("현장평가 700점", f"{total_score - 700:+d}",
                delta_color="normal" if total_score >= 700 else "inverse")
    col4.metric("달성률", f"{total_score / total_max * 100:.1f}%")

    # 분야별 점수
    st.write("**분야별 점수 분포**")
    for cid, c in category_scores.items():
        pct = c["score"] / c["max"] * 100
        st.write(f"- {c['name']}: {c['score']}/{c['max']}점 ({pct:.1f}%)")
        st.progress(pct / 100)

    # 판정
    if total_score >= criteria["field_pass"]:
        # 기술등급 결과도 확인
        tg_passed = False
        tg_grade = "미평가"
        if selected_company != "[새 진단 - 저장 안 됨]":
            tg = companies_db["companies"].get(selected_company, {}).get("innobiz_tech_grade", {})
            tg_passed = tg.get("passed", False)
            tg_grade = tg.get("grade", "미평가")

        if tg_passed:
            st.success(f"✅ **시스템 평가 700점 + 기술등급 {tg_grade}({criteria['tech_grade_min']} 이상) 모두 통과!** 신청 가능 상태입니다.")
        else:
            st.success(f"✅ 시스템 평가 통과({criteria['field_pass']}점). "
                       f"**기술등급 평가 별도 진행 필요** (현재: {tg_grade})")
    elif total_score >= criteria["self_pass"]:
        st.warning(f"⚠️ 자가진단은 통과({criteria['self_pass']}점)했으나 현장평가 기준 미달."
                   f" 추가 필요: **{criteria['field_pass'] - total_score}점**")
    else:
        st.error(f"❌ 자가진단 통과 기준({criteria['self_pass']}점) 미달. 신청 불가."
                 f" 추가 필요: **{criteria['self_pass'] - total_score}점**")

    # 점수 향상 우선순위
    st.divider()
    st.subheader("💡 점수 향상 우선순위 (취약 항목 TOP 5)")

    item_gaps = []
    for item_id, item in criteria["items"].items():
        item_specific_answers = {q["id"]: all_answers.get(q["id"], 0) for q in item["questions"]}
        current = calculate_item_score_inno(item, item_specific_answers)
        gap = item["max"] - current
        if gap > 0:
            item_gaps.append({
                "id": item_id, "name": item["name"],
                "category": item["category_name"],
                "current": current, "max": item["max"], "gap": gap
            })

    item_gaps.sort(key=lambda x: x["gap"], reverse=True)

    for i, gap_info in enumerate(item_gaps[:5], 1):
        st.write(f"**{i}. [{gap_info['category']}] {gap_info['name']}** "
                 f"→ 현재 {gap_info['current']}/{gap_info['max']}점 "
                 f"(개선 가능 **+{gap_info['gap']}점**)")

    # 저장 & AI 분석
    st.divider()
    col_save, col_ai = st.columns(2)

    with col_save:
        if selected_company != "[새 진단 - 저장 안 됨]":
            if st.button("💾 진단 결과 저장", type="primary", use_container_width=True, key="ib_save"):
                companies_db["companies"][selected_company]["innobiz_assessment"] = {
                    "industry": industry,
                    "version": criteria["version"],
                    "answers": all_answers,
                    "total_score": total_score,
                    "category_scores": category_scores,
                    "evaluated_at": datetime.now().isoformat(),
                    "evaluator": st.session_state.user_email
                }
                if gist_save(_companies_filename(), companies_db):
                    st.success("✅ 저장 완료!")
        else:
            st.info("저장하려면 먼저 고객사를 등록하세요.")

    with col_ai:
        # 모델 선택
        selected_model_label_ib = st.selectbox(
            "AI 모델 선택",
            options=list(MODEL_OPTIONS.keys()),
            index=1,
            key="ib_model_select",
            help="Haiku는 빠르고 저렴 / Sonnet은 균형 / Opus는 최고 품질"
        )
        selected_model_ib = MODEL_OPTIONS[selected_model_label_ib]

        # 사용량 한도 체크
        can_use_ib, remaining_ib = check_usage_limit(st.session_state.user_email)

        if not can_use_ib:
            st.error(f"❌ 월 사용량 한도({MAX_MONTHLY_LIMIT}회) 초과. 관리자에게 문의하세요.")
        else:
            if isinstance(remaining_ib, int):
                st.caption(f"💎 이번 달 남은 횟수: {remaining_ib}회 / {MAX_MONTHLY_LIMIT}회")
            else:
                st.caption(f"💎 사용 가능: {remaining_ib}")

            if st.button("🤖 AI 컨설팅 리포트 생성", type="secondary",
                          use_container_width=True, key="ib_ai"):
                with st.spinner("Claude가 분석 중... (10~20초)"):
                    report = generate_innobiz_ai_report(
                        selected_company, industry, criteria,
                        category_scores, total_score, item_gaps[:5],
                        model=selected_model_ib,
                        user_email=st.session_state.user_email
                    )
                    st.session_state["ib_ai_report"] = report
                st.rerun()

    if "ib_ai_report" in st.session_state:
        st.divider()
        st.subheader("🤖 AI 컨설팅 리포트")
        st.markdown(st.session_state["ib_ai_report"])

    # 📥 보고서 다운로드
    st.divider()
    render_section(st, "📥 컨설팅 보고서 다운로드")
    st.caption("진단 결과를 RSV 디자인의 PDF형 HTML 보고서로 다운로드합니다. "
               "브라우저에서 열어 인쇄(Ctrl+P) → PDF로 저장 가능합니다.")

    # 증빙자료 매핑
    evidences_per_category = {}
    for cat in criteria["categories"]:
        evs = []
        for item_id in cat["items"]:
            item = criteria["items"][item_id]
            for ev in item.get("evidences", []):
                if ev not in evs:
                    evs.append(ev)
        evidences_per_category[cat["name"]] = evs

    co_display = selected_company if selected_company != "[새 진단 - 저장 안 됨]" else "신규 진단 기업"

    # 기술등급 정보 가져오기 (저장된 데이터에서)
    tech_grade_info = None
    if selected_company != "[새 진단 - 저장 안 됨]":
        tg = companies_db["companies"].get(selected_company, {}).get("innobiz_tech_grade", {})
        if tg.get("grade"):
            tech_grade_info = {"grade": tg["grade"], "passed": tg.get("passed", False)}

    report_html = generate_consulting_report(
        cert_type="이노비즈",
        company_name=co_display,
        industry_name=criteria["industry_name"],
        total_score=total_score,
        self_pass=criteria["self_pass"],
        field_pass=criteria["field_pass"],
        category_scores=category_scores,
        top_gaps=item_gaps[:5],
        ai_report_md=st.session_state.get("ib_ai_report", ""),
        tech_grade=tech_grade_info,
        evidences_per_category=evidences_per_category,
    )

    filename = f"이노비즈_컨설팅보고서_{co_display}_{datetime.now().strftime('%Y%m%d')}.html"
    st.download_button(
        label="📥 이노비즈 컨설팅 보고서 다운로드 (HTML)",
        data=report_html.encode("utf-8"),
        file_name=filename,
        mime="text/html",
        use_container_width=True,
        key="ib_download"
    )


def generate_innobiz_ai_report(company: str, industry: str, criteria: dict,
                                cat_scores: dict, total: int, top_gaps: list,
                                model: str = "claude-sonnet-4-6",
                                user_email: str = "") -> str:
    """이노비즈 AI 컨설팅 리포트 생성"""
    client = get_claude_client()
    if not client:
        return "API 키 미설정으로 분석 불가."

    cat_summary = "\n".join([
        f"- {v['name']}: {v['score']}/{v['max']}점 ({v['score']/v['max']*100:.1f}%)"
        for v in cat_scores.values()
    ])

    gap_summary = "\n".join([
        f"- {g['category']} / {g['name']}: {g['current']}/{g['max']}점 (개선여지 +{g['gap']}점)"
        for g in top_gaps
    ])

    pass_status = (
        "현장평가 통과 가능" if total >= criteria["field_pass"]
        else "자가진단만 통과 (현장평가 미달)" if total >= criteria["self_pass"]
        else "자가진단 미달 (신청 불가)"
    )

    prompt = f"""당신은 이노비즈(기술혁신형 중소기업) 인증 컨설팅 전문가입니다.

[고객사] {company if company != '[새 진단 - 저장 안 됨]' else '신규 진단'}
[업종] {criteria['industry_name']}
[시스템 평가 총점] {total} / 1000
[현재 상태] {pass_status}
[추가 요건] 개별기술수준 B등급 이상 (별도 평가)

[분야별 점수]
{cat_summary}

[우선 개선 항목 TOP 5]
{gap_summary}

이노비즈는 메인비즈와 달리 **기술혁신·R&D 중심**의 평가입니다. 다음 형식으로 컨설팅 리포트를 작성하세요.
업종({criteria['industry_name']})의 특성을 반영하여 구체적으로 작성하세요.

## 1. 종합 진단
현재 상태를 2-3문장으로 요약. R&D·기술혁신 측면에서 어느 분야가 강하고 약한지.

## 2. 강점 분야 분석
점수가 높은 분야의 구체적 강점과, 현장평가 시 어떻게 어필할지

## 3. 우선 개선 과제 (TOP 3)
이노비즈 통과를 위해 가장 효과적인 3가지 실행 과제. 각 과제마다:
- 무엇을 (구체적 액션, 예: 부설연구소 설립, 특허 출원, R&D 비율 상향)
- 어떻게 (실행 방법)
- 효과 (예상 점수 향상)
- 소요 기간

## 4. 기술등급(B 이상) 확보 전략
시스템 평가 700점을 넘어도 기술등급이 B 미만이면 탈락입니다. 기술성·시장성·사업성 측면에서 어떻게 어필할지

## 5. 증빙자료 준비 가이드
현장평가 통과를 위해 반드시 준비해야 할 증빙자료 우선순위 5가지 (특허·R&D 인건비·연구원 명부 등 이노비즈 특화)

## 6. 신청 전략
신청 시점, 벤처기업 동시 신청 가능 여부, 평가기관(기술보증기금) 대응 시 주의사항
"""

    try:
        response = client.messages.create(
            model=model,
            max_tokens=3000,
            messages=[{"role": "user", "content": prompt}]
        )

        # 사용량 로깅
        if user_email:
            log_api_usage(
                email=user_email,
                model=model,
                input_tokens=response.usage.input_tokens,
                output_tokens=response.usage.output_tokens,
                action="이노비즈_AI리포트"
            )

        return response.content[0].text
    except Exception as e:
        return f"AI 분석 실패: {e}"


# =====================================================================
# 🎓 이노비즈 개별기술수준 평가 (14등급)
# =====================================================================
def tech_grade_page():
    st.header("🎓 이노비즈 개별기술수준 평가")
    st.caption("4개 분야(경영주 기술능력·기술성·시장성·사업성) 평가 → 14등급 산출 → B 이상 통과")

    companies_db = gist_load(_companies_filename(), get_default_companies_db)
    company_list = ["[새 진단 - 저장 안 됨]"] + list(companies_db.get("companies", {}).keys())

    selected_company = st.selectbox("고객사 선택", company_list, key="tg_company")

    # 기존 답변 로드
    saved_answers = {}
    if selected_company != "[새 진단 - 저장 안 됨]":
        co_data = companies_db.get("companies", {}).get(selected_company, {})
        saved = co_data.get("innobiz_tech_grade", {})
        saved_answers = saved.get("answers", {})

    st.divider()

    # 분야별 탭
    tabs = st.tabs([f"📋 {cat['name']} ({cat['weight']}점)"
                    for cat in TECH_GRADE_CRITERIA["categories"]])

    all_answers = saved_answers.copy()
    cat_scores_display = {}

    for tab, cat in zip(tabs, TECH_GRADE_CRITERIA["categories"]):
        with tab:
            st.subheader(f"{cat['name']} (배점 {cat['weight']}점)")

            cat_score = 0
            for q in cat["questions"]:
                q_id = q["id"]

                if q["type"] == "single":
                    labels = [f"{opt['label']} ({opt['score']}점)" for opt in q["options"]]
                    default_idx = saved_answers.get(q_id, 0)
                    if not isinstance(default_idx, int) or default_idx >= len(labels):
                        default_idx = 0

                    selected = st.radio(
                        q["text"],
                        options=range(len(labels)),
                        format_func=lambda i, lbls=labels: lbls[i],
                        index=default_idx,
                        key=f"tg_{q_id}",
                    )
                    all_answers[q_id] = selected
                    cat_score += q["options"][selected]["score"]

            cat_scores_display[cat["name"]] = {"score": cat_score, "max": cat["weight"]}
            pct = cat_score / cat["weight"] * 100
            st.progress(pct / 100, text=f"분야 점수: {cat_score} / {cat['weight']} ({pct:.1f}%)")

    # 최종 등급 산출
    st.divider()
    result = calculate_tech_grade(all_answers)

    st.subheader("🎯 기술등급 평가 결과")

    col1, col2, col3 = st.columns(3)
    col1.metric("총점", f"{result['total_score']} / 1000")
    col2.metric("등급", result["grade"])

    if result["passed"]:
        col3.success("✅ B 이상 통과")
    else:
        col3.error("❌ B 미달 (인증 불가)")

    # 분야별 점수
    st.write("**분야별 점수 분포**")
    for name, s in cat_scores_display.items():
        pct = s["score"] / s["max"] * 100
        st.write(f"- {name}: {s['score']}/{s['max']}점 ({pct:.1f}%)")
        st.progress(pct / 100)

    # 등급 기준 안내
    with st.expander("📊 14등급 산출 기준 보기"):
        st.markdown("""
| 등급 | 점수 범위 | 통과 여부 |
|------|----------|----------|
| AAA | 950~1000 | ✅ |
| AA | 900~949 | ✅ |
| A+ | 850~899 | ✅ |
| A | 800~849 | ✅ |
| BBB+ | 750~799 | ✅ |
| BBB | 700~749 | ✅ |
| BB+ | 650~699 | ✅ |
| BB | 600~649 | ✅ |
| B+ | 550~599 | ✅ |
| **B** | **500~549** | **✅ (최소 통과)** |
| CCC | 400~499 | ❌ |
| CC | 300~399 | ❌ |
| C | 200~299 | ❌ |
| D | 0~199 | ❌ |
        """)

    # 저장
    st.divider()
    if selected_company != "[새 진단 - 저장 안 됨]":
        if st.button("💾 기술등급 평가 저장", type="primary", use_container_width=True):
            companies_db["companies"][selected_company]["innobiz_tech_grade"] = {
                "answers": all_answers,
                "total_score": result["total_score"],
                "grade": result["grade"],
                "passed": result["passed"],
                "evaluated_at": datetime.now().isoformat(),
                "evaluator": st.session_state.user_email
            }
            if gist_save(_companies_filename(), companies_db):
                st.success("✅ 저장 완료!")
    else:
        st.info("저장하려면 먼저 고객사를 등록하세요.")


# =====================================================================
# 📋 신청 워크플로우
# =====================================================================
WORKFLOW_STAGES_MAINBIZ = [
    "1. 자격 확인 (업력 3년 이상, 결격사유 없음)",
    "2. 메인비즈넷 회원가입 및 기업등록",
    "3. 재무정보 입력 (국세청 신고분 기준)",
    "4. 온라인 자가진단 (600점 이상)",
    "5. 평가기관 선택 (신보/기보/KPC)",
    "6. 증빙자료 준비",
    "7. 현장평가 신청 및 수수료 납부",
    "8. 현장평가 실시 (700점 이상)",
    "9. 지방중기청 발급 승인 요청",
    "10. 메인비즈 확인서 발급 (유효기간 3년)",
]

WORKFLOW_STAGES_INNOBIZ = [
    "1. 자격 확인 (업력 3년 이상, 결격사유 없음)",
    "2. 이노비즈넷 회원가입 및 기업등록",
    "3. 재무정보 및 기술사업계획서 입력",
    "4. 온라인 자가진단 (650점 이상)",
    "5. 신청 접수 및 수수료 납부",
    "6. 증빙자료 준비 (특허·R&D 실적 등)",
    "7. 기술보증기금 현장평가 신청",
    "8. 현장평가 - 시스템(700점) + 기술등급(B 이상) 동시 통과",
    "9. 지방중기청 발급 승인 요청",
    "10. 이노비즈 확인서 발급 (유효기간 3년)",
]

def workflow_page():
    st.header("📋 신청 워크플로우 트래커")

    companies_db = gist_load(_companies_filename(), get_default_companies_db)
    companies = companies_db.get("companies", {})

    if not companies:
        st.info("먼저 고객사를 등록하세요.")
        return

    col_co, col_type = st.columns([2, 1])
    with col_co:
        selected_co = st.selectbox("고객사 선택", list(companies.keys()))
    with col_type:
        cert_type = st.radio(
            "인증 종류",
            ["메인비즈", "이노비즈"],
            horizontal=True,
            key="wf_cert_type"
        )

    stages = WORKFLOW_STAGES_MAINBIZ if cert_type == "메인비즈" else WORKFLOW_STAGES_INNOBIZ
    workflow_key = "mainbiz_workflow" if cert_type == "메인비즈" else "innobiz_workflow"

    co_data = companies[selected_co]
    workflow = co_data.setdefault(workflow_key, {"stages": {}})

    completed = sum(1 for s in stages
                    if workflow["stages"].get(s, {}).get("done"))
    progress_pct = completed / len(stages) * 100
    st.progress(progress_pct / 100,
                text=f"진행률: {completed}/{len(stages)} 단계 ({progress_pct:.0f}%)")

    # 이노비즈 추가 안내
    if cert_type == "이노비즈":
        st.info("📌 이노비즈는 **시스템 평가 700점 + 기술등급 B 이상**을 동시 충족해야 합니다.")

    st.divider()

    changed = False
    for stage in stages:
        stage_data = workflow["stages"].get(stage, {"done": False, "memo": "", "completed_at": ""})

        col_check, col_memo = st.columns([2, 3])
        with col_check:
            done = st.checkbox(stage, value=stage_data["done"], key=f"wf_{cert_type}_{stage}")
            if done != stage_data["done"]:
                stage_data["done"] = done
                stage_data["completed_at"] = datetime.now().isoformat() if done else ""
                changed = True
        with col_memo:
            memo = st.text_input("메모", value=stage_data.get("memo", ""),
                                 key=f"wfm_{cert_type}_{stage}",
                                 label_visibility="collapsed",
                                 placeholder="메모/일정/담당자...")
            if memo != stage_data.get("memo", ""):
                stage_data["memo"] = memo
                changed = True

        if stage_data.get("completed_at"):
            st.caption(f"  ✓ 완료: {stage_data['completed_at'][:10]}")

        workflow["stages"][stage] = stage_data

    if changed:
        if st.button("💾 진행 상황 저장", type="primary", use_container_width=True):
            companies_db["companies"][selected_co][workflow_key] = workflow
            if gist_save(_companies_filename(), companies_db):
                st.success("저장 완료!")
                st.rerun()

# =====================================================================
# 🏠 대시보드
# =====================================================================
def dashboard_page():
    render_hero(st,
                "🏆 메인비즈·이노비즈 AI 마스터 컨설턴트",
                "컨설턴트 내부용 통합 관리 시스템 v2.3 · RSV CONSULTING")

    companies_db = gist_load(_companies_filename(), get_default_companies_db)
    companies = companies_db.get("companies", {})

    # ── 메인비즈 통계 ──
    render_section(st, "🏆 메인비즈 현황")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("등록 고객사", len(companies))

    mb_count = sum(1 for c in companies.values()
                   if c.get("mainbiz_assessment", {}).get("total_score"))
    col2.metric("메인비즈 진단", mb_count)

    mb_pass = sum(1 for c in companies.values()
                  if c.get("mainbiz_assessment", {}).get("total_score", 0) >= 700)
    col3.metric("현장평가 가능", mb_pass)

    mb_scores = [c["mainbiz_assessment"]["total_score"] for c in companies.values()
                 if c.get("mainbiz_assessment", {}).get("total_score")]
    mb_avg = sum(mb_scores) / len(mb_scores) if mb_scores else 0
    col4.metric("평균 점수", f"{mb_avg:.0f}점")

    st.divider()

    # ── 이노비즈 통계 ──
    render_section(st, "🚀 이노비즈 현황")
    col1, col2, col3, col4 = st.columns(4)

    ib_count = sum(1 for c in companies.values()
                   if c.get("innobiz_assessment", {}).get("total_score"))
    col1.metric("이노비즈 진단", ib_count)

    ib_sys_pass = sum(1 for c in companies.values()
                      if c.get("innobiz_assessment", {}).get("total_score", 0) >= 700)
    col2.metric("시스템 700점 통과", ib_sys_pass)

    tg_pass = sum(1 for c in companies.values()
                  if c.get("innobiz_tech_grade", {}).get("passed"))
    col3.metric("기술등급 B 이상", tg_pass)

    # 시스템 + 기술등급 둘 다 통과한 회사
    both_pass = sum(1 for c in companies.values()
                    if c.get("innobiz_assessment", {}).get("total_score", 0) >= 700
                    and c.get("innobiz_tech_grade", {}).get("passed"))
    col4.metric("이노비즈 인증 가능", both_pass,
                help="시스템 700점 + 기술등급 B 이상 동시 충족")

    st.divider()

    # ── 인증 정보 카드 ──
    col_mb, col_ib = st.columns(2)
    with col_mb:
        st.info("""
        **🏆 메인비즈 (경영혁신형 중소기업)**
        - 자가진단 **600점** + 현장평가 **700점**
        - 평가기관: 신보 / 기보 / KPC
        - 유효기간: 3년
        - 수수료: 신규 55만원 / 연장 44만원
        """)
    with col_ib:
        st.info("""
        **🚀 이노비즈 (기술혁신형 중소기업)**
        - 자가진단 **650점** + 현장평가 **700점**
        - **+ 기술등급 B 이상** (14등급제)
        - 평가기관: 기술보증기금
        - 유효기간: 3년
        """)

    st.divider()

    # ── 최근 진단 이력 ──
    st.subheader("📋 최근 진단 이력")
    recent = []
    for name, c in companies.items():
        # 메인비즈
        mb = c.get("mainbiz_assessment", {})
        if mb.get("total_score"):
            recent.append({
                "company": name, "type": "메인비즈",
                "total": mb["total_score"],
                "date": mb.get("evaluated_at", "")[:10],
                "industry": mb.get("industry", "")
            })
        # 이노비즈
        ib = c.get("innobiz_assessment", {})
        if ib.get("total_score"):
            recent.append({
                "company": name, "type": "이노비즈",
                "total": ib["total_score"],
                "date": ib.get("evaluated_at", "")[:10],
                "industry": ib.get("industry", "")
            })
    recent.sort(key=lambda x: x["date"], reverse=True)

    if recent:
        for r in recent[:10]:
            emoji = {"manufacturing": "🏭", "service": "💼", "construction": "🏗️", "it": "💻"}.get(r["industry"], "")
            type_emoji = "🏆" if r["type"] == "메인비즈" else "🚀"
            st.write(f"- **{r['date']}** | {type_emoji} {r['type']} | {emoji} {r['company']}: **{r['total']}점**")
    else:
        st.caption("아직 진단 기록이 없습니다.")

# =====================================================================
# ⚙️ 관리자 대시보드 (4탭: 통계·사용자·승인대기·로그)
# =====================================================================
def admin_page():
    render_hero(st, "⚙️ 관리자 대시보드", "사용량 통계 · 사용자 관리 · 승인 대기 · 상세 로그")

    if not st.session_state.is_admin:
        st.error("⛔ 관리자만 접근 가능합니다.")
        return

    tab_stats, tab_users, tab_pending, tab_logs = st.tabs([
        "📊 사용량 통계",
        "👥 사용자 관리",
        "✋ 승인 대기",
        "📜 상세 로그"
    ])

    users_db = gist_load(_users_filename(), get_default_users_db)
    users = users_db.get("users", {})
    usage_db = gist_load(_usage_filename(), get_default_usage_db)
    logs = usage_db.get("logs", [])

    # ─── 탭 1: 사용량 통계 ───────────────────────────────
    with tab_stats:
        from collections import defaultdict
        from datetime import timedelta

        st.subheader("💰 사용량 통계")

        # ── 기간 선택 ──
        col_period, col_range = st.columns([1, 1])
        with col_period:
            period = st.radio(
                "집계 단위",
                ["📅 일별", "📆 주별", "🗓️ 월별"],
                horizontal=True,
                key="usage_period"
            )
        with col_range:
            if "일별" in period:
                lookback_days = st.selectbox("기간", [7, 14, 30, 60, 90], index=2,
                                              format_func=lambda x: f"최근 {x}일")
            elif "주별" in period:
                lookback_weeks = st.selectbox("기간", [4, 8, 12, 24], index=1,
                                               format_func=lambda x: f"최근 {x}주")
                lookback_days = lookback_weeks * 7
            else:  # 월별
                lookback_months = st.selectbox("기간", [3, 6, 12], index=1,
                                                format_func=lambda x: f"최근 {x}개월")
                lookback_days = lookback_months * 31

        # 기간 필터링
        today = date.today()
        cutoff = today - timedelta(days=lookback_days)
        period_logs = [
            l for l in logs
            if l.get("timestamp", "")[:10] >= cutoff.isoformat()
        ]

        st.divider()

        # ── 4개 핵심 메트릭 (오늘 / 이번주 / 이번달 / 기간 전체) ──
        today_str = today.isoformat()
        week_start = (today - timedelta(days=today.weekday())).isoformat()
        month_start = today.replace(day=1).isoformat()
        yesterday_str = (today - timedelta(days=1)).isoformat()

        today_logs = [l for l in logs if l.get("timestamp", "")[:10] == today_str]
        yesterday_logs = [l for l in logs if l.get("timestamp", "")[:10] == yesterday_str]
        week_logs = [l for l in logs if l.get("timestamp", "")[:10] >= week_start]
        month_logs = [l for l in logs if l.get("timestamp", "")[:10] >= month_start]

        today_cost = sum(l.get("cost_usd", 0) for l in today_logs)
        yesterday_cost = sum(l.get("cost_usd", 0) for l in yesterday_logs)
        week_cost = sum(l.get("cost_usd", 0) for l in week_logs)
        month_cost = sum(l.get("cost_usd", 0) for l in month_logs)

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            delta_today = len(today_logs) - len(yesterday_logs)
            st.metric("📅 오늘", f"{len(today_logs)}회",
                      delta=f"{delta_today:+d} vs 어제" if delta_today != 0 else None,
                      help=f"₩{today_cost*USD_TO_KRW:,.0f}")
        with col2:
            st.metric("📆 이번주", f"{len(week_logs)}회",
                      help=f"₩{week_cost*USD_TO_KRW:,.0f}")
        with col3:
            st.metric("🗓️ 이번달", f"{len(month_logs)}회",
                      help=f"₩{month_cost*USD_TO_KRW:,.0f}")
        with col4:
            total_cost = sum(l.get("cost_usd", 0) for l in logs)
            st.metric("💎 누적 비용", f"₩{total_cost*USD_TO_KRW:,.0f}",
                      help=f"${total_cost:.2f}")

        st.divider()

        # ── 기간별 집계 + 차트 ──
        render_section(st, f"📊 {period} 사용량 추이")

        # 데이터 집계
        bucket_calls = defaultdict(int)
        bucket_cost = defaultdict(float)
        bucket_tokens = defaultdict(int)

        for log in period_logs:
            ts = log.get("timestamp", "")
            if not ts:
                continue

            log_date = ts[:10]  # YYYY-MM-DD

            if "일별" in period:
                bucket_key = log_date
            elif "주별" in period:
                # ISO 주 번호 (월요일 시작)
                try:
                    log_dt = datetime.strptime(log_date, "%Y-%m-%d").date()
                    year, week_num, _ = log_dt.isocalendar()
                    bucket_key = f"{year}-W{week_num:02d}"
                except Exception:
                    continue
            else:  # 월별
                bucket_key = log_date[:7]  # YYYY-MM

            bucket_calls[bucket_key] += 1
            bucket_cost[bucket_key] += log.get("cost_usd", 0)
            bucket_tokens[bucket_key] += log.get("input_tokens", 0) + log.get("output_tokens", 0)

        if bucket_calls:
            # 시간순 정렬
            sorted_buckets = sorted(bucket_calls.keys())

            # Streamlit 내장 차트 데이터 준비
            try:
                import pandas as pd
                chart_data = pd.DataFrame({
                    "기간": sorted_buckets,
                    "호출 수": [bucket_calls[b] for b in sorted_buckets],
                    "비용(원)": [round(bucket_cost[b] * USD_TO_KRW) for b in sorted_buckets],
                })
                chart_data = chart_data.set_index("기간")

                # 호출 수 바 차트
                st.write("**호출 수**")
                st.bar_chart(chart_data["호출 수"], height=250)

                # 비용 라인 차트
                st.write("**비용 추이 (KRW)**")
                st.line_chart(chart_data["비용(원)"], height=200)
            except ImportError:
                # pandas 없으면 간단한 progress bar로 대체
                max_calls = max(bucket_calls.values())
                for b in sorted_buckets:
                    pct = bucket_calls[b] / max_calls if max_calls else 0
                    st.write(f"**{b}**: {bucket_calls[b]}회 / ₩{bucket_cost[b]*USD_TO_KRW:,.0f}")
                    st.progress(pct)

            # 상세 테이블
            with st.expander("📋 상세 집계 보기"):
                for b in reversed(sorted_buckets):
                    col1, col2, col3, col4 = st.columns([2, 1, 1, 2])
                    col1.write(f"**{b}**")
                    col2.write(f"{bucket_calls[b]}회")
                    col3.caption(f"{bucket_tokens[b]:,} tok")
                    col4.write(f"₩{bucket_cost[b]*USD_TO_KRW:,.0f}")
        else:
            st.info("선택한 기간 내 사용 기록이 없습니다.")

        st.divider()

        # ── 사용자별 비교 (선택 기간) ──
        render_section(st, f"👥 사용자별 비교 ({period} 기간 내)")

        user_period_calls = defaultdict(int)
        user_period_cost = defaultdict(float)
        user_today_calls = defaultdict(int)
        user_week_calls = defaultdict(int)

        for log in period_logs:
            email = log.get("email", "unknown")
            user_period_calls[email] += 1
            user_period_cost[email] += log.get("cost_usd", 0)

        for log in today_logs:
            user_today_calls[log.get("email", "unknown")] += 1
        for log in week_logs:
            user_week_calls[log.get("email", "unknown")] += 1

        if user_period_calls:
            # 헤더
            col1, col2, col3, col4, col5 = st.columns([3, 1, 1, 1, 2])
            col1.caption("**사용자**")
            col2.caption("**오늘**")
            col3.caption("**이번주**")
            col4.caption("**기간 합계**")
            col5.caption("**비용**")

            # 비용 순 정렬
            sorted_users = sorted(user_period_calls.items(),
                                  key=lambda x: user_period_cost[x[0]], reverse=True)

            for email, calls in sorted_users:
                col1, col2, col3, col4, col5 = st.columns([3, 1, 1, 1, 2])
                # 관리자 표시
                user_info = users.get(email, {})
                badge = " 👑" if user_info.get("is_admin") else ""
                col1.write(f"{email}{badge}")
                col2.write(f"{user_today_calls.get(email, 0)}회")
                col3.write(f"{user_week_calls.get(email, 0)}회")
                col4.write(f"**{calls}회**")
                cost = user_period_cost[email]
                col5.write(f"₩{cost*USD_TO_KRW:,.0f}")
        else:
            st.caption("해당 기간 내 사용자별 데이터 없음")

        st.divider()

        # ── 모델별 사용 분포 ──
        render_section(st, "🤖 모델별 사용 분포 (기간 내)")
        model_stats = {}
        for log in period_logs:
            m = log.get("model", "unknown")
            if m not in model_stats:
                model_stats[m] = {"calls": 0, "cost": 0}
            model_stats[m]["calls"] += 1
            model_stats[m]["cost"] += log.get("cost_usd", 0)

        if model_stats:
            total_model_calls = sum(s["calls"] for s in model_stats.values())
            for model, stats in sorted(model_stats.items(), key=lambda x: x[1]["cost"], reverse=True):
                label = MODEL_PRICES.get(model, {}).get("label", model)
                pct = stats["calls"] / total_model_calls * 100 if total_model_calls else 0

                col1, col2, col3, col4 = st.columns([3, 1, 1, 2])
                col1.write(f"**{label}**")
                col2.write(f"{stats['calls']}회")
                col3.write(f"{pct:.1f}%")
                col4.write(f"₩{stats['cost']*USD_TO_KRW:,.0f}")
                st.progress(pct / 100)
        else:
            st.caption("해당 기간 내 모델 데이터 없음")

    # ─── 탭 2: 사용자 관리 ───────────────────────────────
    with tab_users:
        st.subheader("👥 전체 사용자 목록")

        approved_users = {e: u for e, u in users.items() if u.get("approved")}
        st.caption(f"승인된 사용자: **{len(approved_users)}명**")

        for email, info in users.items():
            if not info.get("approved"):
                continue  # 대기 중인 사용자는 탭 3에서 처리

            with st.container():
                col1, col2, col3, col4, col5 = st.columns([3, 2, 1, 1, 1])

                col1.write(f"**{email}**")
                col1.caption(
                    f"{info.get('name', '-')} · {info.get('company', '-')} · "
                    f"가입: {info.get('created_at', '-')}"
                )

                col2.metric("이번 달 사용", f"{info.get('usage_count', 0)}회",
                            help=f"한도: {MAX_MONTHLY_LIMIT}회 / 월")

                if info.get("is_admin"):
                    col3.info("👑 관리자")
                else:
                    col3.write("")

                # 정지/해제
                if not info.get("is_admin") and email != st.session_state.user_email:
                    if info.get("suspended"):
                        if col4.button("✓해제", key=f"unsus_{email}"):
                            users[email]["suspended"] = False
                            gist_save(_users_filename(), users_db)
                            st.rerun()
                    else:
                        if col4.button("⛔정지", key=f"sus_{email}"):
                            users[email]["suspended"] = True
                            gist_save(_users_filename(), users_db)
                            st.rerun()

                    if col5.button("🗑️", key=f"del_{email}"):
                        del users[email]
                        gist_save(_users_filename(), users_db)
                        st.rerun()

                st.divider()

    # ─── 탭 3: 승인 대기 ───────────────────────────────
    with tab_pending:
        pending = {e: u for e, u in users.items() if not u.get("approved")}
        st.subheader(f"✋ 승인 대기 사용자 ({len(pending)}명)")

        if not pending:
            st.success("✅ 대기 중인 사용자가 없습니다.")
        else:
            for email, info in pending.items():
                with st.container():
                    st.markdown(f"### 📧 {email}")
                    col1, col2 = st.columns(2)
                    col1.write(f"**이름**: {info.get('name', '-')}")
                    col1.write(f"**회사**: {info.get('company', '-')}")
                    col2.write(f"**신청일**: {info.get('created_at', '-')}")
                    col2.write(f"**사용 목적**: {info.get('purpose', '-')}")

                    btn1, btn2, _ = st.columns([1, 1, 4])
                    if btn1.button("✅ 승인", key=f"approve_{email}", type="primary"):
                        users[email]["approved"] = True
                        gist_save(_users_filename(), users_db)
                        st.success(f"{email} 승인 완료!")
                        st.rerun()

                    if btn2.button("❌ 거부", key=f"reject_{email}"):
                        del users[email]
                        gist_save(_users_filename(), users_db)
                        st.rerun()

                    st.divider()

    # ─── 탭 4: 상세 로그 ───────────────────────────────
    with tab_logs:
        st.subheader("📜 API 호출 상세 로그")

        # 필터
        col1, col2 = st.columns([3, 1])
        with col1:
            filter_email = st.selectbox(
                "사용자 필터",
                options=["(전체)"] + sorted(set(l.get("email", "") for l in logs))
            )
        with col2:
            limit = st.number_input("표시 개수", min_value=10, max_value=500, value=50, step=10)

        # 필터 적용
        filtered_logs = logs
        if filter_email != "(전체)":
            filtered_logs = [l for l in logs if l.get("email") == filter_email]

        filtered_logs = sorted(filtered_logs, key=lambda x: x.get("timestamp", ""), reverse=True)[:limit]

        st.caption(f"전체 {len(logs):,}건 중 {len(filtered_logs):,}건 표시")

        # 테이블
        if filtered_logs:
            for log in filtered_logs:
                ts = log.get("timestamp", "")[:19].replace("T", " ")
                email = log.get("email", "-")
                model = log.get("model", "-")
                model_label = MODEL_PRICES.get(model, {}).get("label", model)
                action = log.get("action", "-")
                in_tok = log.get("input_tokens", 0)
                out_tok = log.get("output_tokens", 0)
                cost = log.get("cost_usd", 0)

                col1, col2, col3, col4, col5 = st.columns([2, 3, 2, 2, 1])
                col1.caption(ts)
                col2.write(f"{email}")
                col2.caption(action)
                col3.write(model_label)
                col4.caption(f"in: {in_tok:,} / out: {out_tok:,}")
                col5.write(f"${cost:.4f}")

            # CSV 다운로드
            csv_lines = ["timestamp,email,model,action,input_tokens,output_tokens,cost_usd"]
            for log in filtered_logs:
                csv_lines.append(
                    f"{log.get('timestamp','')},{log.get('email','')},{log.get('model','')},"
                    f"{log.get('action','')},{log.get('input_tokens',0)},{log.get('output_tokens',0)},"
                    f"{log.get('cost_usd',0)}"
                )
            csv_content = "\n".join(csv_lines)

            st.download_button(
                "📥 로그 CSV 다운로드",
                data=csv_content.encode("utf-8-sig"),
                file_name=f"usage_logs_{date.today().isoformat()}.csv",
                mime="text/csv"
            )
        else:
            st.info("표시할 로그가 없습니다.")

    st.divider()
    render_section(st, "📊 평가지표 정보")
    col_mb, col_ib = st.columns(2)
    with col_mb:
        st.markdown("""
        **🏆 메인비즈**
        - 버전: 2026.01
        - 업종: 4개 (제조·서비스·건설·IT)
        - 항목: 16개 (4분야 × 4항목)
        - 통과: 자가진단 600 / 현장 700
        """)
    with col_ib:
        st.markdown("""
        **🚀 이노비즈**
        - 버전: 2026.01
        - 업종: 4개 (제조·서비스·건설·IT)
        - 항목: 16개 (시스템) + 11개 (기술등급)
        - 통과: 자가진단 650 / 현장 700 + 기술등급 B 이상
        """)


# =====================================================================
# 🚪 메인 라우터
# =====================================================================
def main():
    init_auth()

    # 🎨 RSV 디자인 CSS 주입 (모든 페이지에 적용)
    inject_css(st)

    if not st.session_state.user_email:
        login_screen()
        return

    with st.sidebar:
        st.success(f"👤 {st.session_state.user_email}")
        if st.session_state.is_admin:
            st.caption("👑 관리자 (무제한)")
        else:
            # 사용량 표시
            users_db_temp = gist_load(_users_filename(), get_default_users_db)
            user_info = users_db_temp.get("users", {}).get(st.session_state.user_email, {})
            used = user_info.get("usage_count", 0)
            remaining = max(MAX_MONTHLY_LIMIT - used, 0)
            st.caption(f"💎 이번 달: {used} / {MAX_MONTHLY_LIMIT}회 (남음: {remaining})")
            st.progress(min(used / MAX_MONTHLY_LIMIT, 1.0))

        if st.button("🚪 로그아웃", use_container_width=True):
            st.session_state.user_email = None
            st.session_state.is_admin = False
            st.rerun()

        st.divider()
        menu_options = [
            "🏠 대시보드",
            "🏢 고객사 관리",
            "📊 메인비즈 진단",
            "📊 이노비즈 진단",
            "🎓 이노비즈 기술등급 평가",
            "📋 신청 워크플로우",
            "📖 메인비즈 가이드북",
            "📖 이노비즈 가이드북",
        ]
        if st.session_state.is_admin:
            menu_options.append("⚙️ 관리자")

        menu = st.radio("메뉴", menu_options)

    if menu == "🏠 대시보드":
        dashboard_page()
    elif menu == "🏢 고객사 관리":
        companies_page()
    elif menu == "📊 메인비즈 진단":
        mainbiz_assessment_page()
    elif menu == "📊 이노비즈 진단":
        innobiz_assessment_page()
    elif menu == "🎓 이노비즈 기술등급 평가":
        tech_grade_page()
    elif menu == "📋 신청 워크플로우":
        workflow_page()
    elif menu == "📖 메인비즈 가이드북":
        render_guidebook_page(st, "메인비즈")
    elif menu == "📖 이노비즈 가이드북":
        render_guidebook_page(st, "이노비즈")
    elif menu == "⚙️ 관리자":
        admin_page()

if __name__ == "__main__":
    main()
