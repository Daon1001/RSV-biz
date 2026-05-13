"""
RSV 디자인 시스템
- 다크 네이비 + 골드 럭셔리 스타일
- Streamlit CSS 주입
- 컨설팅 보고서 HTML 생성
- 가이드북 콘텐츠
"""
from datetime import datetime
from typing import Dict, List

# =====================================================================
# 🎨 컬러 팔레트 (RSV 톤)
# =====================================================================
RSV_COLORS = {
    "navy_dark": "#0A1628",
    "navy": "#0b1f52",
    "navy_mid": "#1a3a7a",
    "navy_light": "#2a5298",
    "gold": "#d4af37",
    "gold_light": "#F4D98A",
    "gold_dark": "#8B6F3E",
    "bg_paper": "#E8E0E0",
    "text_dark": "#1A1A1A",
    "text_muted": "#666666",
    "success": "#2D8659",
    "warning": "#C9A961",
    "danger": "#B85450",
}

# =====================================================================
# 🎨 Streamlit 화면용 CSS (사이드바·헤더·카드 등)
# =====================================================================
STREAMLIT_CSS = """
<style>
/* ── 폰트 ── */
@import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css');

/* ── 전역 ── */
.block-container {
    padding-top: 1.5rem !important;
    padding-bottom: 2rem !important;
    max-width: 1280px !important;
}

.stApp {
    background: linear-gradient(180deg, #f5f7fb 0%, #eef2f7 100%) !important;
    font-family: 'Pretendard Variable', Pretendard, 'Noto Sans KR', -apple-system, sans-serif !important;
}

/* ── 사이드바 (네이비 + 골드) ── */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0A1628 0%, #0b1f52 60%, #1a3a7a 100%) !important;
}
section[data-testid="stSidebar"] > div {
    color: white !important;
}
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] .stMarkdown {
    color: white !important;
}
section[data-testid="stSidebar"] .stRadio label {
    color: white !important;
    font-weight: 500;
}
section[data-testid="stSidebar"] .stButton > button {
    background: rgba(212, 175, 55, 0.15) !important;
    border: 1px solid rgba(212, 175, 55, 0.4) !important;
    color: #d4af37 !important;
    font-weight: 600 !important;
    border-radius: 10px !important;
}
section[data-testid="stSidebar"] .stButton > button:hover {
    background: rgba(212, 175, 55, 0.3) !important;
    border-color: #d4af37 !important;
}
section[data-testid="stSidebar"] .stSuccess {
    background: rgba(212, 175, 55, 0.1) !important;
    border: 1px solid rgba(212, 175, 55, 0.3) !important;
    border-radius: 8px;
}

/* ── 메인 헤더 (그라데이션 박스) ── */
.rsv-hero {
    background: linear-gradient(135deg, #0A1628 0%, #0b1f52 50%, #1a3a7a 100%);
    border-radius: 16px;
    padding: 32px 40px;
    margin-bottom: 28px;
    border-bottom: 4px solid #d4af37;
    box-shadow: 0 8px 24px rgba(11, 31, 82, 0.18);
    position: relative;
    overflow: hidden;
}
.rsv-hero::before {
    content: "";
    position: absolute;
    top: -50%;
    right: -10%;
    width: 300px;
    height: 200%;
    background: radial-gradient(ellipse, rgba(212, 175, 55, 0.15) 0%, transparent 70%);
    pointer-events: none;
}
.rsv-hero h1 {
    color: white !important;
    font-size: 28px;
    font-weight: 800;
    margin: 0 !important;
    letter-spacing: -0.5px;
}
.rsv-hero p {
    color: rgba(255, 255, 255, 0.75) !important;
    font-size: 14px;
    margin: 8px 0 0 !important;
}
.rsv-hero .gold {
    color: #d4af37 !important;
    font-weight: 700;
}

/* ── 섹션 헤더 ── */
.rsv-section-title {
    background: white;
    border-left: 4px solid #d4af37;
    border-radius: 8px;
    padding: 14px 20px;
    margin: 24px 0 16px;
    font-size: 18px;
    font-weight: 700;
    color: #0b1f52;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
}

/* ── 카드 ── */
.rsv-card {
    background: white;
    border-radius: 12px;
    padding: 20px 24px;
    margin-bottom: 16px;
    border: 1px solid #e5e9f0;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
}

/* ── 메트릭 카드 강조 ── */
[data-testid="stMetric"] {
    background: white;
    padding: 16px 20px;
    border-radius: 12px;
    border: 1px solid #e5e9f0;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.03);
    border-left: 3px solid #d4af37;
}
[data-testid="stMetricLabel"] {
    color: #666 !important;
    font-size: 13px !important;
    font-weight: 500 !important;
}
[data-testid="stMetricValue"] {
    color: #0b1f52 !important;
    font-weight: 800 !important;
}

/* ── 버튼 ── */
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #0b1f52 0%, #1a3a7a 100%) !important;
    border: none !important;
    color: white !important;
    font-weight: 600 !important;
    border-radius: 10px !important;
    padding: 10px 24px !important;
    box-shadow: 0 4px 12px rgba(11, 31, 82, 0.25) !important;
}
.stButton > button[kind="primary"]:hover {
    background: linear-gradient(135deg, #0A1628 0%, #0b1f52 100%) !important;
    box-shadow: 0 6px 16px rgba(11, 31, 82, 0.35) !important;
}
.stDownloadButton > button {
    background: linear-gradient(135deg, #d4af37 0%, #c9a961 100%) !important;
    border: none !important;
    color: white !important;
    font-weight: 700 !important;
    border-radius: 10px !important;
    padding: 12px 28px !important;
    box-shadow: 0 4px 12px rgba(212, 175, 55, 0.35) !important;
}
.stDownloadButton > button:hover {
    background: linear-gradient(135deg, #c9a961 0%, #b8941f 100%) !important;
    transform: translateY(-1px);
}

/* ── 탭 ── */
.stTabs [data-baseweb="tab-list"] {
    gap: 4px;
    background: white;
    padding: 6px;
    border-radius: 10px;
    border: 1px solid #e5e9f0;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 8px;
    padding: 8px 16px;
    font-weight: 600;
    color: #666;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #0b1f52 0%, #1a3a7a 100%) !important;
    color: white !important;
}

/* ── 프로그레스바 골드 ── */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #d4af37 0%, #f4d98a 100%) !important;
}

/* ── Expander ── */
.streamlit-expanderHeader {
    background: #f8fafc !important;
    border: 1px solid #e5e9f0 !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
    color: #0b1f52 !important;
}

/* ── 알림박스 ── */
.stAlert {
    border-radius: 10px !important;
    border-left-width: 4px !important;
}

/* ── 로그인 화면 카드 ── */
.rsv-login-card {
    max-width: 480px;
    margin: 40px auto;
    background: white;
    border-radius: 20px;
    padding: 40px;
    box-shadow: 0 20px 50px rgba(11, 31, 82, 0.15);
    border-top: 6px solid #d4af37;
}
.rsv-login-card h1 {
    color: #0b1f52;
    font-size: 28px;
    margin-bottom: 8px;
    text-align: center;
}
.rsv-login-card .subtitle {
    color: #666;
    font-size: 14px;
    text-align: center;
    margin-bottom: 24px;
}
</style>
"""

