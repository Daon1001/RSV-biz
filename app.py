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
    st.title("🏆 메인비즈·이노비즈 AI 마스터 컨설턴트")
    st.caption("컨설턴트 내부용 통합 관리 시스템 v2.0")

    tab_login, tab_signup = st.tabs(["🔑 로그인", "✍️ 회원가입"])
    users_db = gist_load(_users_filename(), get_default_users_db)

    with tab_login:
        email = st.text_input("이메일", key="login_email")
        if st.button("로그인", type="primary", use_container_width=True):
            user = users_db.get("users", {}).get(email)
            if not user:
                st.error("등록되지 않은 이메일입니다.")
            elif not user.get("approved"):
                st.warning("관리자 승인 대기 중입니다.")
            else:
                st.session_state.user_email = email
                st.session_state.is_admin = user.get("is_admin", False)
                st.rerun()

    with tab_signup:
        new_email = st.text_input("이메일", key="signup_email")
        if st.button("가입 신청", use_container_width=True):
            if not new_email or "@" not in new_email:
                st.error("올바른 이메일을 입력하세요.")
            elif new_email in users_db.get("users", {}):
                st.warning("이미 가입된 이메일입니다.")
            else:
                users_db.setdefault("users", {})[new_email] = {
                    "approved": False, "is_admin": False,
                    "created_at": date.today().isoformat(),
                    "usage_count": 0
                }
                if gist_save(_users_filename(), users_db):
                    st.success("가입 신청 완료! 관리자 승인 후 이용 가능합니다.")

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
            options=["manufacturing", "service", "construction"],
            format_func=lambda x: {"manufacturing": "🏭 제조업",
                                   "service": "💼 서비스업",
                                   "construction": "🏗️ 건설업"}[x],
            index=["manufacturing", "service", "construction"].index(default_industry),
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
        if st.button("🤖 AI 컨설팅 리포트 생성", type="secondary", use_container_width=True):
            with st.spinner("Claude가 분석 중... (10~20초)"):
                report = generate_ai_report(
                    selected_company, industry, criteria,
                    category_scores, total_score, item_gaps[:5]
                )
                st.session_state["mb_ai_report"] = report
            st.rerun()

    if "mb_ai_report" in st.session_state:
        st.divider()
        st.subheader("🤖 AI 컨설팅 리포트")
        st.markdown(st.session_state["mb_ai_report"])

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
                        cat_scores: dict, total: int, top_gaps: list) -> str:
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
            model="claude-sonnet-4-5",
            max_tokens=2500,
            messages=[{"role": "user", "content": prompt}]
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
                    options=["manufacturing", "service", "construction"],
                    format_func=lambda x: {"manufacturing": "🏭 제조업",
                                           "service": "💼 서비스업",
                                           "construction": "🏗️ 건설업"}[x]
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
                industry_emoji = {"manufacturing": "🏭", "service": "💼", "construction": "🏗️"}.get(
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

                    if co.get("memo"):
                        st.caption(f"💬 {co['memo']}")

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

def workflow_page():
    st.header("📋 메인비즈 신청 워크플로우")

    companies_db = gist_load(_companies_filename(), get_default_companies_db)
    companies = companies_db.get("companies", {})

    if not companies:
        st.info("먼저 고객사를 등록하세요.")
        return

    selected_co = st.selectbox("고객사 선택", list(companies.keys()))

    co_data = companies[selected_co]
    workflow = co_data.setdefault("mainbiz_workflow", {"stages": {}})

    completed = sum(1 for s in WORKFLOW_STAGES_MAINBIZ
                    if workflow["stages"].get(s, {}).get("done"))
    progress_pct = completed / len(WORKFLOW_STAGES_MAINBIZ) * 100
    st.progress(progress_pct / 100,
                text=f"진행률: {completed}/{len(WORKFLOW_STAGES_MAINBIZ)} 단계 ({progress_pct:.0f}%)")

    st.divider()

    changed = False
    for stage in WORKFLOW_STAGES_MAINBIZ:
        stage_data = workflow["stages"].get(stage, {"done": False, "memo": "", "completed_at": ""})

        col_check, col_memo = st.columns([2, 3])
        with col_check:
            done = st.checkbox(stage, value=stage_data["done"], key=f"wf_{stage}")
            if done != stage_data["done"]:
                stage_data["done"] = done
                stage_data["completed_at"] = datetime.now().isoformat() if done else ""
                changed = True
        with col_memo:
            memo = st.text_input("메모", value=stage_data.get("memo", ""),
                                 key=f"wfm_{stage}",
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
            companies_db["companies"][selected_co]["mainbiz_workflow"] = workflow
            if gist_save(_companies_filename(), companies_db):
                st.success("저장 완료!")
                st.rerun()

# =====================================================================
# 🏠 대시보드
# =====================================================================
def dashboard_page():
    st.title("🏆 메인비즈·이노비즈 AI 마스터 컨설턴트")
    st.caption("컨설턴트 내부용 통합 관리 시스템 v2.0")

    companies_db = gist_load(_companies_filename(), get_default_companies_db)
    companies = companies_db.get("companies", {})

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("등록 고객사", len(companies))

    mb_count = sum(1 for c in companies.values()
                   if c.get("mainbiz_assessment", {}).get("total_score"))
    col2.metric("진단 완료", mb_count)

    pass_count = sum(1 for c in companies.values()
                     if c.get("mainbiz_assessment", {}).get("total_score", 0) >= 700)
    col3.metric("현장평가 가능", pass_count)

    all_scores = [c["mainbiz_assessment"]["total_score"] for c in companies.values()
                  if c.get("mainbiz_assessment", {}).get("total_score")]
    avg = sum(all_scores) / len(all_scores) if all_scores else 0
    col4.metric("평균 점수", f"{avg:.0f}점")

    st.divider()

    col_info, col_recent = st.columns(2)
    with col_info:
        st.info("""
        **🏆 메인비즈 (경영혁신형 중소기업)**
        - 자가진단 **600점** 이상 → 현장평가 신청 가능
        - 현장평가 **700점** 이상 → 인증 발급
        - 평가기관: 신보 / 기보 / KPC
        - 유효기간: **3년**
        - 수수료: 신규 55만원 / 연장 44만원
        """)
    with col_recent:
        st.subheader("📋 최근 진단 이력")
        recent = []
        for name, c in companies.items():
            mb = c.get("mainbiz_assessment", {})
            if mb.get("total_score"):
                recent.append({
                    "company": name,
                    "total": mb["total_score"],
                    "date": mb.get("evaluated_at", "")[:10],
                    "industry": mb.get("industry", "")
                })
        recent.sort(key=lambda x: x["date"], reverse=True)

        if recent:
            for r in recent[:5]:
                emoji = {"manufacturing": "🏭", "service": "💼", "construction": "🏗️"}.get(r["industry"], "")
                st.write(f"- **{r['date']}** | {emoji} {r['company']}: {r['total']}점")
        else:
            st.caption("아직 진단 기록이 없습니다.")

# =====================================================================
# ⚙️ 관리자
# =====================================================================
def admin_page():
    st.header("⚙️ 관리자 패널")

    users_db = gist_load(_users_filename(), get_default_users_db)
    users = users_db.get("users", {})

    st.subheader("👥 사용자 관리")
    for email, info in users.items():
        col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
        col1.write(f"**{email}**")
        col1.caption(f"가입: {info.get('created_at', '-')} | 사용: {info.get('usage_count', 0)}회")

        if info.get("approved"):
            col2.success("✅ 승인")
        else:
            if col2.button("승인", key=f"approve_{email}"):
                users[email]["approved"] = True
                gist_save(_users_filename(), users_db)
                st.rerun()

        if info.get("is_admin"):
            col3.info("👑 관리자")

        if email != st.session_state.user_email:
            if col4.button("🗑️", key=f"del_{email}"):
                del users[email]
                gist_save(_users_filename(), users_db)
                st.rerun()

    st.divider()
    st.subheader("📊 평가지표 정보")
    st.write("**현재 버전**: 2026.01")
    st.write("**지원 업종**: 제조업, 서비스업, 건설업")
    st.write("**항목 수**: 16개 (4분야 × 4항목)")
    st.caption("⚠️ 정기 동기화 기능은 향후 GitHub Actions 크론으로 구현 예정")

# =====================================================================
# 🚪 메인 라우터
# =====================================================================
def main():
    init_auth()

    if not st.session_state.user_email:
        login_screen()
        return

    with st.sidebar:
        st.success(f"👤 {st.session_state.user_email}")
        if st.session_state.is_admin:
            st.caption("👑 관리자")
        if st.button("🚪 로그아웃", use_container_width=True):
            st.session_state.user_email = None
            st.session_state.is_admin = False
            st.rerun()

        st.divider()
        menu_options = [
            "🏠 대시보드",
            "🏢 고객사 관리",
            "📊 메인비즈 진단",
            "📋 신청 워크플로우",
        ]
        if st.session_state.is_admin:
            menu_options.append("⚙️ 관리자")

        menu = st.radio("메뉴", menu_options)

        st.divider()
        st.caption("📌 **이노비즈 모듈**은 메인비즈 안정화 후 추가 예정")

    if menu == "🏠 대시보드":
        dashboard_page()
    elif menu == "🏢 고객사 관리":
        companies_page()
    elif menu == "📊 메인비즈 진단":
        mainbiz_assessment_page()
    elif menu == "📋 신청 워크플로우":
        workflow_page()
    elif menu == "⚙️ 관리자":
        admin_page()

if __name__ == "__main__":
    main()
