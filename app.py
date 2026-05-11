"""
메인비즈·이노비즈 AI 마스터 컨설턴트
- 컨설턴트 내부용 통합 관리 시스템
- 자가진단 시뮬레이션 + 컨설팅 관리 + 신청 워크플로우
"""
import streamlit as st
import anthropic
import json
import requests
from datetime import datetime, date
from typing import Dict, Any, List, Optional

# ── 페이지 설정 ──
st.set_page_config(
    page_title="메인비즈·이노비즈 AI 마스터 컨설턴트",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================================
# 🔒 GitHub Gist DB 시스템 (벤처/연구소 앱과 동일 패턴)
# =====================================================================
def _gist_headers():
    token = st.secrets.get("github_token", "")
    if not token:
        return None
    return {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}

def _gist_id():
    return st.secrets.get("gist_id", "")

def _users_filename():
    # 메인비즈·이노비즈 전용 사용자 파일 (벤처/연구소와 분리)
    return st.secrets.get("mainnoinno_users_filename", "mainnoinno_users.json")

def _companies_filename():
    # 고객사 데이터 파일
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
# 📊 평가지표 마스터 데이터 (정기 동기화 대상)
# =====================================================================
# 실제 운영 시에는 정기 크론으로 메인비즈넷/이노비즈넷에서 동기화
# 현재는 공식 평가지표 기반 하드코딩 (v2026.01 기준)

MAINBIZ_CRITERIA = {
    "version": "2026.01",
    "total_score": 1000,
    "self_pass": 600,
    "field_pass": 700,
    "categories": [
        {
            "id": "strategy",
            "name": "전략기획 및 이행관리",
            "weight": 250,
            "items": [
                {"id": "s1", "name": "비전·미션 수립 및 공유", "max": 50},
                {"id": "s2", "name": "중장기 경영전략 수립", "max": 60},
                {"id": "s3", "name": "연간 사업계획 수립 및 실행", "max": 70},
                {"id": "s4", "name": "전략 실행 모니터링 체계", "max": 70},
            ]
        },
        {
            "id": "performance",
            "name": "성과관리",
            "weight": 250,
            "items": [
                {"id": "p1", "name": "성과지표(KPI) 설정", "max": 60},
                {"id": "p2", "name": "성과 측정 및 분석", "max": 60},
                {"id": "p3", "name": "재무성과 (매출·이익률 추이)", "max": 70},
                {"id": "p4", "name": "비재무성과 (고객만족·품질)", "max": 60},
            ]
        },
        {
            "id": "organization",
            "name": "조직 및 인력관리",
            "weight": 250,
            "items": [
                {"id": "o1", "name": "조직구조 및 직무체계", "max": 60},
                {"id": "o2", "name": "인사평가 및 보상체계", "max": 70},
                {"id": "o3", "name": "교육훈련 및 역량개발", "max": 60},
                {"id": "o4", "name": "조직문화 및 소통", "max": 60},
            ]
        },
        {
            "id": "esg",
            "name": "사회 신뢰 활동 (ESG경영)",
            "weight": 250,
            "items": [
                {"id": "e1", "name": "환경경영 (Environment)", "max": 70},
                {"id": "e2", "name": "사회적 책임 (Social)", "max": 70},
                {"id": "e3", "name": "지배구조 (Governance)", "max": 60},
                {"id": "e4", "name": "이해관계자 관계", "max": 50},
            ]
        },
    ]
}

INNOBIZ_CRITERIA = {
    "version": "2026.01",
    "total_score": 1000,
    "self_pass": 650,
    "field_pass": 700,
    "tech_grade_min": "B",
    "categories": [
        {
            "id": "innovation",
            "name": "기술혁신능력",
            "weight": 300,
            "items": [
                {"id": "i1", "name": "연구개발(R&D) 조직 운영", "max": 70},
                {"id": "i2", "name": "연구전담인력 보유", "max": 80},
                {"id": "i3", "name": "R&D 투자 비율", "max": 80},
                {"id": "i4", "name": "지식재산권 보유 현황", "max": 70},
            ]
        },
        {
            "id": "commercialization",
            "name": "기술사업화능력",
            "weight": 250,
            "items": [
                {"id": "c1", "name": "기술의 시장성", "max": 70},
                {"id": "c2", "name": "사업화 계획 수립", "max": 60},
                {"id": "c3", "name": "신제품 매출 비중", "max": 70},
                {"id": "c4", "name": "사업화 인프라", "max": 50},
            ]
        },
        {
            "id": "management",
            "name": "기술혁신경영능력",
            "weight": 250,
            "items": [
                {"id": "m1", "name": "기술전략 수립", "max": 60},
                {"id": "m2", "name": "기술 정보화 수준", "max": 60},
                {"id": "m3", "name": "품질관리 체계", "max": 70},
                {"id": "m4", "name": "기술협력 네트워크", "max": 60},
            ]
        },
        {
            "id": "achievement",
            "name": "기술혁신성과",
            "weight": 200,
            "items": [
                {"id": "a1", "name": "매출액 증가율", "max": 60},
                {"id": "a2", "name": "수익성 (영업이익률)", "max": 50},
                {"id": "a3", "name": "고용 증가율", "max": 40},
                {"id": "a4", "name": "기술인증·수상실적", "max": 50},
            ]
        },
    ]
}

# =====================================================================
# 🔐 인증 시스템
# =====================================================================
def init_auth():
    if "user_email" not in st.session_state:
        st.session_state.user_email = None
        st.session_state.is_admin = False

def login_screen():
    st.title("🏆 메인비즈·이노비즈 AI 마스터 컨설턴트")
    st.caption("컨설턴트 내부용 통합 관리 시스템")

    tab_login, tab_signup = st.tabs(["🔑 로그인", "✍️ 회원가입"])

    users_db = gist_load(_users_filename(), get_default_users_db)

    with tab_login:
        email = st.text_input("이메일", key="login_email")
        if st.button("로그인", type="primary", use_container_width=True):
            user = users_db.get("users", {}).get(email)
            if not user:
                st.error("등록되지 않은 이메일입니다. 회원가입을 먼저 진행하세요.")
            elif not user.get("approved"):
                st.warning("관리자 승인 대기 중입니다.")
            else:
                st.session_state.user_email = email
                st.session_state.is_admin = user.get("is_admin", False)
                st.rerun()

    with tab_signup:
        new_email = st.text_input("이메일 (회사 이메일 권장)", key="signup_email")
        if st.button("가입 신청", use_container_width=True):
            if not new_email or "@" not in new_email:
                st.error("올바른 이메일을 입력하세요.")
            elif new_email in users_db.get("users", {}):
                st.warning("이미 가입된 이메일입니다.")
            else:
                users_db.setdefault("users", {})[new_email] = {
                    "approved": False, "is_admin": False,
                    "created_at": date.today().isoformat(),
                    "usage_count": 0,
                    "last_reset_month": date.today().month
                }
                if gist_save(_users_filename(), users_db):
                    st.success("가입 신청 완료! 관리자 승인 후 이용 가능합니다.")
                else:
                    st.error("저장 실패. 관리자에게 문의하세요.")

# =====================================================================
# 📊 자가진단 시뮬레이터
# =====================================================================
def simulator_page(certification_type: str):
    criteria = MAINBIZ_CRITERIA if certification_type == "메인비즈" else INNOBIZ_CRITERIA

    st.header(f"📊 {certification_type} 자가진단 시뮬레이터")
    st.caption(f"평가지표 버전: {criteria['version']} | "
               f"자가진단 통과: {criteria['self_pass']}점 | "
               f"현장평가 통과: {criteria['field_pass']}점")

    # 고객사 선택
    companies_db = gist_load(_companies_filename(), get_default_companies_db)
    company_list = ["[새 진단]"] + list(companies_db.get("companies", {}).keys())
    selected_company = st.selectbox("고객사 선택", company_list, key=f"sim_co_{certification_type}")

    # 기존 진단 데이터 로드
    saved_scores = {}
    if selected_company != "[새 진단]":
        co_data = companies_db.get("companies", {}).get(selected_company, {})
        saved_scores = co_data.get("assessments", {}).get(certification_type, {}).get("scores", {})

    st.divider()

    # 카테고리별 점수 입력
    total_score = 0
    total_max = 0
    category_scores = {}
    item_scores = {}

    for cat in criteria["categories"]:
        with st.expander(f"**{cat['name']}** (배점 {cat['weight']}점)", expanded=True):
            cat_score = 0
            cat_max = 0
            cols = st.columns(2)
            for idx, item in enumerate(cat["items"]):
                with cols[idx % 2]:
                    default = saved_scores.get(item["id"], int(item["max"] * 0.7))
                    score = st.slider(
                        f"{item['name']} (최대 {item['max']}점)",
                        min_value=0, max_value=item["max"],
                        value=default,
                        key=f"{certification_type}_{item['id']}"
                    )
                    item_scores[item["id"]] = score
                    cat_score += score
                    cat_max += item["max"]

            pct = (cat_score / cat_max * 100) if cat_max > 0 else 0
            st.progress(pct / 100, text=f"분야 점수: {cat_score} / {cat_max} ({pct:.1f}%)")
            category_scores[cat["id"]] = {"name": cat["name"], "score": cat_score, "max": cat_max}
            total_score += cat_score
            total_max += cat_max

    st.divider()

    # 결과 표시
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("총점", f"{total_score} / {total_max}")
    with col2:
        st.metric("자가진단 통과 기준", f"{criteria['self_pass']}점",
                  delta=f"{total_score - criteria['self_pass']:+d}점")
    with col3:
        st.metric("현장평가 통과 기준", f"{criteria['field_pass']}점",
                  delta=f"{total_score - criteria['field_pass']:+d}점")

    # 통과 여부 판정
    if total_score >= criteria["field_pass"]:
        st.success(f"✅ 현장평가 통과 기준({criteria['field_pass']}점) 충족! 신청 가능 상태입니다.")
    elif total_score >= criteria["self_pass"]:
        st.warning(f"⚠️ 자가진단은 통과({criteria['self_pass']}점)했으나 현장평가 기준({criteria['field_pass']}점) 미달."
                   f" 보완 필요: {criteria['field_pass'] - total_score}점")
    else:
        st.error(f"❌ 자가진단 통과 기준({criteria['self_pass']}점) 미달. 신청 불가."
                 f" 추가 필요: {criteria['self_pass'] - total_score}점")

    # 이노비즈 추가 안내
    if certification_type == "이노비즈":
        st.info(f"📌 이노비즈는 시스템 점수 외에 **개별기술수준 평가 {criteria['tech_grade_min']}등급 이상**도 필요합니다.")

    # 저장 + AI 분석
    st.divider()
    col_save, col_ai = st.columns(2)
    with col_save:
        if selected_company != "[새 진단]":
            if st.button("💾 진단 결과 저장", use_container_width=True):
                companies_db.setdefault("companies", {}).setdefault(selected_company, {}) \
                    .setdefault("assessments", {})[certification_type] = {
                    "scores": item_scores,
                    "total": total_score,
                    "evaluated_at": datetime.now().isoformat(),
                    "evaluator": st.session_state.user_email
                }
                if gist_save(_companies_filename(), companies_db):
                    st.success("저장 완료!")

    with col_ai:
        if st.button("🤖 AI 컨설팅 리포트 생성", type="primary", use_container_width=True):
            with st.spinner("Claude가 분석 중..."):
                report = generate_ai_report(
                    certification_type, selected_company,
                    category_scores, total_score, criteria
                )
                st.session_state[f"ai_report_{certification_type}"] = report
            st.rerun()

    # AI 리포트 표시
    if f"ai_report_{certification_type}" in st.session_state:
        st.divider()
        st.subheader("🤖 AI 컨설팅 리포트")
        st.markdown(st.session_state[f"ai_report_{certification_type}"])

# =====================================================================
# 🤖 Claude AI 분석
# =====================================================================
def get_claude_client():
    api_key = st.secrets.get("anthropic_api_key", "")
    if not api_key:
        st.error("Claude API 키가 설정되지 않았습니다.")
        return None
    return anthropic.Anthropic(api_key=api_key)

def generate_ai_report(cert_type: str, company: str, cat_scores: Dict, total: int, criteria: Dict) -> str:
    client = get_claude_client()
    if not client:
        return "API 키 미설정으로 분석 불가."

    category_summary = "\n".join([
        f"- {v['name']}: {v['score']}/{v['max']}점 ({v['score']/v['max']*100:.1f}%)"
        for v in cat_scores.values()
    ])

    pass_status = (
        "현장평가 통과 가능" if total >= criteria["field_pass"]
        else "자가진단만 통과 (현장평가 미달)" if total >= criteria["self_pass"]
        else "자가진단 미달 (신청 불가)"
    )

    prompt = f"""당신은 {cert_type} 인증 컨설팅 전문가입니다.

[고객사] {company if company != '[새 진단]' else '신규 진단'}
[인증 종류] {cert_type}
[총점] {total} / {criteria['total_score']}
[현재 상태] {pass_status}
[통과 기준] 자가진단 {criteria['self_pass']}점 / 현장평가 {criteria['field_pass']}점

[분야별 점수]
{category_summary}

다음 형식으로 컨설팅 리포트를 작성하세요:

## 1. 종합 진단
현재 상태를 2-3문장으로 요약

## 2. 강점 분야
점수 비율이 높은 분야 분석

## 3. 취약 분야 및 보완 방안
점수 비율이 낮은 분야를 구체적으로 어떻게 개선할지 (실무 액션 위주)

## 4. 우선 개선 과제 TOP 3
가장 효과적으로 점수를 올릴 수 있는 3가지 액션

## 5. 신청 전략
{cert_type}의 특성에 맞춰 신청 시점과 준비 방향 제안
"""
    try:
        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=2000,
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
                industry = st.text_input("업종")
            with col2:
                est_year = st.number_input("설립연도", min_value=1950, max_value=date.today().year, value=2020)
                ceo = st.text_input("대표자")
                contact = st.text_input("담당자 연락처")

            target_certs = st.multiselect("진행 예정 인증",
                                          ["메인비즈", "이노비즈", "벤처기업", "기업부설연구소"])
            memo = st.text_area("메모")

            if st.form_submit_button("등록", type="primary"):
                if not name:
                    st.error("회사명은 필수입니다.")
                elif name in companies:
                    st.error("이미 등록된 회사명입니다.")
                else:
                    companies[name] = {
                        "biz_no": biz_no, "industry": industry,
                        "est_year": est_year, "ceo": ceo,
                        "contact": contact, "target_certs": target_certs,
                        "memo": memo,
                        "created_at": datetime.now().isoformat(),
                        "created_by": st.session_state.user_email,
                        "assessments": {}, "workflow": {}
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
                with st.expander(f"**{name}** ({co.get('industry', '-')})"):
                    col1, col2, col3 = st.columns(3)
                    col1.write(f"**대표**: {co.get('ceo', '-')}")
                    col1.write(f"**설립**: {co.get('est_year', '-')}년")
                    col2.write(f"**사업자번호**: {co.get('biz_no', '-')}")
                    col2.write(f"**연락처**: {co.get('contact', '-')}")
                    col3.write(f"**진행 인증**: {', '.join(co.get('target_certs', [])) or '-'}")

                    # 진단 이력
                    assessments = co.get("assessments", {})
                    if assessments:
                        st.write("**진단 이력**")
                        for cert, data in assessments.items():
                            st.write(f"- {cert}: {data.get('total', 0)}점 ({data.get('evaluated_at', '')[:10]})")

                    if co.get("memo"):
                        st.caption(f"💬 {co['memo']}")

# =====================================================================
# 📋 신청 워크플로우
# =====================================================================
WORKFLOW_STAGES = {
    "메인비즈": [
        "1. 자격 확인 (업력 3년 이상, 결격사유 없음)",
        "2. 메인비즈넷 회원가입 및 기업등록",
        "3. 재무정보 입력",
        "4. 온라인 자가진단 (600점 이상)",
        "5. 평가기관 선택 및 현장평가 신청",
        "6. 증빙자료 준비",
        "7. 현장평가 실시 (700점 이상)",
        "8. 지방중기청 발급 승인 요청",
        "9. 메인비즈 확인서 발급 (유효기간 3년)",
    ],
    "이노비즈": [
        "1. 자격 확인 (업력 3년 이상, 기술혁신활동 입증)",
        "2. 이노비즈넷 회원가입 및 기업등록",
        "3. 재무정보 및 기술사업계획서 작성",
        "4. 온라인 자가진단 (650점 이상)",
        "5. 신청 접수 및 수수료 납부 (77만원)",
        "6. 기술보증기금 현장평가 신청",
        "7. 증빙자료 준비 (특허, R&D 실적 등)",
        "8. 현장평가 실시 (700점 이상 + 기술등급 B 이상)",
        "9. 이노비즈 확인서 발급 (유효기간 3년)",
    ]
}

def workflow_page():
    st.header("📋 신청 워크플로우 트래커")

    companies_db = gist_load(_companies_filename(), get_default_companies_db)
    companies = companies_db.get("companies", {})

    if not companies:
        st.info("먼저 고객사를 등록하세요.")
        return

    selected_co = st.selectbox("고객사 선택", list(companies.keys()))
    cert_type = st.radio("인증 종류", ["메인비즈", "이노비즈"], horizontal=True)

    co_data = companies[selected_co]
    workflow = co_data.setdefault("workflow", {}).setdefault(cert_type, {"stages": {}, "started_at": ""})

    st.divider()

    # 진행률 표시
    stages = WORKFLOW_STAGES[cert_type]
    completed = sum(1 for s in stages if workflow["stages"].get(s, {}).get("done"))
    progress_pct = completed / len(stages) * 100
    st.progress(progress_pct / 100, text=f"진행률: {completed}/{len(stages)} 단계 ({progress_pct:.0f}%)")

    st.divider()

    # 단계별 체크리스트
    changed = False
    for stage in stages:
        stage_data = workflow["stages"].get(stage, {"done": False, "memo": "", "completed_at": ""})

        col_check, col_memo = st.columns([1, 3])
        with col_check:
            done = st.checkbox(stage, value=stage_data["done"], key=f"wf_{cert_type}_{stage}")
            if done != stage_data["done"]:
                stage_data["done"] = done
                stage_data["completed_at"] = datetime.now().isoformat() if done else ""
                changed = True
        with col_memo:
            memo = st.text_input("메모", value=stage_data.get("memo", ""),
                                 key=f"wf_memo_{cert_type}_{stage}",
                                 label_visibility="collapsed", placeholder="메모...")
            if memo != stage_data.get("memo", ""):
                stage_data["memo"] = memo
                changed = True

        if stage_data.get("completed_at"):
            st.caption(f"  ✓ 완료: {stage_data['completed_at'][:10]}")

        workflow["stages"][stage] = stage_data

    if changed:
        if st.button("💾 진행 상황 저장", type="primary", use_container_width=True):
            companies_db["companies"][selected_co]["workflow"][cert_type] = workflow
            if gist_save(_companies_filename(), companies_db):
                st.success("저장 완료!")
                st.rerun()

# =====================================================================
# ⚙️ 관리자 패널
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
            col2.success("✅ 승인됨")
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
    st.subheader("📊 평가지표 버전 정보")
    col1, col2 = st.columns(2)
    col1.metric("메인비즈 평가지표", MAINBIZ_CRITERIA["version"])
    col2.metric("이노비즈 평가지표", INNOBIZ_CRITERIA["version"])
    st.caption("⚠️ 평가지표 정기 동기화 기능은 향후 GitHub Actions 크론으로 구현 예정")

# =====================================================================
# 🚪 메인
# =====================================================================
def main():
    init_auth()

    if not st.session_state.user_email:
        login_screen()
        return

    # 사이드바
    with st.sidebar:
        st.success(f"👤 {st.session_state.user_email}")
        if st.session_state.is_admin:
            st.caption("👑 관리자")
        if st.button("🚪 로그아웃", use_container_width=True):
            st.session_state.user_email = None
            st.session_state.is_admin = False
            st.rerun()

        st.divider()
        menu = st.radio("메뉴", [
            "🏠 대시보드",
            "🏢 고객사 관리",
            "📊 메인비즈 진단",
            "📊 이노비즈 진단",
            "📋 신청 워크플로우",
        ] + (["⚙️ 관리자"] if st.session_state.is_admin else []))

    # 메뉴 라우팅
    if menu == "🏠 대시보드":
        dashboard_page()
    elif menu == "🏢 고객사 관리":
        companies_page()
    elif menu == "📊 메인비즈 진단":
        simulator_page("메인비즈")
    elif menu == "📊 이노비즈 진단":
        simulator_page("이노비즈")
    elif menu == "📋 신청 워크플로우":
        workflow_page()
    elif menu == "⚙️ 관리자":
        admin_page()

def dashboard_page():
    st.title("🏆 메인비즈·이노비즈 AI 마스터 컨설턴트")
    st.caption("컨설턴트 내부용 통합 관리 시스템")

    companies_db = gist_load(_companies_filename(), get_default_companies_db)
    companies = companies_db.get("companies", {})

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("등록 고객사", len(companies))

    mainbiz_count = sum(1 for c in companies.values()
                        if "메인비즈" in c.get("target_certs", []))
    innobiz_count = sum(1 for c in companies.values()
                        if "이노비즈" in c.get("target_certs", []))
    col2.metric("메인비즈 진행", mainbiz_count)
    col3.metric("이노비즈 진행", innobiz_count)

    # 평균 점수
    all_scores = []
    for c in companies.values():
        for cert_data in c.get("assessments", {}).values():
            if cert_data.get("total"):
                all_scores.append(cert_data["total"])
    avg = sum(all_scores) / len(all_scores) if all_scores else 0
    col4.metric("평균 진단 점수", f"{avg:.0f}점")

    st.divider()

    st.subheader("📌 빠른 안내")
    col_a, col_b = st.columns(2)
    with col_a:
        st.info("""
        **메인비즈 (경영혁신형)**
        - 자가진단: 600점 / 현장평가: 700점
        - 4개 분야: 전략·성과·조직·ESG
        - 평가기관: 신보/기보/KPC
        - 유효기간: 3년
        """)
    with col_b:
        st.info("""
        **이노비즈 (기술혁신형)**
        - 자가진단: 650점 / 현장평가: 700점
        - 4개 분야: 기술혁신·사업화·경영·성과
        - 추가요건: 기술등급 B 이상
        - 평가기관: 기술보증기금
        - 수수료: 신규 77만원
        """)

    # 최근 진단
    st.subheader("📋 최근 진단 이력")
    recent = []
    for name, c in companies.items():
        for cert, data in c.get("assessments", {}).items():
            recent.append({
                "company": name, "cert": cert,
                "total": data.get("total", 0),
                "date": data.get("evaluated_at", "")[:10]
            })
    recent.sort(key=lambda x: x["date"], reverse=True)

    if recent:
        for r in recent[:5]:
            st.write(f"- **{r['date']}** | {r['company']} | {r['cert']}: {r['total']}점")
    else:
        st.caption("아직 진단 기록이 없습니다.")

if __name__ == "__main__":
    main()