def inject_css(st):
    """Streamlit에 RSV CSS 주입"""
    st.markdown(STREAMLIT_CSS, unsafe_allow_html=True)


def render_hero(st, title: str, subtitle: str = ""):
    """RSV 스타일 메인 헤더 렌더링"""
    st.markdown(f"""
    <div class="rsv-hero">
        <h1>{title}</h1>
        {f'<p>{subtitle}</p>' if subtitle else ''}
    </div>
    """, unsafe_allow_html=True)


def render_section(st, title: str):
    """섹션 헤더 렌더링"""
    st.markdown(f'<div class="rsv-section-title">{title}</div>',
                unsafe_allow_html=True)


# =====================================================================
# 📄 컨설팅 보고서 HTML 생성 (A4 출력 가능)
# =====================================================================

REPORT_CSS = """
@import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css');

@page { size: A4 portrait; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }

body {
    font-family: 'Pretendard Variable', Pretendard, 'Noto Sans KR', sans-serif;
    font-size: 13px;
    color: #1A1A1A;
    line-height: 1.7;
    background: #E8E0E0;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px 0;
    letter-spacing: -0.2px;
}

.page {
    width: 210mm;
    min-height: 297mm;
    background: white;
    margin-bottom: 15px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    position: relative;
    overflow: hidden;
    page-break-after: always;
    padding: 25mm 20mm;
}

@media print {
    body { background: white !important; padding: 0 !important; }
    .page { box-shadow: none; margin-bottom: 0; }
    .cover {
        background: linear-gradient(135deg, #0A1628 0%, #0b1f52 50%, #1a3a7a 100%) !important;
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
    }
}

/* ── 표지 페이지 ── */
.cover {
    background: linear-gradient(135deg, #0A1628 0%, #0b1f52 50%, #1a3a7a 100%);
    color: white;
    padding: 0 !important;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    position: relative;
}
.cover::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 8px;
    background: linear-gradient(90deg, #d4af37 0%, #f4d98a 50%, #d4af37 100%);
}
.cover::after {
    content: "";
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 8px;
    background: linear-gradient(90deg, #d4af37 0%, #f4d98a 50%, #d4af37 100%);
}
.cover-badge {
    display: inline-block;
    background: rgba(212, 175, 55, 0.2);
    border: 1.5px solid #d4af37;
    color: #d4af37;
    padding: 6px 18px;
    border-radius: 30px;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
    margin-bottom: 24px;
}
.cover-title {
    font-size: 38px;
    font-weight: 900;
    color: white;
    margin-bottom: 12px;
    letter-spacing: -1px;
}
.cover-subtitle {
    font-size: 18px;
    color: rgba(255, 255, 255, 0.75);
    margin-bottom: 60px;
    font-weight: 300;
}
.cover-company {
    font-size: 28px;
    color: #d4af37;
    font-weight: 700;
    margin-bottom: 8px;
}
.cover-meta {
    color: rgba(255, 255, 255, 0.6);
    font-size: 14px;
    margin-bottom: 4px;
}
.cover-deco {
    width: 60px;
    height: 3px;
    background: #d4af37;
    margin: 24px auto;
}
.cover-footer {
    position: absolute;
    bottom: 50px;
    color: rgba(255, 255, 255, 0.5);
    font-size: 12px;
    letter-spacing: 1px;
}

/* ── 섹션 헤더 ── */
.section-header {
    display: flex;
    align-items: center;
    margin-bottom: 24px;
    padding-bottom: 14px;
    border-bottom: 2px solid #0b1f52;
}
.section-no {
    background: linear-gradient(135deg, #0b1f52 0%, #1a3a7a 100%);
    color: #d4af37;
    width: 44px;
    height: 44px;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    font-weight: 800;
    margin-right: 14px;
}
.section-title {
    font-size: 22px;
    font-weight: 800;
    color: #0b1f52;
}
.section-subtitle {
    font-size: 12px;
    color: #666;
    margin-top: 2px;
}

/* ── 페이지 헤더 (작은 라벨) ── */
.page-label {
    display: inline-block;
    background: #0b1f52;
    color: #d4af37;
    padding: 4px 14px;
    border-radius: 30px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.5px;
    margin-bottom: 16px;
}

/* ── 요약 박스 (V자) ── */
.summary-box {
    background: linear-gradient(135deg, #f8fafc 0%, #f0f4fa 100%);
    border-left: 4px solid #d4af37;
    padding: 20px 24px;
    border-radius: 8px;
    margin: 16px 0;
    font-size: 14px;
    line-height: 1.8;
    color: #1a1a1a;
}
.summary-box strong { color: #0b1f52; font-weight: 700; }

/* ── 메트릭 그리드 ── */
.metric-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
    margin: 20px 0;
}
.metric-card {
    background: white;
    border: 1px solid #e5e9f0;
    border-top: 3px solid #d4af37;
    border-radius: 10px;
    padding: 14px 16px;
    text-align: center;
}
.metric-card.pass { border-top-color: #2D8659; }
.metric-card.warn { border-top-color: #C9A961; }
.metric-card.fail { border-top-color: #B85450; }
.metric-label {
    color: #666;
    font-size: 11px;
    margin-bottom: 6px;
    letter-spacing: 0.5px;
}
.metric-value {
    color: #0b1f52;
    font-size: 24px;
    font-weight: 800;
}
.metric-value.gold { color: #d4af37; }
.metric-value.pass { color: #2D8659; }
.metric-value.fail { color: #B85450; }
.metric-sub {
    font-size: 11px;
    color: #999;
    margin-top: 4px;
}

/* ── 점수 분포 테이블 ── */
.score-table {
    width: 100%;
    border-collapse: collapse;
    margin: 16px 0;
    font-size: 13px;
}
.score-table th {
    background: #0b1f52;
    color: #d4af37;
    padding: 10px 14px;
    text-align: left;
    font-weight: 700;
    letter-spacing: 0.5px;
}
.score-table td {
    padding: 10px 14px;
    border-bottom: 1px solid #e5e9f0;
}
.score-table tr:hover { background: #f8fafc; }
.score-bar {
    height: 8px;
    background: #e5e9f0;
    border-radius: 4px;
    overflow: hidden;
    width: 120px;
    display: inline-block;
}
.score-bar-fill {
    height: 100%;
    background: linear-gradient(90deg, #d4af37 0%, #f4d98a 100%);
    border-radius: 4px;
}

/* ── 강점/약점 박스 ── */
.swot {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin: 16px 0;
}
.swot-box {
    padding: 16px 20px;
    border-radius: 10px;
    font-size: 13px;
}
.swot-strength {
    background: linear-gradient(135deg, #f0f9f4 0%, #e8f5ec 100%);
    border-left: 4px solid #2D8659;
}
.swot-weakness {
    background: linear-gradient(135deg, #fdf2f0 0%, #faeae6 100%);
    border-left: 4px solid #B85450;
}
.swot-box h4 {
    font-size: 14px;
    font-weight: 800;
    margin-bottom: 10px;
}
.swot-strength h4 { color: #2D8659; }
.swot-weakness h4 { color: #B85450; }
.swot-box ul { padding-left: 18px; }
.swot-box li { margin-bottom: 6px; line-height: 1.6; }

/* ── 액션 카드 ── */
.action-card {
    background: white;
    border: 1px solid #e5e9f0;
    border-radius: 12px;
    padding: 16px 20px;
    margin-bottom: 12px;
    position: relative;
    padding-left: 60px;
}
.action-card::before {
    content: attr(data-no);
    position: absolute;
    left: 14px;
    top: 16px;
    background: linear-gradient(135deg, #d4af37 0%, #c9a961 100%);
    color: white;
    width: 32px;
    height: 32px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
    font-size: 14px;
}
.action-card h4 {
    color: #0b1f52;
    font-size: 15px;
    font-weight: 700;
    margin-bottom: 8px;
}
.action-card .action-meta {
    display: flex;
    gap: 12px;
    margin-top: 8px;
    flex-wrap: wrap;
}
.action-tag {
    background: #f0f4fa;
    color: #0b1f52;
    padding: 3px 10px;
    border-radius: 20px;
    font-size: 11px;
    font-weight: 600;
}

/* ── 증빙자료 체크리스트 ── */
.evidence-list {
    background: #fafbfd;
    border: 1px solid #e5e9f0;
    border-radius: 10px;
    padding: 16px 20px;
    margin: 14px 0;
}
.evidence-list h4 {
    color: #0b1f52;
    font-size: 14px;
    font-weight: 700;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
}
.evidence-list h4::before {
    content: "📎";
    margin-right: 6px;
}
.evidence-list li {
    list-style: none;
    padding: 4px 0 4px 24px;
    position: relative;
    font-size: 12.5px;
}
.evidence-list li::before {
    content: "□";
    position: absolute;
    left: 0;
    color: #d4af37;
    font-weight: 700;
}

/* ── 안내 박스 ── */
.notice {
    background: linear-gradient(135deg, #fff9e6 0%, #fef3d6 100%);
    border-left: 4px solid #d4af37;
    padding: 14px 18px;
    border-radius: 8px;
    margin: 14px 0;
    font-size: 12.5px;
}

/* ── 푸터 ── */
.page-footer {
    position: absolute;
    bottom: 15mm;
    left: 20mm;
    right: 20mm;
    border-top: 1px solid #e5e9f0;
    padding-top: 10px;
    display: flex;
    justify-content: space-between;
    font-size: 10px;
    color: #999;
}
"""


def _grade_pct(score: int, max_score: int) -> str:
    """점수 비율에 따른 색상 클래스"""
    pct = score / max_score * 100 if max_score else 0
    if pct >= 80:
        return "pass"
    elif pct >= 60:
        return ""
    elif pct >= 40:
        return "warn"
    else:
        return "fail"


def generate_consulting_report(
    cert_type: str,        # "메인비즈" or "이노비즈"
    company_name: str,
    industry_name: str,
    total_score: int,
    self_pass: int,
    field_pass: int,
    category_scores: dict,  # {cat_id: {"name": str, "score": int, "max": int}}
    top_gaps: list,         # [{"category", "name", "current", "max", "gap"}, ...]
    ai_report_md: str = "",
    tech_grade: dict = None,  # {"grade": str, "passed": bool} (이노비즈 전용)
    evidences_per_category: dict = None,  # {cat_name: [evidence_str, ...]}
) -> str:
    """RSV 디자인 기반 컨설팅 보고서 HTML 생성"""

    today = datetime.now().strftime("%Y년 %m월 %d일")

    # 상태 판정
    if total_score >= field_pass:
        status_text = "현장평가 통과 가능"
        status_class = "pass"
    elif total_score >= self_pass:
        status_text = "자가진단 통과 / 현장평가 미달"
        status_class = "warn"
    else:
        status_text = "자가진단 미달 (신청 불가)"
        status_class = "fail"

    # 분야별 점수 테이블
    score_rows = ""
    for cid, cat in category_scores.items():
        pct = cat["score"] / cat["max"] * 100
        grade_cls = _grade_pct(cat["score"], cat["max"])
        score_rows += f"""
        <tr>
            <td><strong>{cat['name']}</strong></td>
            <td style="text-align:center"><strong>{cat['score']}</strong> / {cat['max']}</td>
            <td style="text-align:center" class="metric-value {grade_cls}" style="font-size:14px">{pct:.1f}%</td>
            <td>
                <div class="score-bar">
                    <div class="score-bar-fill" style="width: {pct}%"></div>
                </div>
            </td>
        </tr>
        """

    # 강점 / 약점
    strengths = [c for c in category_scores.values() if c["score"] / c["max"] >= 0.7]
    weaknesses = [c for c in category_scores.values() if c["score"] / c["max"] < 0.6]

    strength_html = "".join([
        f"<li><strong>{c['name']}</strong>: {c['score']}/{c['max']}점 ({c['score']/c['max']*100:.0f}%)</li>"
        for c in strengths
    ]) or "<li>모든 분야에서 추가 보완이 필요합니다.</li>"

    weakness_html = "".join([
        f"<li><strong>{c['name']}</strong>: {c['score']}/{c['max']}점 ({c['score']/c['max']*100:.0f}%)</li>"
        for c in weaknesses
    ]) or "<li>현재 점수 분포가 안정적입니다.</li>"

    # 우선 개선 과제 카드
    action_cards = ""
    for i, gap in enumerate(top_gaps[:5], 1):
        action_cards += f"""
        <div class="action-card" data-no="{i}">
            <h4>[{gap['category']}] {gap['name']}</h4>
            <p style="color:#666; font-size:12.5px; line-height:1.6;">
                현재 <strong style="color:#B85450">{gap['current']}점</strong>에서
                최대 <strong style="color:#2D8659">{gap['max']}점</strong>까지 향상 가능
                <span style="color:#d4af37; font-weight:700">(+{gap['gap']}점)</span>
            </p>
            <div class="action-meta">
                <span class="action-tag">우선순위 {i}</span>
                <span class="action-tag">예상 효과 +{gap['gap']}점</span>
            </div>
        </div>
        """

    # 증빙자료
    evidence_html = ""
    if evidences_per_category:
        for cat_name, evs in evidences_per_category.items():
            ev_items = "".join([f"<li>{e}</li>" for e in evs])
            evidence_html += f"""
            <div class="evidence-list">
                <h4>{cat_name} 증빙자료</h4>
                <ul style="padding-left:0">{ev_items}</ul>
            </div>
            """

    # 기술등급 정보 (이노비즈만)
    tech_grade_html = ""
    if cert_type == "이노비즈" and tech_grade:
        tg_cls = "pass" if tech_grade.get("passed") else "fail"
        tg_status = "✓ B 이상 통과" if tech_grade.get("passed") else "✗ B 미달"
        tech_grade_html = f"""
        <div class="metric-card {tg_cls}">
            <div class="metric-label">개별기술등급</div>
            <div class="metric-value {tg_cls}">{tech_grade.get('grade', '미평가')}</div>
            <div class="metric-sub">{tg_status}</div>
        </div>
        """

    # AI 리포트 마크다운 -> HTML 변환 (간단 처리)
    ai_html = ai_report_md.replace("## ", "<h3>").replace("\n## ", "\n<h3>") if ai_report_md else ""
    ai_html = ai_html.replace("\n# ", "\n<h2>").replace("\n", "<br>")

    cert_color = "#0b1f52" if cert_type == "메인비즈" else "#1a3a7a"

    html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>{company_name} {cert_type} 컨설팅 보고서</title>
<style>{REPORT_CSS}</style>
</head>
<body>

<!-- ============ Page 1: 표지 ============ -->
<div class="page cover">
    <div class="cover-badge">CONSULTING REPORT</div>
    <div class="cover-title">{cert_type} 인증 컨설팅 보고서</div>
    <div class="cover-subtitle">{'경영혁신형 중소기업 (Main-Biz)' if cert_type == '메인비즈' else '기술혁신형 중소기업 (Inno-Biz)'}</div>
    <div class="cover-deco"></div>
    <div class="cover-company">{company_name}</div>
    <div class="cover-meta">업종 · {industry_name}</div>
    <div class="cover-meta">평가일자 · {today}</div>
    <div class="cover-footer">PREPARED BY RSV CONSULTING</div>
</div>

<!-- ============ Page 2: 요약 ============ -->
<div class="page">
    <div class="page-label">EXECUTIVE SUMMARY</div>
    <div class="section-header">
        <div class="section-no">01</div>
        <div>
            <div class="section-title">진단 요약</div>
            <div class="section-subtitle">{cert_type} 자가진단 결과 종합</div>
        </div>
    </div>

    <div class="summary-box">
        <strong>{company_name}</strong>의 {cert_type} 자가진단 결과,
        총 <strong style="color:#d4af37">{total_score}점 / 1,000점</strong>으로
        <strong>{status_text}</strong> 상태로 평가되었습니다.
        {('현재 점수에서 ' + str(field_pass - total_score) + '점 추가 확보 시 현장평가 통과가 가능합니다.') if total_score < field_pass else '현장평가 신청을 진행하실 수 있습니다.'}
    </div>

    <div class="metric-grid">
        <div class="metric-card">
            <div class="metric-label">총 점수</div>
            <div class="metric-value gold">{total_score}</div>
            <div class="metric-sub">/ 1,000점</div>
        </div>
        <div class="metric-card {'pass' if total_score >= self_pass else 'fail'}">
            <div class="metric-label">자가진단 ({self_pass}점)</div>
            <div class="metric-value {'pass' if total_score >= self_pass else 'fail'}">
                {'✓' if total_score >= self_pass else '✗'} {abs(total_score - self_pass):+d}
            </div>
            <div class="metric-sub">{'통과' if total_score >= self_pass else '미달'}</div>
        </div>
        <div class="metric-card {'pass' if total_score >= field_pass else 'fail'}">
            <div class="metric-label">현장평가 ({field_pass}점)</div>
            <div class="metric-value {'pass' if total_score >= field_pass else 'fail'}">
                {'✓' if total_score >= field_pass else '✗'} {abs(total_score - field_pass):+d}
            </div>
            <div class="metric-sub">{'통과' if total_score >= field_pass else '미달'}</div>
        </div>
        {tech_grade_html if tech_grade_html else f'''
        <div class="metric-card">
            <div class="metric-label">달성률</div>
            <div class="metric-value">{total_score/10:.1f}%</div>
            <div class="metric-sub">전체 대비</div>
        </div>
        '''}
    </div>

    <div class="section-header" style="margin-top:30px">
        <div class="section-no">02</div>
        <div>
            <div class="section-title">분야별 점수 분포</div>
            <div class="section-subtitle">4개 핵심 분야 평가 결과</div>
        </div>
    </div>

    <table class="score-table">
        <thead>
            <tr>
                <th>평가 분야</th>
                <th style="text-align:center; width:120px">점수</th>
                <th style="text-align:center; width:100px">달성률</th>
                <th style="width:140px">분포</th>
            </tr>
        </thead>
        <tbody>
            {score_rows}
        </tbody>
    </table>

    <div class="page-footer">
        <span>{company_name} · {cert_type} 컨설팅 보고서</span>
        <span>Page 02</span>
    </div>
</div>

<!-- ============ Page 3: 강점/약점 ============ -->
<div class="page">
    <div class="page-label">SWOT ANALYSIS</div>
    <div class="section-header">
        <div class="section-no">03</div>
        <div>
            <div class="section-title">강점 & 보완 분야</div>
            <div class="section-subtitle">분야별 진단 결과 기반 분석</div>
        </div>
    </div>

    <div class="swot">
        <div class="swot-box swot-strength">
            <h4>💪 강점 분야 (70% 이상)</h4>
            <ul>{strength_html}</ul>
            <p style="margin-top:12px; font-size:11.5px; color:#2D8659;">
                현장평가 시 적극 어필하여 가산점 확보 가능
            </p>
        </div>
        <div class="swot-box swot-weakness">
            <h4>⚠️ 보완 필요 분야 (60% 미만)</h4>
            <ul>{weakness_html}</ul>
            <p style="margin-top:12px; font-size:11.5px; color:#B85450;">
                우선 개선 과제로 선정하여 단기 집중 보완 필요
            </p>
        </div>
    </div>

    <div class="section-header" style="margin-top:30px">
        <div class="section-no">04</div>
        <div>
            <div class="section-title">우선 개선 과제 TOP 5</div>
            <div class="section-subtitle">점수 향상 효과가 가장 큰 항목</div>
        </div>
    </div>

    {action_cards}

    <div class="page-footer">
        <span>{company_name} · {cert_type} 컨설팅 보고서</span>
        <span>Page 03</span>
    </div>
</div>

<!-- ============ Page 4: 증빙자료 가이드 ============ -->
<div class="page">
    <div class="page-label">EVIDENCE CHECKLIST</div>
    <div class="section-header">
        <div class="section-no">05</div>
        <div>
            <div class="section-title">현장평가 증빙자료 준비</div>
            <div class="section-subtitle">분야별 필수 증빙자료 체크리스트</div>
        </div>
    </div>

    <div class="notice">
        <strong>💡 안내</strong><br>
        현장평가 시 자가진단 입력 내용에 대한 객관적 증빙이 필요합니다.
        아래 체크리스트를 활용하여 사전에 준비하시기 바랍니다.
    </div>

    {evidence_html if evidence_html else '<p style="color:#666; padding:20px;">증빙자료 정보가 없습니다.</p>'}

    <div class="page-footer">
        <span>{company_name} · {cert_type} 컨설팅 보고서</span>
        <span>Page 04</span>
    </div>
</div>

{f'''
<!-- ============ Page 5: AI 상세 분석 ============ -->
<div class="page">
    <div class="page-label">AI EXPERT ANALYSIS</div>
    <div class="section-header">
        <div class="section-no">06</div>
        <div>
            <div class="section-title">AI 전문가 상세 분석</div>
            <div class="section-subtitle">Claude AI 기반 맞춤 컨설팅</div>
        </div>
    </div>

    <div style="font-size:13px; line-height:1.8; color:#1a1a1a;">
        {ai_html}
    </div>

    <div class="page-footer">
        <span>{company_name} · {cert_type} 컨설팅 보고서</span>
        <span>Page 05</span>
    </div>
</div>
''' if ai_report_md else ''}

<!-- ============ 마지막: 안내 ============ -->
<div class="page">
    <div class="page-label">DISCLAIMER & CONTACT</div>
    <div class="section-header">
        <div class="section-no">99</div>
        <div>
            <div class="section-title">유의사항 및 안내</div>
            <div class="section-subtitle">본 보고서 활용 시 주의사항</div>
        </div>
    </div>

    <div class="notice" style="background: linear-gradient(135deg, #fdf2f0 0%, #faeae6 100%); border-left-color: #B85450;">
        <strong>⚠️ 면책 조항</strong><br>
        본 보고서는 입력하신 답변을 기반으로 한 <strong>참고용 시뮬레이션</strong>입니다.
        실제 {cert_type} 현장평가는 평가기관({'신용보증기금 / 기술보증기금 / 한국생산성본부' if cert_type == '메인비즈' else '기술보증기금'})의
        전문 평가자가 별도 기준으로 진행하며, 결과가 본 보고서와 다를 수 있습니다.
        최종 자가진단 및 신청은 공식 사이트({'https://www.smes.go.kr/mainbiz' if cert_type == '메인비즈' else 'https://www.innobiz.net'})에서 진행해 주세요.
    </div>

    <div class="summary-box" style="margin-top:30px">
        <strong>📌 다음 단계</strong><br><br>
        <strong>1. 우선 개선 과제 실행</strong> — 본 보고서의 TOP 5 개선 과제를 우선 보완<br>
        <strong>2. 증빙자료 준비</strong> — 체크리스트에 따라 분야별 증빙 수집<br>
        <strong>3. 공식 자가진단</strong> — 점수 충족 시 공식 사이트에서 자가진단 실시<br>
        <strong>4. 평가기관 신청</strong> — 자가진단 통과 시 현장평가 신청<br>
        <strong>5. 현장평가 대응</strong> — 평가자 방문 시 강점 분야 적극 어필
    </div>

    <div style="margin-top:60px; text-align:center; color:#999; font-size:11px;">
        본 보고서는 {today} 기준으로 작성되었습니다.<br>
        © RSV CONSULTING · 메인비즈·이노비즈 AI 마스터 컨설턴트
    </div>

    <div class="page-footer">
        <span>{company_name} · {cert_type} 컨설팅 보고서</span>
        <span>End of Report</span>
    </div>
</div>

</body>
</html>"""

    return html


# =====================================================================
# 📖 가이드북 콘텐츠
# =====================================================================

GUIDEBOOK = {
    "메인비즈": {
        "title": "메인비즈 (경영혁신형 중소기업) 가이드북",
        "subtitle": "Management Innovation Business",
        "overview": """**메인비즈**는 「중소기업 기술혁신 촉진법」 제15조의3에 따라
중소벤처기업부장관이 선정한 **경영혁신형 중소기업**입니다.

특별한 기술이 없는 기업이라도 **서비스, 마케팅, 공정, 인사조직** 등
경영 전반의 혁신활동 및 역량을 평가받아 인증받을 수 있습니다.

OECD 오슬로 매뉴얼(Oslo Manual)에 기반한 평가지표로,
잠재적인 경영혁신 역량을 보유한 기업을 발굴·육성합니다.""",
        "requirements": [
            "「중소기업기본법」 제2조에 따른 중소기업",
            "업력 3년 이상",
            "결격사유 없음 (체납·회생절차·부채비율 1,000% 이상 등 제외)",
            "게임·도박·사행성·불건전 업종 제외"
        ],
        "process": [
            ("1. 메인비즈넷 가입", "smes.go.kr/mainbiz 회원가입 및 기업등록"),
            ("2. 재무정보 입력", "국세청 신고 재무제표 기준"),
            ("3. 온라인 자가진단", "1,000점 만점 / 600점 이상 통과"),
            ("4. 평가기관 선택", "신보 / 기보 / KPC 중 선택"),
            ("5. 현장평가 신청", "수수료 납부 (신규 55만원)"),
            ("6. 현장평가", "1,000점 만점 / 700점 이상 통과"),
            ("7. 확인서 발급", "지방중기청 통해 우편 발송 (유효기간 3년)")
        ],
        "evaluation": {
            "전략기획 및 이행관리": "비전·미션, 중장기 전략, 사업계획, 실행 모니터링",
            "성과관리": "KPI 설정, 성과 측정, 재무성과, 비재무성과",
            "조직 및 인력관리": "조직구조, 인사평가·보상, 교육훈련, 조직문화",
            "사회 신뢰 활동 (ESG)": "환경경영, 사회적 책임, 지배구조, 이해관계자"
        },
        "benefits": {
            "🏦 금융 지원": [
                "중소벤처기업진흥공단 정책자금 우대",
                "신용보증기금·기술보증기금 보증료 0.1~0.2%p 감면",
                "각종 협약은행 대출 금리 우대"
            ],
            "💰 세제 지원": [
                "정기 세무조사 유예 (수도권 2년 / 지방 3년)",
                "중소기업 특별세액감면 적용",
                "연구개발비 세액공제 우대"
            ],
            "🏛️ 정부 사업 가점": [
                "중소벤처기업부 R&D 사업 신청 시 가점",
                "조달청 물품구매 적격심사 신인도 가점",
                "병무청 병역지정업체 심사 시 가점"
            ],
            "📜 기타 혜택": [
                "특허 출원 시 우선심사 대상",
                "코스닥 상장요건 일부 완화",
                "메인비즈 마크 사용권 (마케팅 활용)"
            ]
        },
        "tips": [
            "**전략 문서 사전 준비**: 비전·미션, 중장기 경영전략, 연간 사업계획서를 문서화하여 준비",
            "**ESG 활동 기록**: 사회공헌, 환경경영, 윤리경영 활동을 정기적으로 기록",
            "**인사평가 체계화**: 정기 인사평가 + 성과급 지급 기준 문서화",
            "**고객만족도 측정**: 정기 조사 + 결과 기반 개선 활동 기록",
            "**ISO 인증 확보**: ISO 9001/14001 보유 시 가점 효과"
        ]
    },
    "이노비즈": {
        "title": "이노비즈 (기술혁신형 중소기업) 가이드북",
        "subtitle": "Innovation Business",
        "overview": """**이노비즈**는 「중소기업 기술혁신 촉진법」 제15조에 따라
중소벤처기업부장관이 선정한 **기술혁신형 중소기업**입니다.

기술혁신 활동을 통해 **기술경쟁력 확보** 또는
**미래 성장가능성**이 있는 중소기업을 발굴·육성합니다.

메인비즈와 달리 **기술·R&D 중심** 평가이며,
시스템 평가(1,000점)와 **개별기술수준 평가(14등급)**를 동시에 통과해야 합니다.""",
        "requirements": [
            "「중소기업기본법」 제2조에 따른 중소기업",
            "업력 3년 이상",
            "해당 업종: 제조업·건설업·농업·비제조업·소프트웨어업·바이오업·환경업·전문디자인업",
            "결격사유 없음"
        ],
        "process": [
            ("1. 이노비즈넷 가입", "innobiz.net 회원가입 및 기업등록"),
            ("2. 재무정보 + 기술사업계획서 입력", "최근 3개년 재무제표 + 기술 내용"),
            ("3. 온라인 자가진단", "1,000점 만점 / **650점 이상** 통과"),
            ("4. 신청 접수 및 수수료 납부", "신규 77만원 (부가세 포함)"),
            ("5. 기술보증기금 현장평가", "전문 평가자 방문"),
            ("6. 시스템 평가 + 개별기술 평가", "**700점 이상 + B등급 이상 동시 충족**"),
            ("7. 확인서 발급", "유효기간 3년 / 등급별 표기 (AAA~B)")
        ],
        "evaluation": {
            "기술혁신능력 (300점)": "R&D 조직, 연구전담인력, R&D 투자비율, 지식재산권",
            "기술사업화능력 (250점)": "기술 시장성, 사업화 계획, 신제품 매출, 사업화 인프라",
            "기술혁신경영능력 (250점)": "기술전략, 정보화 수준, 품질관리, 기술협력",
            "기술혁신성과 (200점)": "매출 증가율, 영업이익률, 고용 증가, 기술인증·수상"
        },
        "tech_grade": {
            "구성": "경영주 기술능력(200) + 기술성(300) + 시장성(250) + 사업성(250) = 1,000점",
            "등급": "AAA(950+) / AA(900+) / A+(850+) / A(800+) / BBB+(750+) / BBB(700+) / BB+(650+) / BB(600+) / B+(550+) / **B(500+ 최소통과)** / CCC / CC / C / D",
            "통과기준": "**B등급 이상** (500점 이상) 필수"
        },
        "benefits": {
            "🏦 금융 지원": [
                "기술보증기금 보증료 0.2%p 감면 + 보증한도 우대",
                "중소벤처기업진흥공단 정책자금 우대 금리",
                "협약은행 신용대출 신용등급 1단계 상향 (5점 가점)"
            ],
            "💰 세제 지원": [
                "정기 세무조사 유예 (수도권 2년 / 지방 3년)",
                "수도권 취득세 중과 면제",
                "연구개발비 세액공제 우대 (중소기업 25%)"
            ],
            "🔬 R&D 지원": [
                "기술혁신개발사업 가점 3점",
                "공정혁신 지원사업 가점",
                "생산정보화 지원사업 가점 5점",
                "쿠폰제 경영컨설팅 지원사업 가점 5점",
                "해외유명인증획득지원 가점 10점"
            ],
            "👥 인력 지원": [
                "산업기능요원·전문연구요원 심사 시 가점 5점",
                "이노비즈 인력양성 사업 우대"
            ],
            "📈 판로·기타": [
                "기술개발제품 우선구매 대상 포함",
                "조달청 적격심사 신인도 0.25점 가점",
                "특허 출원 우선심사 대상",
                "코스닥 상장요건 완화",
                "이노비즈펀드 투자 우선 검토"
            ]
        },
        "tips": [
            "**기업부설연구소 사전 설립**: 한국산업기술진흥협회(KOITA) 등록 시 큰 가점",
            "**R&D 투자비 3% 이상 확보**: 매출액 대비 R&D 비율은 핵심 지표",
            "**특허 출원 확대**: 등록 3건 이상 시 가점 효과 큼 (해외특허 보유 시 추가)",
            "**연구전담요원 3명 이상**: 학위 보유자(석사 이상) 포함 시 가점",
            "**기술로드맵(TRM) 작성**: 외부 컨설팅 검증을 거친 문서가 효과적",
            "**기술등급 B 이상 사전 점검**: 시스템 점수 700점만으로는 부족, 기술등급 별도 관리 필수"
        ]
    }
}


def render_guidebook_page(st, cert_type: str):
    """가이드북 페이지 렌더링"""
    book = GUIDEBOOK[cert_type]

    render_hero(st, f"📖 {book['title']}", book["subtitle"])

    # 개요
    render_section(st, "💡 제도 개요")
    st.markdown(book["overview"])

    # 신청 자격
    render_section(st, "✅ 신청 자격 요건")
    for req in book["requirements"]:
        st.markdown(f"- {req}")

    # 신청 절차
    render_section(st, "📋 신청 절차")
    for i, (stage, desc) in enumerate(book["process"], 1):
        with st.container():
            col1, col2 = st.columns([1, 4])
            with col1:
                st.markdown(f"### {stage}")
            with col2:
                st.markdown(f"{desc}")

    # 평가 항목
    render_section(st, "📊 평가 항목")
    for cat, desc in book["evaluation"].items():
        st.markdown(f"**{cat}**")
        st.caption(desc)

    # 이노비즈는 기술등급 추가 안내
    if cert_type == "이노비즈" and "tech_grade" in book:
        render_section(st, "🎓 개별기술수준 평가 (14등급)")
        tg = book["tech_grade"]
        st.markdown(f"**구성**: {tg['구성']}")
        st.markdown(f"**등급 체계**: {tg['등급']}")
        st.warning(f"**통과기준**: {tg['통과기준']}")

    # 혜택
    render_section(st, "🎁 인증 혜택")
    for category, benefits in book["benefits"].items():
        with st.expander(f"**{category}**", expanded=True):
            for b in benefits:
                st.markdown(f"- {b}")

    # 합격 팁
    render_section(st, "💎 합격 팁 (컨설턴트 노하우)")
    for tip in book["tips"]:
        st.markdown(f"- {tip}")

    st.divider()
    st.caption(f"📌 최신 정보는 공식 사이트에서 확인하세요: "
               f"{'https://www.smes.go.kr/mainbiz' if cert_type == '메인비즈' else 'https://www.innobiz.net'}")
