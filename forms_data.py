# -*- coding: utf-8 -*-
"""RSV 증빙서류 양식 원본 데이터 (33종). 자동 생성 파일 — 직접 수정 금지."""

FORM_CSS = r"""
@page { size: A4 portrait; margin: 14mm 13mm; }
* { box-sizing: border-box; margin:0; padding:0; }
body {
  font-family: "Pretendard","Malgun Gothic","맑은 고딕","Apple SD Gothic Neo",sans-serif;
  color:#1A1A1A; font-size:10pt; line-height:1.5; background:#8A8F98;
}
.page {
  width:210mm; min-height:297mm; padding:14mm 13mm; margin:0 auto 8mm;
  background:#fff; page-break-after:always; position:relative;
  display:flex; flex-direction:column;
}
.page:last-child { page-break-after:auto; }

/* ── 공통 헤더 ── */
.dochead { display:flex; justify-content:space-between; align-items:flex-end;
  border-bottom:2.2pt solid #0F1E3D; padding-bottom:3mm; margin-bottom:5mm; }
.dochead .co { font-size:10pt; font-weight:700; color:#0F1E3D; letter-spacing:.5px; }
.dochead .ttl { font-size:17pt; font-weight:800; color:#0F1E3D; letter-spacing:-.5px; margin-top:1mm; }
.dochead .meta { text-align:right; font-size:8pt; color:#5A6472; line-height:1.6; }
.dochead .meta b { color:#B8942E; font-weight:700; }

/* ── 표 ── */
table { width:100%; border-collapse:collapse; font-size:9.5pt; }
th, td { border:0.5pt solid #B4BCC7; padding:2.2mm 2mm; vertical-align:middle; }
th { background:#EDF0F4; color:#0F1E3D; font-weight:700; text-align:center; font-size:9pt; }
td.lb { background:#F6F8FA; font-weight:700; color:#0F1E3D; text-align:center; width:24mm; }
td.h { height:11mm; }
td.hh { height:16mm; }
td.hhh { height:26mm; }
.c { text-align:center; } .r { text-align:right; }
.guide { color:#9AA3AE; font-size:8pt; font-weight:400; }

/* ── 결재란 ── */
.sign { position:absolute; top:14mm; right:13mm; border-collapse:collapse; font-size:7.5pt; width:52mm; }
.sign th { background:#F6F8FA; padding:1mm; font-size:7.5pt; width:8mm; }
.sign td { height:13mm; }

/* ── 섹션 구분 ── */
.sec { background:#0F1E3D; color:#fff; font-size:10pt; font-weight:700;
  padding:2mm 3mm; margin:5mm 0 3mm; letter-spacing:.5px; }
.sec span { color:#B8942E; font-weight:400; font-size:8.5pt; margin-left:3mm; }
h3.sub { font-size:10pt; color:#0F1E3D; font-weight:700; margin:4mm 0 2mm;
  border-left:3pt solid #B8942E; padding-left:2.5mm; }

/* ── 푸터 ── */
.foot { margin-top:auto; padding-top:4mm; border-top:0.5pt solid #C9CFD8;
  display:flex; justify-content:space-between; font-size:7.5pt; color:#8A929C; }

/* ── 게시용 포스터 ── */
.poster { flex:1; display:flex; flex-direction:column; justify-content:center;
  text-align:center; padding:0 8mm; }
.poster .eyebrow { font-size:9pt; letter-spacing:6px; color:#B8942E; font-weight:700; }
.poster h1 { font-size:34pt; font-weight:800; color:#0F1E3D; margin:6mm 0; letter-spacing:-1.5px; }
.poster .lead { font-size:14pt; line-height:1.9; color:#22314A; font-weight:600; }
.poster .rule { width:40mm; height:2.5pt; background:#B8942E; margin:8mm auto; }
.poster .items { text-align:left; max-width:150mm; margin:0 auto; }
.poster .items li { font-size:12pt; line-height:2.1; list-style:none; padding-left:9mm; position:relative; }
.poster .items li::before { content:"—"; position:absolute; left:0; color:#B8942E; font-weight:800; }
.poster .sig { margin-top:14mm; font-size:11pt; color:#0F1E3D; line-height:2; }
.poster .sig b { font-size:13pt; letter-spacing:2px; }

/* ── 표지 ── */
.cover { background:#0F1E3D; color:#fff; }
.cover .in { flex:1; display:flex; flex-direction:column; justify-content:center; }
.cover .eyebrow { font-size:9pt; letter-spacing:8px; color:#B8942E; }
.cover h1 { font-size:40pt; font-weight:800; margin:8mm 0 4mm; letter-spacing:-2px; line-height:1.2; }
.cover .sub { font-size:13pt; color:#C3CBD6; line-height:2; }
.cover .box { border:1pt solid #B8942E; padding:6mm; margin-top:16mm; }
.cover .box p { font-size:10pt; color:#DCE2EA; line-height:1.9; }
.cover .box p b { color:#B8942E; }

/* ── 체크리스트 ── */
.chk td { font-size:8.5pt; padding:1.6mm 2mm; }
.chk .no { width:18mm; font-weight:700; color:#B8942E; text-align:center; font-size:8pt; }
.chk .q { width:14mm; text-align:center; color:#5A6472; font-size:8pt; }
.chk .box { width:12mm; text-align:center; font-size:11pt; color:#B4BCC7; }

.note { background:#F6F8FA; border-left:3pt solid #B8942E; padding:3mm 4mm;
  font-size:8.5pt; color:#3C4655; line-height:1.7; margin-top:4mm; }
.note b { color:#0F1E3D; }

@media print {
  body { background:#fff; }
  .page { margin:0; width:auto; min-height:auto; padding:0; box-shadow:none; }
}

/* ═══ 입력 · 인쇄 기능 ═══ */
[contenteditable]{ outline:none; }
td[contenteditable]{ background:#FCFDFE; cursor:text; }
td[contenteditable]:hover{ background:#F2F7FC; }
td[contenteditable]:focus{ background:#FFF9E6; box-shadow:inset 0 0 0 1.5pt #B8942E; }
td[contenteditable]:empty::before{ content:attr(data-ph); color:#C2C9D2; font-size:8pt; }
.ed{ display:inline-block; min-width:26mm; border-bottom:0.7pt dotted #B8942E;
     cursor:text; text-align:center; padding:0 1mm; }
.ed:empty::before{ content:attr(data-ph); color:#C2C9D2; font-weight:400; }
.ed:focus{ background:#FFF9E6; }
h1[contenteditable]:focus,.lead[contenteditable]:focus{ background:#FFF9E6; }

.pbtn{ position:absolute; top:6mm; right:13mm; z-index:5;
  font-family:inherit; font-size:7.5pt; color:#0F1E3D; background:#fff;
  border:0.8pt solid #B8942E; border-radius:2px; padding:1mm 2.5mm; cursor:pointer; }
.pbtn:hover{ background:#B8942E; color:#fff; }

#bar{ position:sticky; top:0; z-index:50; background:#0F1E3D; color:#fff;
  padding:3mm 5mm; display:flex; gap:3mm; align-items:center; flex-wrap:wrap;
  font-size:9.5pt; box-shadow:0 2px 8px rgba(0,0,0,.25); }
#bar b{ color:#B8942E; letter-spacing:1px; margin-right:2mm; }
#bar button, #bar select, #bar label.fb{
  font-family:inherit; font-size:9pt; padding:1.5mm 3mm; border-radius:3px;
  border:0.8pt solid #4A5A78; background:#1B2E4F; color:#fff; cursor:pointer; }
#bar button:hover, #bar label.fb:hover{ background:#B8942E; border-color:#B8942E; }
#bar select{ max-width:70mm; }
#bar .st{ margin-left:auto; font-size:8.5pt; color:#9FB0C8; }
#bar input[type=file]{ display:none; }

@media print{
  #bar, .pbtn{ display:none !important; }
  td[contenteditable]{ background:transparent !important; box-shadow:none !important; }
  td[contenteditable]:empty::before, .ed:empty::before{ content:"" !important; }
  .ed{ border-bottom:0.5pt solid #999; }
  body.single .page{ display:none !important; }
  body.single .page.only{ display:flex !important; }
}

"""

FORMS = [
{
 "docno": 'IMP-L-01',
 "title": '경영이념 · 비전 선언문',
 "loc": '게시 위치: 사무실 주 출입구 · 현장 휴게실',
 "qs": [1],
 "posted": True,
 "html": r"""<div class="page">
  <div class="dochead">
    <div><div class="co">«CO_FULL»</div><div class="ttl">경영이념 · 비전 선언문</div></div><button class="pbtn" onclick="printOne(this)">이 문서만 인쇄</button>
    <div class="meta">문서번호 <b>IMP-L-01</b><br>제정일 20&nbsp;&nbsp;&nbsp;.&nbsp;&nbsp;&nbsp;.&nbsp;&nbsp;&nbsp;.<br>게시용</div>
  </div>
  <div class="poster">
    <div class="eyebrow">OUR VISION</div>
    <h1><span class="ed" contenteditable="true" spellcheck="false" data-ph="비전 문구를 여기에"></span></h1>
    <div class="lead">
      «CO_FULL»은<br>
      <span class="ed" contenteditable="true" spellcheck="false" data-ph="핵심 사업 영역"></span> 분야에서<br>
      <span class="ed" contenteditable="true" spellcheck="false" data-ph="고객에게 제공하는 가치"></span>를 실현합니다.
    </div>
    <div class="rule"></div>
    <div class="items">
      <ul>
        <li><b>경영이념</b> &nbsp;<span class="ed" contenteditable="true" spellcheck="false" data-ph="예: 정직한 품질, 지키는 납기, 함께 크는 회사"></span></li>
        <li><b>핵심가치</b> &nbsp;<span class="ed" contenteditable="true" spellcheck="false" data-ph="가치 1"></span> · <span class="ed" contenteditable="true" spellcheck="false" data-ph="가치 2"></span> · <span class="ed" contenteditable="true" spellcheck="false" data-ph="가치 3"></span></li>
        <li><b>3개년 목표</b> &nbsp;매출 <span class="ed" contenteditable="true" spellcheck="false" data-ph=""></span>억원 · 신제품 <span class="ed" contenteditable="true" spellcheck="false" data-ph=""></span>종 · 불량률 <span class="ed" contenteditable="true" spellcheck="false" data-ph=""></span>% 이하</li>
      </ul>
    </div>
    <div class="sig">
      위와 같이 선언하며, 전 임직원과 함께 실천할 것을 약속합니다.<br><br>
      20&nbsp;&nbsp;&nbsp;&nbsp;년&nbsp;&nbsp;&nbsp;&nbsp;월&nbsp;&nbsp;&nbsp;&nbsp;일<br>
      <b>«CO_FULL» 대표이사</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (인)
    </div>
  </div>
  <div class="foot"><span>게시 위치: 사무실 주 출입구 · 현장 휴게실</span><span>IMP-L-01 · 문항 1</span></div>
</div>""",
},
{
 "docno": 'IMP-L-02',
 "title": '3개년 중장기 경영계획서',
 "loc": '주식회사 아이엠팩',
 "qs": [2],
 "posted": False,
 "html": r"""<div class="page">
  <table class="sign">
    <tr><th>작성</th><th>검토</th><th>승인</th></tr>
    <tr><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>
  <div class="dochead">
    <div><div class="co">«CO_FULL»</div><div class="ttl">3개년 중장기 경영계획서</div></div><button class="pbtn" onclick="printOne(this)">이 문서만 인쇄</button>
  </div>
  <div class="meta" style="font-size:8pt;color:#5A6472;text-align:right;margin:-3mm 0 4mm">
    문서번호 <b style="color:#B8942E">IMP-L-02</b> &nbsp;|&nbsp; 계획기간 20&nbsp;&nbsp;&nbsp;년 ~ 20&nbsp;&nbsp;&nbsp;년 &nbsp;|&nbsp; 수립일 20&nbsp;&nbsp;.&nbsp;&nbsp;.&nbsp;&nbsp;.
  </div>

  <h3 class="sub">1. 경영환경 분석 요약</h3>
  <table>
    <tr><td class="lb">시장 환경</td><td class="h" contenteditable="true" spellcheck="false" data-ph="주요 수요 변화 · 시장 규모 · 성장률"></td></tr>
    <tr><td class="lb">경쟁 환경</td><td class="h" contenteditable="true" spellcheck="false" data-ph="주요 경쟁사 · 당사 포지션"></td></tr>
    <tr><td class="lb">내부 역량</td><td class="h" contenteditable="true" spellcheck="false" data-ph="설비 · 인력 · 기술 보유 수준"></td></tr>
  </table>

  <h3 class="sub">2. 연도별 목표 수치</h3>
  <table>
    <tr>
      <th style="width:34mm">구분</th><th>기준연도 20&nbsp;&nbsp;</th><th>1차연도 20&nbsp;&nbsp;</th><th>2차연도 20&nbsp;&nbsp;</th><th>3차연도 20&nbsp;&nbsp;</th>
    </tr>
    <tr><td class="lb">매출액 (백만원)</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">영업이익 (백만원)</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">영업이익률 (%)</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">상시근로자 (명)</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">신제품 출시 (종)</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">불량률 (%)</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">1인당 매출액 (백만원)</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">3. 연도별 중점 추진과제</h3>
  <table>
    <tr><th style="width:26mm">연도</th><th>중점 추진과제</th><th style="width:30mm">담당 부서</th><th style="width:32mm">소요 예산</th></tr>
    <tr><td class="lb">1차연도</td><td class="hh" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">2차연도</td><td class="hh" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">3차연도</td><td class="hh" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <div class="note">
    <b>작성 요령</b> — 문항 2번은 <b>'연도별 목표 수치'</b>가 명시되어야 체계 등급입니다. 정성적 서술만 있으면 '계획' 등급에 머무릅니다.
    표 2의 숫자 칸을 반드시 채우고, 기준연도는 직전 결산 실적을 그대로 옮기십시오.
  </div>

  <div class="foot"><span>«CO_FULL»</span><span>IMP-L-02 · 문항 2</span></div>
</div>""",
},
{
 "docno": 'IMP-L-03',
 "title": '연도별 경영목표 대비표',
 "loc": '게시 위치: 사무실 주 출입구',
 "qs": [2, 6],
 "posted": True,
 "html": r"""<div class="page">
  <div class="dochead">
    <div><div class="co">«CO_FULL»</div><div class="ttl">연도별 경영목표 대비표</div></div><button class="pbtn" onclick="printOne(this)">이 문서만 인쇄</button>
    <div class="meta">문서번호 <b>IMP-L-03</b><br>대상연도 20&nbsp;&nbsp;&nbsp;년<br>게시용</div>
  </div>

  <table>
    <tr>
      <th rowspan="2" style="width:30mm">관리 지표</th><th rowspan="2" style="width:22mm">연간 목표</th>
      <th colspan="4">분기 실적</th><th rowspan="2" style="width:20mm">누계 실적</th><th rowspan="2" style="width:20mm">달성률</th>
    </tr>
    <tr><th>1Q</th><th>2Q</th><th>3Q</th><th>4Q</th></tr>
    <tr><td class="lb">매출액</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">영업이익</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">신규 수주</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">불량률</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">납기준수율</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">원가절감액</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">교육 이수율</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb"></td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">미달 지표 원인 및 대책</h3>
  <table>
    <tr><th style="width:30mm">지표</th><th>미달 원인</th><th style="width:55mm">개선 대책</th><th style="width:22mm">담당</th></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">직원 공유 이력</h3>
  <table>
    <tr><th style="width:28mm">공유 일자</th><th style="width:34mm">공유 방법</th><th>공유 대상</th><th style="width:26mm">확인자</th></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false" data-ph="게시판 부착 / 조회 / 사내 공지"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <div class="note">
    <b>문항 6번(경영실적 공유) 증빙 겸용</b> — 이 표를 <b>분기마다 갱신해 게시판에 부착</b>하고 하단 공유 이력을 채우면
    문항 2 · 6 두 개를 동시에 커버합니다. 부착 사진을 반드시 남기십시오.
  </div>

  <div class="foot"><span>게시 위치: 사무실 주 출입구</span><span>IMP-L-03 · 문항 2 · 6</span></div>
</div>""",
},
{
 "docno": 'IMP-L-04',
 "title": '월례 경영회의록',
 "loc": '보존연한 5년 · 문서철: 경영회의록철',
 "qs": [3],
 "posted": False,
 "html": r"""<div class="page">
  <table class="sign">
    <tr><th>작성</th><th>검토</th><th>승인</th></tr>
    <tr><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>
  <div class="dochead">
    <div><div class="co">«CO_FULL»</div><div class="ttl">월례 경영회의록</div></div><button class="pbtn" onclick="printOne(this)">이 문서만 인쇄</button>
  </div>
  <div style="font-size:8pt;color:#5A6472;text-align:right;margin:-3mm 0 4mm">
    문서번호 <b style="color:#B8942E">IMP-L-04</b> &nbsp;|&nbsp; 제 &nbsp;&nbsp;&nbsp; 차 회의
  </div>

  <table>
    <tr><td class="lb">일시</td><td style="width:56mm" contenteditable="true" spellcheck="false">20&nbsp;&nbsp;&nbsp;.&nbsp;&nbsp;&nbsp;.&nbsp;&nbsp;&nbsp;. &nbsp;&nbsp;&nbsp;:&nbsp;&nbsp;&nbsp; ~ &nbsp;&nbsp;&nbsp;:&nbsp;&nbsp;&nbsp;</td>
        <td class="lb">장소</td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">주관</td><td contenteditable="true" spellcheck="false">대표이사</td><td class="lb">참석 인원</td><td contenteditable="true" spellcheck="false">총 &nbsp;&nbsp;&nbsp;&nbsp; 명</td></tr>
    <tr><td class="lb">참석자</td><td colspan="3" class="hh" contenteditable="true" spellcheck="false" data-ph="직위 · 성명 (자필 서명 또는 날인)"></td></tr>
  </table>

  <h3 class="sub">1. 전월 지시사항 조치 결과</h3>
  <table>
    <tr><th style="width:12mm">No</th><th>지시 내용</th><th style="width:24mm">담당</th><th style="width:26mm">조치 결과</th><th style="width:20mm">완료 여부</th></tr>
    <tr><td class="c" contenteditable="true" spellcheck="false">1</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c" contenteditable="true" spellcheck="false">2</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c" contenteditable="true" spellcheck="false">3</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">2. 부서별 실적 보고</h3>
  <table>
    <tr><th style="width:26mm">부서</th><th>주요 실적</th><th style="width:24mm">목표 대비</th><th style="width:40mm">특이사항</th></tr>
    <tr><td class="lb">영업</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">생산</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">품질</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">관리</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">3. 협의 안건 및 결정사항</h3>
  <table>
    <tr><th style="width:12mm">No</th><th>안건</th><th style="width:62mm">결정사항</th></tr>
    <tr><td class="c" contenteditable="true" spellcheck="false">1</td><td class="hh" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c" contenteditable="true" spellcheck="false">2</td><td class="hh" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">4. 차월 지시사항</h3>
  <table>
    <tr><th>지시 내용</th><th style="width:24mm">담당</th><th style="width:26mm">완료 기한</th></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <div class="note">
    <b>주의</b> — 문항 3번은 <b>대표이사가 직접 주관</b>하는 정기 회의체여야 합니다.
    '주관' 칸을 대표이사로 고정하고, <b>참석자 자필 서명</b>을 반드시 받으십시오. 최소 3개월분 연속 누적이 필요합니다.
  </div>

  <div class="foot"><span>보존연한 5년 · 문서철: 경영회의록철</span><span>IMP-L-04 · 문항 3</span></div>
</div>""",
},
{
 "docno": 'IMP-L-05',
 "title": '노사협의회 회의록',
 "loc": '보존연한 3년 (법정) · 문서철: 노사협의회철',
 "qs": [4],
 "posted": False,
 "html": r"""<div class="page">
  <table class="sign">
    <tr><th>근로자<br>위원</th><th>사용자<br>위원</th><th>의장</th></tr>
    <tr><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>
  <div class="dochead">
    <div><div class="co">«CO_FULL»</div><div class="ttl">노사협의회 회의록</div></div><button class="pbtn" onclick="printOne(this)">이 문서만 인쇄</button>
  </div>
  <div style="font-size:8pt;color:#5A6472;text-align:right;margin:-3mm 0 4mm">
    문서번호 <b style="color:#B8942E">IMP-L-05</b> &nbsp;|&nbsp; 제 &nbsp;&nbsp;&nbsp; 기 제 &nbsp;&nbsp;&nbsp; 차 회의
  </div>

  <table>
    <tr><td class="lb">일시</td><td style="width:56mm" contenteditable="true" spellcheck="false">20&nbsp;&nbsp;&nbsp;.&nbsp;&nbsp;&nbsp;.&nbsp;&nbsp;&nbsp;. &nbsp;&nbsp;&nbsp;:&nbsp;&nbsp;&nbsp;</td>
        <td class="lb">장소</td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">근로자위원</td><td colspan="3" class="h" contenteditable="true" spellcheck="false" data-ph="성명 (서명)"></td></tr>
    <tr><td class="lb">사용자위원</td><td colspan="3" class="h" contenteditable="true" spellcheck="false" data-ph="성명 (서명)"></td></tr>
  </table>

  <h3 class="sub">1. 협의 사항</h3>
  <table>
    <tr><th style="width:12mm">No</th><th>안건</th><th style="width:52mm">협의 결과</th><th style="width:22mm">시행 시기</th></tr>
    <tr><td class="c" contenteditable="true" spellcheck="false">1</td><td class="hh" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c" contenteditable="true" spellcheck="false">2</td><td class="hh" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c" contenteditable="true" spellcheck="false">3</td><td class="hh" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">2. 보고 사항 <span class="guide" style="font-weight:400">(경영계획 · 생산실적 · 인력계획)</span></h3>
  <table>
    <tr><th style="width:34mm">구분</th><th>보고 내용</th></tr>
    <tr><td class="lb">경영계획 전반</td><td class="h" contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">생산 · 인력 계획</td><td class="h" contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">기타</td><td class="h" contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">3. 근로자 건의사항 및 조치</h3>
  <table>
    <tr><th>건의 내용</th><th style="width:52mm">조치 계획 · 결과</th><th style="width:22mm">담당</th></tr>
    <tr><td class="hh" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="hh" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <div class="note">
    <b>법적 근거</b> — 상시근로자 30인 이상 사업장은 「근로자참여 및 협력증진에 관한 법률」에 따라
    <b>3개월마다 정기 노사협의회 개최 의무</b>가 있습니다. 미개최 시 과태료 대상이며, 메인비즈 문항 4번도 자동 실점입니다.
    <b>회의록은 작성일로부터 3년간 보존</b>해야 합니다.
  </div>

  <div class="foot"><span>보존연한 3년 (법정) · 문서철: 노사협의회철</span><span>IMP-L-05 · 문항 4</span></div>
</div>""",
},
{
 "docno": 'IMP-L-06',
 "title": '직원 제안제도 접수 · 처리 대장',
 "loc": '주식회사 아이엠팩',
 "qs": [4],
 "posted": False,
 "html": r"""<div class="page">
  <div class="dochead">
    <div><div class="co">«CO_FULL»</div><div class="ttl">직원 제안제도 접수 · 처리 대장</div></div><button class="pbtn" onclick="printOne(this)">이 문서만 인쇄</button>
    <div class="meta">문서번호 <b>IMP-L-06</b><br>대상연도 20&nbsp;&nbsp;&nbsp;년</div>
  </div>

  <table>
    <tr>
      <th style="width:11mm">연번</th><th style="width:22mm">접수일</th><th style="width:22mm">제안자</th>
      <th>제안 내용</th><th style="width:40mm">검토 결과</th><th style="width:20mm">채택<br>여부</th><th style="width:22mm">포상</th>
    </tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">1</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">2</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">3</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">4</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">5</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">6</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">7</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">8</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">9</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">10</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">11</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">12</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">13</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">14</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">15</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">연간 집계</h3>
  <table>
    <tr><th>접수 건수</th><th>채택 건수</th><th>채택률</th><th>포상 총액</th><th>추정 개선 효과</th></tr>
    <tr><td class="h c" contenteditable="true" spellcheck="false"></td><td class="c" contenteditable="true" spellcheck="false"></td><td class="c" contenteditable="true" spellcheck="false"></td><td class="c" contenteditable="true" spellcheck="false"></td><td class="c" contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <div class="note">
    <b>운영 요령</b> — 게시판 옆에 <b>제안함(A4 용지 + 필기구)</b>을 설치하고, 월 1회 개봉해 이 대장에 기록하십시오.
    채택 제안은 <b>소액이라도 포상</b>하면 문항 4번 '직원 의견수렴 채널' 증빙이 확실해집니다.
  </div>

  <div class="foot"><span>«CO_FULL»</span><span>IMP-L-06 · 문항 4</span></div>
</div>""",
},
{
 "docno": 'IMP-L-07',
 "title": '윤리 · 준법경영 헌장',
 "loc": '게시 위치: 사무실 주 출입구 · 현장 휴게실',
 "qs": [5],
 "posted": True,
 "html": r"""<div class="page">
  <div class="dochead">
    <div><div class="co">«CO_FULL»</div><div class="ttl">윤리 · 준법경영 헌장</div></div><button class="pbtn" onclick="printOne(this)">이 문서만 인쇄</button>
    <div class="meta">문서번호 <b>IMP-L-07</b><br>제정일 20&nbsp;&nbsp;&nbsp;.&nbsp;&nbsp;&nbsp;.&nbsp;&nbsp;&nbsp;.<br>게시용</div>
  </div>
  <div class="poster" style="justify-content:flex-start;padding-top:6mm">
    <div class="eyebrow">CODE OF ETHICS</div>
    <div class="rule" style="margin:6mm auto"></div>
    <div class="items" style="max-width:158mm">
      <ul>
        <li style="font-size:11.5pt;line-height:1.9;margin-bottom:5mm"><b>하나.</b> 우리는 모든 법령과 사내 규정을 준수하며, 어떠한 경우에도 이를 우회하지 않는다.</li>
        <li style="font-size:11.5pt;line-height:1.9;margin-bottom:5mm"><b>하나.</b> 우리는 고객에게 정직한 품질과 정확한 정보를 제공하며, 약속한 납기를 지킨다.</li>
        <li style="font-size:11.5pt;line-height:1.9;margin-bottom:5mm"><b>하나.</b> 우리는 거래처와 공정하게 거래하며, 우월적 지위를 이용해 부당한 요구를 하지 않는다.</li>
        <li style="font-size:11.5pt;line-height:1.9;margin-bottom:5mm"><b>하나.</b> 우리는 직무와 관련해 금품 · 향응을 주고받지 않는다.</li>
        <li style="font-size:11.5pt;line-height:1.9;margin-bottom:5mm"><b>하나.</b> 우리는 회사의 자산과 영업비밀을 보호하며, 사적으로 사용하지 않는다.</li>
        <li style="font-size:11.5pt;line-height:1.9;margin-bottom:5mm"><b>하나.</b> 우리는 성별 · 연령 · 출신 등을 이유로 차별하지 않으며, 직장 내 괴롭힘과 성희롱을 용납하지 않는다.</li>
        <li style="font-size:11.5pt;line-height:1.9;margin-bottom:5mm"><b>하나.</b> 우리는 안전을 최우선으로 하며, 안전수칙 위반을 묵인하지 않는다.</li>
        <li style="font-size:11.5pt;line-height:1.9"><b>하나.</b> 우리는 위반 사실을 알게 된 경우 즉시 신고하며, 신고자는 어떠한 불이익도 받지 않는다.</li>
      </ul>
    </div>
    <div class="sig" style="margin-top:10mm;font-size:10pt">
      본 헌장은 전 임직원에게 적용되며, 위반 시 사규에 따라 조치한다.<br>
      <span style="font-size:9pt;color:#5A6472">신고 채널 &nbsp;|&nbsp; 담당 <span class="ed" contenteditable="true" spellcheck="false" data-ph=""></span> &nbsp;·&nbsp; 연락처 <span class="ed" contenteditable="true" spellcheck="false" data-ph=""></span> &nbsp;·&nbsp; 신고함 (사무실 게시판 옆)</span><br><br>
      20&nbsp;&nbsp;&nbsp;&nbsp;년&nbsp;&nbsp;&nbsp;&nbsp;월&nbsp;&nbsp;&nbsp;&nbsp;일<br>
      <b>«CO_FULL» 대표이사</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (인)
    </div>
  </div>
  <div class="foot"><span>게시 위치: 사무실 주 출입구 · 현장 휴게실</span><span>IMP-L-07 · 문항 5</span></div>
</div>""",
},
{
 "docno": 'IMP-L-08',
 "title": '윤리 · 준법교육 이수 기록부',
 "loc": '주식회사 아이엠팩',
 "qs": [5],
 "posted": False,
 "html": r"""<div class="page">
  <table class="sign">
    <tr><th>작성</th><th>승인</th></tr>
    <tr><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>
  <div class="dochead">
    <div><div class="co">«CO_FULL»</div><div class="ttl">윤리 · 준법교육 이수 기록부</div></div><button class="pbtn" onclick="printOne(this)">이 문서만 인쇄</button>
  </div>
  <div style="font-size:8pt;color:#5A6472;text-align:right;margin:-3mm 0 4mm">
    문서번호 <b style="color:#B8942E">IMP-L-08</b>
  </div>

  <table>
    <tr><td class="lb">교육명</td><td colspan="3" contenteditable="true" spellcheck="false" data-ph="예: 윤리경영 및 직장 내 괴롭힘 예방 교육"></td></tr>
    <tr><td class="lb">일시</td><td style="width:52mm" contenteditable="true" spellcheck="false">20&nbsp;&nbsp;&nbsp;.&nbsp;&nbsp;&nbsp;.&nbsp;&nbsp;&nbsp;. &nbsp;&nbsp;&nbsp;:&nbsp;&nbsp;&nbsp; ~ &nbsp;&nbsp;&nbsp;:&nbsp;&nbsp;&nbsp;</td>
        <td class="lb">장소</td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">강사</td><td contenteditable="true" spellcheck="false"></td><td class="lb">교육 시간</td><td contenteditable="true" spellcheck="false">&nbsp;&nbsp;&nbsp;&nbsp; 시간</td></tr>
    <tr><td class="lb">교육 내용</td><td colspan="3" class="hh" contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">이수자 명단</h3>
  <table>
    <tr><th style="width:11mm">No</th><th style="width:28mm">부서</th><th style="width:28mm">직위</th><th style="width:32mm">성명</th><th>서명</th>
        <th style="width:11mm">No</th><th style="width:28mm">부서</th><th style="width:32mm">성명</th><th>서명</th></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">1</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td class="c" contenteditable="true" spellcheck="false">11</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">2</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td class="c" contenteditable="true" spellcheck="false">12</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">3</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td class="c" contenteditable="true" spellcheck="false">13</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">4</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td class="c" contenteditable="true" spellcheck="false">14</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">5</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td class="c" contenteditable="true" spellcheck="false">15</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">6</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td class="c" contenteditable="true" spellcheck="false">16</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">7</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td class="c" contenteditable="true" spellcheck="false">17</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">8</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td class="c" contenteditable="true" spellcheck="false">18</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">9</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td class="c" contenteditable="true" spellcheck="false">19</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">10</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td class="c" contenteditable="true" spellcheck="false">20</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <table style="margin-top:4mm">
    <tr><th style="width:34mm">교육 사진 첨부</th><td class="hhh" contenteditable="true" spellcheck="false" data-ph="교육 현장 사진 2매 이상 부착 (강의 장면 · 참석자 전경)"></td></tr>
  </table>

  <div class="note">
    <b>연 1회 이상 실시</b>하고 이수율 100%를 목표로 하십시오. 외부 강사 없이 <b>대표이사 또는 관리책임자가 직접 30분 교육</b>해도
    기록부 + 사진이 있으면 증빙으로 인정됩니다. 법정 의무교육(성희롱 예방 · 산업안전보건 등)과 묶어 진행하면 효율적입니다.
  </div>

  <div class="foot"><span>«CO_FULL»</span><span>IMP-L-08 · 문항 5</span></div>
</div>""",
},
{
 "docno": 'IMP-L-09',
 "title": '월간 경영실적 공유',
 "loc": '게시 위치: 사무실 주 출입구 · 현장 휴게실',
 "qs": [6],
 "posted": True,
 "html": r"""<div class="page">
  <div class="dochead">
    <div><div class="co">«CO_FULL»</div><div class="ttl">월간 경영실적 공유</div></div><button class="pbtn" onclick="printOne(this)">이 문서만 인쇄</button>
    <div class="meta">문서번호 <b>IMP-L-09</b><br>20&nbsp;&nbsp;&nbsp;년 &nbsp;&nbsp;&nbsp;월<br>게시용</div>
  </div>

  <div class="sec">이번 달 우리 회사 성적표</div>
  <table>
    <tr><th style="width:36mm">항목</th><th style="width:32mm">이번 달 목표</th><th style="width:32mm">이번 달 실적</th><th style="width:26mm">달성률</th><th>한 줄 코멘트</th></tr>
    <tr><td class="lb">매출액</td><td class="hh" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">생산량</td><td class="hh" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">불량률</td><td class="hh" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">납기준수율</td><td class="hh" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">무재해 일수</td><td class="hh" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">잘한 점</h3>
  <table><tr><td class="hhh" contenteditable="true" spellcheck="false"></td></tr></table>

  <h3 class="sub">다음 달 우리가 함께 할 일</h3>
  <table><tr><td class="hhh" contenteditable="true" spellcheck="false"></td></tr></table>

  <h3 class="sub">이달의 칭찬</h3>
  <table>
    <tr><th style="width:34mm">부서 · 성명</th><th>사유</th></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <div class="note">
    <b>게시 후 사진 촬영 필수</b> — 문항 6번은 '직원에게 정기적으로 공유'가 핵심입니다.
    매월 말 이 양식을 채워 게시하고, <b>부착된 상태의 사진</b>을 월별로 모아두면 '체계' 등급이 확실합니다.
    작성일 20&nbsp;&nbsp;&nbsp;.&nbsp;&nbsp;&nbsp;.&nbsp;&nbsp;&nbsp;. &nbsp;/&nbsp; 작성자 <span class="ed" contenteditable="true" spellcheck="false" data-ph=""></span>
  </div>

  <div class="foot"><span>게시 위치: 사무실 주 출입구 · 현장 휴게실</span><span>IMP-L-09 · 문항 6</span></div>
</div>""",
},
{
 "docno": 'IMP-S-01',
 "title": '3개년 경영혁신 로드맵',
 "loc": '게시 위치: 사무실 주 출입구',
 "qs": [7],
 "posted": True,
 "html": r"""<div class="page">
  <div class="dochead">
    <div><div class="co">«CO_FULL»</div><div class="ttl">3개년 경영혁신 로드맵</div></div><button class="pbtn" onclick="printOne(this)">이 문서만 인쇄</button>
    <div class="meta">문서번호 <b>IMP-S-01</b><br>20&nbsp;&nbsp;&nbsp; ~ 20&nbsp;&nbsp;&nbsp;<br>게시용</div>
  </div>

  <table>
    <tr>
      <th style="width:30mm">혁신 영역</th>
      <th>1차연도 20&nbsp;&nbsp;&nbsp;<br><span class="guide" style="font-weight:400">기반 구축</span></th>
      <th>2차연도 20&nbsp;&nbsp;&nbsp;<br><span class="guide" style="font-weight:400">확산 · 정착</span></th>
      <th>3차연도 20&nbsp;&nbsp;&nbsp;<br><span class="guide" style="font-weight:400">고도화</span></th>
    </tr>
    <tr><td class="lb">조직 · 인력</td><td class="hhh" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">제품 · 서비스</td><td class="hhh" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">공정 · 품질</td><td class="hhh" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">마케팅 · 판로</td><td class="hhh" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">정보화 · 시스템</td><td class="hhh" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">연도별 목표 수치</h3>
  <table>
    <tr><th style="width:30mm">지표</th><th>현재</th><th>1차연도</th><th>2차연도</th><th>3차연도</th></tr>
    <tr><td class="lb">매출액</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">불량률</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">생산성 (1인당)</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">신제품 매출 비중</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <div class="note">
    <b>작성 요령</b> — 각 칸에 <b>과제명 + 완료 시기</b>를 함께 적으십시오(예: "SOP 12종 제정 — 1차연도 3분기").
    빈칸이 있어도 무방하나, <b>5개 영역 × 3개년 중 최소 8개 칸</b>은 채워야 로드맵으로 인정됩니다.
  </div>

  <div class="foot"><span>게시 위치: 사무실 주 출입구</span><span>IMP-S-01 · 문항 7</span></div>
</div>""",
},
{
 "docno": 'IMP-S-02',
 "title": '혁신 과제 정의서',
 "loc": '주식회사 아이엠팩',
 "qs": [8],
 "posted": False,
 "html": r"""<div class="page">
  <table class="sign">
    <tr><th>작성</th><th>검토</th><th>승인</th></tr>
    <tr><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>
  <div class="dochead">
    <div><div class="co">«CO_FULL»</div><div class="ttl">혁신 과제 정의서</div></div><button class="pbtn" onclick="printOne(this)">이 문서만 인쇄</button>
  </div>
  <div style="font-size:8pt;color:#5A6472;text-align:right;margin:-3mm 0 4mm">
    문서번호 <b style="color:#B8942E">IMP-S-02</b> &nbsp;|&nbsp; 과제번호 IN-20&nbsp;&nbsp;-&nbsp;&nbsp;&nbsp;
  </div>

  <table>
    <tr><td class="lb">과제명</td><td colspan="3" class="h" contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">혁신 영역</td><td style="width:52mm" contenteditable="true" spellcheck="false" data-ph="조직 / 제품 / 공정 / 마케팅 / 정보화"></td>
        <td class="lb">과제 등급</td><td contenteditable="true" spellcheck="false" data-ph="전사 / 부서"></td></tr>
    <tr><td class="lb">담당자</td><td contenteditable="true" spellcheck="false"></td><td class="lb">총괄 책임자</td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">추진 기간</td><td contenteditable="true" spellcheck="false">20&nbsp;&nbsp;.&nbsp;&nbsp;. ~ 20&nbsp;&nbsp;.&nbsp;&nbsp;.</td>
        <td class="lb">소요 예산</td><td contenteditable="true" spellcheck="false">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 천원</td></tr>
  </table>

  <h3 class="sub">1. 추진 배경 및 문제 정의</h3>
  <table><tr><td class="hhh" contenteditable="true" spellcheck="false"></td></tr></table>

  <h3 class="sub">2. 목표 수치 (KPI)</h3>
  <table>
    <tr><th style="width:44mm">KPI 명</th><th style="width:30mm">현재 수준</th><th style="width:30mm">목표 수준</th><th style="width:26mm">측정 주기</th><th>측정 방법</th></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">3. 세부 실행 계획</h3>
  <table>
    <tr><th style="width:12mm">No</th><th>실행 항목</th><th style="width:24mm">담당</th><th style="width:28mm">완료 기한</th><th style="width:20mm">진척률</th></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">1</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">2</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">3</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">4</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">5</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">4. 기대 효과</h3>
  <table>
    <tr><td class="lb">정량 효과</td><td class="h" contenteditable="true" spellcheck="false" data-ph="원가 절감액 · 시간 단축 · 불량 감소 등 숫자로"></td></tr>
    <tr><td class="lb">정성 효과</td><td class="h" contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <div class="note">
    <b>문항 8번 핵심</b> — <b>담당자 · 기한 · 목표수치(KPI)</b> 세 가지가 모두 명시되어야 '체계' 등급입니다.
    과제는 <b>최소 3건 이상</b> 작성해 두십시오.
  </div>

  <div class="foot"><span>«CO_FULL»</span><span>IMP-S-02 · 문항 8</span></div>
</div>""",
},
{
 "docno": 'IMP-S-03',
 "title": '혁신 과제 KPI 관리표',
 "loc": '게시 위치: 사무실 주 출입구',
 "qs": [8, 9],
 "posted": True,
 "html": r"""<div class="page">
  <div class="dochead">
    <div><div class="co">«CO_FULL»</div><div class="ttl">혁신 과제 KPI 관리표</div></div><button class="pbtn" onclick="printOne(this)">이 문서만 인쇄</button>
    <div class="meta">문서번호 <b>IMP-S-03</b><br>대상연도 20&nbsp;&nbsp;&nbsp;년<br>게시용</div>
  </div>

  <table>
    <tr>
      <th style="width:11mm">No</th><th style="width:44mm">과제명</th><th style="width:22mm">담당자</th>
      <th style="width:24mm">완료 기한</th><th style="width:32mm">KPI (현재 → 목표)</th>
      <th>1Q</th><th>2Q</th><th>3Q</th><th>4Q</th><th style="width:18mm">달성</th>
    </tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">1</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">2</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">3</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">4</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">5</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">6</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">7</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">8</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">9</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">10</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <table style="margin-top:5mm">
    <tr><th style="width:40mm">전체 과제 수</th><th style="width:40mm">완료</th><th style="width:40mm">진행중</th><th>전체 달성률</th></tr>
    <tr><td class="h c" contenteditable="true" spellcheck="false"></td><td class="c" contenteditable="true" spellcheck="false"></td><td class="c" contenteditable="true" spellcheck="false"></td><td class="c" contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <div class="note">
    <b>분기별 갱신 후 게시</b> — 이 표 한 장이 문항 8 · 9번을 동시에 증빙합니다.
    분기 칸에는 <b>실적 수치</b>를 적고, 목표 미달 시 붉은 펜으로 표시해 관리 흔적을 남기십시오.
  </div>

  <div class="foot"><span>게시 위치: 사무실 주 출입구</span><span>IMP-S-03 · 문항 8 · 9</span></div>
</div>""",
},
{
 "docno": 'IMP-S-04',
 "title": '목표 대비 실적 점검표',
 "loc": '주식회사 아이엠팩',
 "qs": [9],
 "posted": False,
 "html": r"""<div class="page">
  <table class="sign">
    <tr><th>작성</th><th>검토</th><th>승인</th></tr>
    <tr><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>
  <div class="dochead">
    <div><div class="co">«CO_FULL»</div><div class="ttl">목표 대비 실적 점검표</div></div><button class="pbtn" onclick="printOne(this)">이 문서만 인쇄</button>
  </div>
  <div style="font-size:8pt;color:#5A6472;text-align:right;margin:-3mm 0 4mm">
    문서번호 <b style="color:#B8942E">IMP-S-04</b> &nbsp;|&nbsp; 점검 대상 20&nbsp;&nbsp;년 &nbsp;&nbsp;분기 &nbsp;|&nbsp; 점검일 20&nbsp;&nbsp;.&nbsp;&nbsp;.&nbsp;&nbsp;.
  </div>

  <table>
    <tr>
      <th style="width:11mm">No</th><th style="width:46mm">점검 항목</th><th style="width:24mm">목표</th>
      <th style="width:24mm">실적</th><th style="width:20mm">달성률</th><th style="width:18mm">판정</th><th>미달 사유 · 대책</th>
    </tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">1</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">2</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">3</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">4</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">5</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">6</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">7</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">8</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">9</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">10</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">종합 의견</h3>
  <table><tr><td class="hhh" contenteditable="true" spellcheck="false"></td></tr></table>

  <h3 class="sub">차기 분기 중점 관리 항목</h3>
  <table>
    <tr><th>항목</th><th style="width:26mm">담당</th><th style="width:30mm">목표</th></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <div class="note"><b>판정 기준</b> — 달성 ○ / 부분달성 △ / 미달 × 로 표기. <b>분기 1회 이상 · 연 4회</b> 기록이 누적되어야 '정기적 점검'으로 인정됩니다.</div>

  <div class="foot"><span>«CO_FULL»</span><span>IMP-S-04 · 문항 9</span></div>
</div>""",
},
{
 "docno": 'IMP-S-05',
 "title": '혁신 추진 점검 회의록',
 "loc": '주식회사 아이엠팩',
 "qs": [9],
 "posted": False,
 "html": r"""<div class="page">
  <table class="sign">
    <tr><th>작성</th><th>승인</th></tr>
    <tr><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>
  <div class="dochead">
    <div><div class="co">«CO_FULL»</div><div class="ttl">혁신 추진 점검 회의록</div></div><button class="pbtn" onclick="printOne(this)">이 문서만 인쇄</button>
  </div>
  <div style="font-size:8pt;color:#5A6472;text-align:right;margin:-3mm 0 4mm">
    문서번호 <b style="color:#B8942E">IMP-S-05</b> &nbsp;|&nbsp; 제 &nbsp;&nbsp;&nbsp; 차
  </div>

  <table>
    <tr><td class="lb">일시</td><td style="width:56mm" contenteditable="true" spellcheck="false">20&nbsp;&nbsp;&nbsp;.&nbsp;&nbsp;&nbsp;.&nbsp;&nbsp;&nbsp;. &nbsp;&nbsp;&nbsp;:&nbsp;&nbsp;&nbsp;</td><td class="lb">장소</td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">참석자</td><td colspan="3" class="hh" contenteditable="true" spellcheck="false" data-ph="직위 · 성명 (서명)"></td></tr>
  </table>

  <h3 class="sub">과제별 진척 점검</h3>
  <table>
    <tr><th style="width:44mm">과제명</th><th style="width:22mm">담당</th><th style="width:20mm">계획 진척</th><th style="width:20mm">실제 진척</th><th>지연 사유 · 조치</th></tr>
    <tr><td class="hh" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="hh" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="hh" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="hh" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="hh" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">결정사항 및 후속 조치</h3>
  <table>
    <tr><th style="width:12mm">No</th><th>결정사항</th><th style="width:24mm">담당</th><th style="width:28mm">기한</th></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">1</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">2</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">3</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">4</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <div class="note"><b>주기</b> — 월 1회 또는 분기 1회. 월례 경영회의(IMP-L-04)의 안건으로 통합해도 되나, <b>별도 회의록으로 분리</b>하면 증빙 효과가 더 큽니다.</div>

  <div class="foot"><span>«CO_FULL»</span><span>IMP-S-05 · 문항 9</span></div>
</div>""",
},
{
 "docno": 'IMP-S-06',
 "title": 'SWOT 분석 · 시장 · 경쟁사 조사 보고서',
 "loc": '주식회사 아이엠팩',
 "qs": [10, 36],
 "posted": False,
 "html": r"""<div class="page">
  <table class="sign">
    <tr><th>작성</th><th>검토</th><th>승인</th></tr>
    <tr><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>
  <div class="dochead">
    <div><div class="co">«CO_FULL»</div><div class="ttl">SWOT 분석 · 시장 · 경쟁사 조사 보고서</div></div><button class="pbtn" onclick="printOne(this)">이 문서만 인쇄</button>
  </div>
  <div style="font-size:8pt;color:#5A6472;text-align:right;margin:-3mm 0 4mm">
    문서번호 <b style="color:#B8942E">IMP-S-06</b> &nbsp;|&nbsp; 작성일 20&nbsp;&nbsp;.&nbsp;&nbsp;.&nbsp;&nbsp;.
  </div>

  <h3 class="sub">1. SWOT 분석</h3>
  <table>
    <tr><th style="width:50%">S · 강점 (내부)</th><th>W · 약점 (내부)</th></tr>
    <tr><td class="hhh" style="height:34mm" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><th>O · 기회 (외부)</th><th>T · 위협 (외부)</th></tr>
    <tr><td class="hhh" style="height:34mm" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">2. 도출 전략</h3>
  <table>
    <tr><th style="width:24mm">전략 유형</th><th>전략 내용</th><th style="width:24mm">담당</th><th style="width:26mm">추진 시기</th></tr>
    <tr><td class="lb">SO 공격</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">ST 다각화</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">WO 보완</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">WT 방어</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">3. 경쟁사 비교</h3>
  <table>
    <tr><th style="width:30mm">비교 항목</th><th>당사</th><th>경쟁사 A</th><th>경쟁사 B</th></tr>
    <tr><td class="lb">주력 제품</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">가격 수준</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">품질 · 기술</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">납기</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">주요 고객군</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">4. 영업전략 반영 사항</h3>
  <table><tr><td class="hhh" contenteditable="true" spellcheck="false"></td></tr></table>

  <div class="note"><b>문항 10 · 36번 동시 증빙</b> — 조사 결과가 <b>실제 영업전략에 반영된 흔적</b>(4항)이 있어야 두 문항 모두 인정됩니다. 연 1회 이상 갱신하십시오.</div>

  <div class="foot"><span>«CO_FULL»</span><span>IMP-S-06 · 문항 10 · 36</span></div>
</div>""",
},
{
 "docno": 'IMP-S-07',
 "title": '혁신활동 예산편성 · 집행 내역서',
 "loc": '주식회사 아이엠팩',
 "qs": [11],
 "posted": False,
 "html": r"""<div class="page">
  <table class="sign">
    <tr><th>작성</th><th>검토</th><th>승인</th></tr>
    <tr><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>
  <div class="dochead">
    <div><div class="co">«CO_FULL»</div><div class="ttl">혁신활동 예산편성 · 집행 내역서</div></div><button class="pbtn" onclick="printOne(this)">이 문서만 인쇄</button>
  </div>
  <div style="font-size:8pt;color:#5A6472;text-align:right;margin:-3mm 0 4mm">
    문서번호 <b style="color:#B8942E">IMP-S-07</b> &nbsp;|&nbsp; 20&nbsp;&nbsp;&nbsp;년도 &nbsp;|&nbsp; 단위: 천원
  </div>

  <h3 class="sub">1. 연간 예산 편성</h3>
  <table>
    <tr><th style="width:36mm">예산 항목</th><th style="width:28mm">편성액</th><th style="width:28mm">집행액</th><th style="width:24mm">집행률</th><th>비고</th></tr>
    <tr><td class="lb">연구개발비</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">설비 · 자동화 투자</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">교육훈련비</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">인증 취득비</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">정보화 시스템</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">마케팅 · 판로개척</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">컨설팅비</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">기타</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb" style="background:#EDF0F4">합계</td><td class="h" style="background:#F6F8FA" contenteditable="true" spellcheck="false"></td><td style="background:#F6F8FA" contenteditable="true" spellcheck="false"></td><td style="background:#F6F8FA" contenteditable="true" spellcheck="false"></td><td style="background:#F6F8FA" contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">2. 주요 집행 내역</h3>
  <table>
    <tr><th style="width:11mm">No</th><th style="width:24mm">집행일</th><th>집행 내용</th><th style="width:28mm">거래처</th><th style="width:26mm">금액</th><th style="width:22mm">증빙</th></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">1</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">2</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">3</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">4</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">5</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">6</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">7</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">8</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <div class="note"><b>문항 11번 핵심</b> — '별도로 편성'이 요건입니다. 일반 판관비에 섞여 있으면 인정되지 않으니, <b>예산 항목을 분리</b>하고 세금계산서 · 이체증을 함께 편철하십시오.</div>

  <div class="foot"><span>«CO_FULL»</span><span>IMP-S-07 · 문항 11</span></div>
</div>""",
},
{
 "docno": 'IMP-R-01',
 "title": '연간 교육훈련 계획서',
 "loc": '게시 위치: 사무실 게시판',
 "qs": [16, 22],
 "posted": True,
 "html": r"""<div class="page">
  <table class="sign">
    <tr><th>작성</th><th>승인</th></tr>
    <tr><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>
  <div class="dochead">
    <div><div class="co">«CO_FULL»</div><div class="ttl">연간 교육훈련 계획서</div></div><button class="pbtn" onclick="printOne(this)">이 문서만 인쇄</button>
  </div>
  <div style="font-size:8pt;color:#5A6472;text-align:right;margin:-3mm 0 4mm">
    문서번호 <b style="color:#B8942E">IMP-R-01</b> &nbsp;|&nbsp; 20&nbsp;&nbsp;&nbsp;년도 &nbsp;|&nbsp; 게시용
  </div>

  <table>
    <tr>
      <th style="width:11mm">No</th><th style="width:44mm">교육 과정명</th><th style="width:22mm">구분</th>
      <th style="width:24mm">대상</th><th style="width:18mm">인원</th><th style="width:18mm">시간</th>
      <th style="width:22mm">시행 시기</th><th style="width:24mm">예산(천원)</th><th>비고</th>
    </tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">1</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false" data-ph="법정"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">2</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false" data-ph="직무"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">3</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false" data-ph="안전"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">4</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">5</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">6</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">7</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">8</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">9</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">10</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c" style="background:#EDF0F4" colspan="7" contenteditable="true" spellcheck="false"><b>합계</b></td><td class="h" style="background:#F6F8FA" contenteditable="true" spellcheck="false"></td><td style="background:#F6F8FA" contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">교육비 집행 실적</h3>
  <table>
    <tr><th style="width:30mm">구분</th><th>1분기</th><th>2분기</th><th>3분기</th><th>4분기</th><th style="width:26mm">합계</th></tr>
    <tr><td class="lb">계획액</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">집행액</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">집행률</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <div class="note"><b>문항 16번 핵심</b> — '계획 수립 + 예산 실제 집행' 두 가지가 모두 필요합니다. 계획서만 있고 집행 내역이 없으면 '계획' 등급에 머무릅니다. <b>교육비 세금계산서 · 이체증</b>을 반드시 함께 편철하십시오.</div>

  <div class="foot"><span>게시 위치: 사무실 게시판</span><span>IMP-R-01 · 문항 16 · 22</span></div>
</div>""",
},
{
 "docno": 'IMP-R-02',
 "title": '교육훈련 이수 대장',
 "loc": '주식회사 아이엠팩',
 "qs": [16, 22],
 "posted": False,
 "html": r"""<div class="page">
  <div class="dochead">
    <div><div class="co">«CO_FULL»</div><div class="ttl">교육훈련 이수 대장</div></div><button class="pbtn" onclick="printOne(this)">이 문서만 인쇄</button>
    <div class="meta">문서번호 <b>IMP-R-02</b><br>20&nbsp;&nbsp;&nbsp;년도</div>
  </div>

  <table>
    <tr>
      <th style="width:11mm">No</th><th style="width:24mm">교육일자</th><th style="width:46mm">교육 과정명</th>
      <th style="width:22mm">부서</th><th style="width:24mm">성명</th><th style="width:16mm">시간</th>
      <th style="width:24mm">수료 여부</th><th>수료증 번호</th>
    </tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">1</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">2</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">3</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">4</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">5</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">6</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">7</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">8</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">9</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">10</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">11</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">12</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">13</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">14</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">15</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">16</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">17</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">18</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <table style="margin-top:4mm">
    <tr><th style="width:44mm">계획 대비 이수율</th><th style="width:44mm">1인당 평균 교육시간</th><th>수료증 보관 위치</th></tr>
    <tr><td class="h c" contenteditable="true" spellcheck="false"></td><td class="c" contenteditable="true" spellcheck="false"></td><td class="c" contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <div class="note"><b>문항 22번</b> — '계획대로 실시 + 이수 실적 관리'가 요건입니다. 계획서(IMP-R-01)와 이 대장이 <b>한 세트</b>로 제출되어야 합니다.</div>

  <div class="foot"><span>«CO_FULL»</span><span>IMP-R-02 · 문항 16 · 22</span></div>
</div>""",
},
{
 "docno": 'IMP-R-03',
 "title": '직무기술서',
 "loc": '주식회사 아이엠팩',
 "qs": [17],
 "posted": False,
 "html": r"""<div class="page">
  <table class="sign">
    <tr><th>작성</th><th>승인</th></tr>
    <tr><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>
  <div class="dochead">
    <div><div class="co">«CO_FULL»</div><div class="ttl">직무기술서</div></div><button class="pbtn" onclick="printOne(this)">이 문서만 인쇄</button>
  </div>
  <div style="font-size:8pt;color:#5A6472;text-align:right;margin:-3mm 0 4mm">
    문서번호 <b style="color:#B8942E">IMP-R-03</b> &nbsp;|&nbsp; 제정 20&nbsp;&nbsp;.&nbsp;&nbsp;.&nbsp;&nbsp;. &nbsp;|&nbsp; 개정 20&nbsp;&nbsp;.&nbsp;&nbsp;.&nbsp;&nbsp;.
  </div>

  <table>
    <tr><td class="lb">직무명</td><td style="width:56mm" contenteditable="true" spellcheck="false"></td><td class="lb">소속 부서</td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">직급 · 직위</td><td contenteditable="true" spellcheck="false"></td><td class="lb">보고 라인</td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">직무 목적</td><td colspan="3" class="hh" contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">1. 주요 책임 및 업무</h3>
  <table>
    <tr><th style="width:12mm">No</th><th>업무 내용</th><th style="width:24mm">비중(%)</th><th style="width:26mm">수행 주기</th></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">1</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">2</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">3</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">4</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">5</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">2. 요구 역량 및 자격 요건</h3>
  <table>
    <tr><td class="lb">학력 · 전공</td><td style="width:56mm" class="h" contenteditable="true" spellcheck="false"></td><td class="lb">경력</td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">필수 자격증</td><td class="h" contenteditable="true" spellcheck="false"></td><td class="lb">우대 자격</td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">필요 지식 · 기술</td><td colspan="3" class="hh" contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">필요 교육</td><td colspan="3" class="h" contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">3. 성과 지표</h3>
  <table>
    <tr><th style="width:50mm">평가 지표</th><th style="width:34mm">목표 수준</th><th>측정 방법</th></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <div class="note"><b>작성 범위</b> — 전 직무를 다 만들 필요는 없습니다. <b>핵심 직무 5~8개</b>(생산관리 · 품질 · 영업 · 구매 · 설비 등)만 작성해도 문항 17번 인정됩니다.</div>

  <div class="foot"><span>«CO_FULL»</span><span>IMP-R-03 · 문항 17</span></div>
</div>""",
},
{
 "docno": 'IMP-R-04',
 "title": '핵심인력 현황 및 승계 계획표',
 "loc": '주식회사 아이엠팩',
 "qs": [17],
 "posted": False,
 "html": r"""<div class="page">
  <table class="sign">
    <tr><th>작성</th><th>승인</th></tr>
    <tr><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>
  <div class="dochead">
    <div><div class="co">«CO_FULL»</div><div class="ttl">핵심인력 현황 및 승계 계획표</div></div><button class="pbtn" onclick="printOne(this)">이 문서만 인쇄</button>
  </div>
  <div style="font-size:8pt;color:#5A6472;text-align:right;margin:-3mm 0 4mm">
    문서번호 <b style="color:#B8942E">IMP-R-04</b> &nbsp;|&nbsp; 기준일 20&nbsp;&nbsp;.&nbsp;&nbsp;.&nbsp;&nbsp;.
  </div>

  <h3 class="sub">1. 핵심 직무 인력 현황</h3>
  <table>
    <tr>
      <th style="width:11mm">No</th><th style="width:34mm">핵심 직무</th><th style="width:24mm">현 담당자</th>
      <th style="width:18mm">근속</th><th style="width:26mm">보유 자격 · 기술</th><th style="width:24mm">대체 가능 인력</th><th>공백 위험도</th>
    </tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">1</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">2</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">3</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">4</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">5</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">6</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">2. 경력개발 · 승계 계획</h3>
  <table>
    <tr><th style="width:34mm">대상 직무</th><th style="width:26mm">후보 인력</th><th>육성 계획 (교육 · OJT · 자격취득)</th><th style="width:26mm">목표 시기</th></tr>
    <tr><td class="hh" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="hh" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="hh" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="hh" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">3. 인력 운영 계획</h3>
  <table>
    <tr><th style="width:30mm">구분</th><th>당해연도</th><th>차년도</th><th>차차년도</th></tr>
    <tr><td class="lb">현원</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">채용 계획</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">퇴직 예상</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <div class="note"><b>공백 위험도</b> — 高(대체 인력 없음) / 中(부분 대체 가능) / 低(즉시 대체 가능). 高 등급 직무는 반드시 2항에 육성 계획을 기재하십시오.</div>

  <div class="foot"><span>«CO_FULL»</span><span>IMP-R-04 · 문항 17</span></div>
</div>""",
},
{
 "docno": 'IMP-O-01',
 "title": '조직도',
 "loc": '게시 위치: 사무실 주 출입구',
 "qs": [18, 19],
 "posted": True,
 "html": r"""<div class="page">
  <div class="dochead">
    <div><div class="co">«CO_FULL»</div><div class="ttl">조직도</div></div><button class="pbtn" onclick="printOne(this)">이 문서만 인쇄</button>
    <div class="meta">문서번호 <b>IMP-O-01</b><br>기준일 20&nbsp;&nbsp;&nbsp;.&nbsp;&nbsp;&nbsp;.&nbsp;&nbsp;&nbsp;.<br>게시용</div>
  </div>

  <div style="flex:1;display:flex;flex-direction:column;justify-content:center">
    <table style="width:100%">
      <tr><th colspan="5" style="font-size:12pt;padding:5mm;background:#0F1E3D;color:#fff">대표이사</th></tr>
      <tr><td colspan="5" style="border:none;text-align:center;padding:0;color:#B8942E;font-size:14pt" contenteditable="true" spellcheck="false">│</td></tr>
      <tr>
        <th style="width:20%;padding:4mm;font-size:10.5pt">영업부</th>
        <th style="width:20%;padding:4mm;font-size:10.5pt">생산부</th>
        <th style="width:20%;padding:4mm;font-size:10.5pt">품질관리부</th>
        <th style="width:20%;padding:4mm;font-size:10.5pt">관리부</th>
        <th style="width:20%;padding:4mm;font-size:10.5pt"><span class="ed" contenteditable="true" spellcheck="false" data-ph=""></span></th>
      </tr>
      <tr>
        <td style="height:52mm;vertical-align:top;padding:3mm" contenteditable="true" spellcheck="false" data-ph="부서장 / 담당자 / 담당자"></td>
        <td style="vertical-align:top;padding:3mm" contenteditable="true" spellcheck="false" data-ph="부서장 / 담당자 / 담당자"></td>
        <td style="vertical-align:top;padding:3mm" contenteditable="true" spellcheck="false" data-ph="부서장 / 담당자"></td>
        <td style="vertical-align:top;padding:3mm" contenteditable="true" spellcheck="false" data-ph="부서장 / 담당자"></td>
        <td style="vertical-align:top;padding:3mm" contenteditable="true" spellcheck="false"></td>
      </tr>
      <tr>
        <th style="font-size:8.5pt">&nbsp;&nbsp;&nbsp;명</th><th style="font-size:8.5pt">&nbsp;&nbsp;&nbsp;명</th>
        <th style="font-size:8.5pt">&nbsp;&nbsp;&nbsp;명</th><th style="font-size:8.5pt">&nbsp;&nbsp;&nbsp;명</th><th style="font-size:8.5pt">&nbsp;&nbsp;&nbsp;명</th>
      </tr>
    </table>

    <table style="margin-top:8mm">
      <tr><th style="width:34mm">총 인원</th><td style="width:30mm" class="h" contenteditable="true" spellcheck="false"></td>
          <th style="width:34mm">최종 개정일</th><td contenteditable="true" spellcheck="false"></td></tr>
      <tr><th>개정 사유</th><td colspan="3" class="h" contenteditable="true" spellcheck="false"></td></tr>
    </table>
  </div>

  <div class="note">
    <b>문항 19번</b> — '최신 상태로 관리'가 요건입니다. 인원 변동 시 <b>즉시 갱신 + 개정일 기재</b>가 핵심이며,
    개정 이력이 없는 조직도는 '계획' 등급으로 떨어집니다. 부서 구성은 실제에 맞게 수정해 사용하십시오.
  </div>

  <div class="foot"><span>게시 위치: 사무실 주 출입구</span><span>IMP-O-01 · 문항 18 · 19</span></div>
</div>""",
},
{
 "docno": 'IMP-O-02',
 "title": '업무분장표',
 "loc": '게시 위치: 각 부서 게시판',
 "qs": [19],
 "posted": True,
 "html": r"""<div class="page">
  <table class="sign">
    <tr><th>작성</th><th>승인</th></tr>
    <tr><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>
  <div class="dochead">
    <div><div class="co">«CO_FULL»</div><div class="ttl">업무분장표</div></div><button class="pbtn" onclick="printOne(this)">이 문서만 인쇄</button>
  </div>
  <div style="font-size:8pt;color:#5A6472;text-align:right;margin:-3mm 0 4mm">
    문서번호 <b style="color:#B8942E">IMP-O-02</b> &nbsp;|&nbsp; 기준일 20&nbsp;&nbsp;.&nbsp;&nbsp;.&nbsp;&nbsp;. &nbsp;|&nbsp; 게시용
  </div>

  <table>
    <tr>
      <th style="width:22mm">부서</th><th style="width:22mm">직위</th><th style="width:24mm">성명</th>
      <th>담당 업무</th><th style="width:26mm">대리 담당자</th>
    </tr>
    <tr><td class="lb" rowspan="3">영업부</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb" rowspan="4">생산부</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb" rowspan="2">품질관리부</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb" rowspan="3">관리부</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb" rowspan="2"><span class="ed" contenteditable="true" spellcheck="false" data-ph=""></span></td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">개정 이력</h3>
  <table>
    <tr><th style="width:26mm">개정일</th><th style="width:20mm">차수</th><th>개정 내용</th><th style="width:24mm">승인자</th></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <div class="note"><b>대리 담당자 칸</b>은 담당자 부재 시 업무 공백을 막는 장치로, 평가 시 <b>조직 관리 성숙도</b>를 보여주는 항목입니다. 비워두지 마십시오.</div>

  <div class="foot"><span>게시 위치: 각 부서 게시판</span><span>IMP-O-02 · 문항 19</span></div>
</div>""",
},
{
 "docno": 'IMP-O-03',
 "title": '조직개편 전 · 후 대비표 및 공지문',
 "loc": '게시 위치: 사무실 주 출입구',
 "qs": [18],
 "posted": True,
 "html": r"""<div class="page">
  <table class="sign">
    <tr><th>작성</th><th>승인</th></tr>
    <tr><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>
  <div class="dochead">
    <div><div class="co">«CO_FULL»</div><div class="ttl">조직개편 전 · 후 대비표 및 공지문</div></div><button class="pbtn" onclick="printOne(this)">이 문서만 인쇄</button>
  </div>
  <div style="font-size:8pt;color:#5A6472;text-align:right;margin:-3mm 0 4mm">
    문서번호 <b style="color:#B8942E">IMP-O-03</b> &nbsp;|&nbsp; 시행일 20&nbsp;&nbsp;.&nbsp;&nbsp;.&nbsp;&nbsp;.
  </div>

  <h3 class="sub">1. 개편 배경 및 목적</h3>
  <table><tr><td class="hhh" contenteditable="true" spellcheck="false"></td></tr></table>

  <h3 class="sub">2. 개편 전 · 후 비교</h3>
  <table>
    <tr><th style="width:26mm">구분</th><th style="width:37%">개편 전</th><th>개편 후</th></tr>
    <tr><td class="lb">조직 구성</td><td class="hhh" style="height:30mm" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">부서 수 · 인원</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">주요 변경 직무</td><td class="hh" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">보고 체계</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">3. 기대 효과</h3>
  <table><tr><td class="hh" contenteditable="true" spellcheck="false"></td></tr></table>

  <div class="sec" style="margin-top:6mm">사&nbsp;내&nbsp;공&nbsp;지<span>게시판 부착용</span></div>
  <table>
    <tr><td class="lb">제목</td><td contenteditable="true" spellcheck="false">조직개편 시행 안내</td></tr>
    <tr><td class="lb">시행일</td><td contenteditable="true" spellcheck="false">20&nbsp;&nbsp;&nbsp;년 &nbsp;&nbsp;&nbsp;월 &nbsp;&nbsp;&nbsp;일</td></tr>
    <tr><td class="lb">공지 내용</td><td class="hhh" style="height:32mm" contenteditable="true" spellcheck="false" data-ph="개편 내용 요약 · 직원 협조 요청 사항"></td></tr>
    <tr><td class="lb">공지자</td><td contenteditable="true" spellcheck="false">«CO_FULL» 대표이사 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (인)</td></tr>
  </table>

  <div class="note"><b>문항 18번</b> — 최근 3년 내 실적이어야 합니다. 대규모 개편이 없었다면 <b>직무 재설계</b>(업무분장 재조정 · 겸직 정리 · 신규 직무 신설)로 갈음할 수 있으며, 이 양식에 그 내용을 기재하면 됩니다.</div>

  <div class="foot"><span>게시 위치: 사무실 주 출입구</span><span>IMP-O-03 · 문항 18</span></div>
</div>""",
},
{
 "docno": 'IMP-O-04',
 "title": '인사평가표',
 "loc": '보존연한 3년 · 대외비',
 "qs": [20],
 "posted": False,
 "html": r"""<div class="page">
  <table class="sign">
    <tr><th>1차<br>평가</th><th>2차<br>평가</th><th>확인</th></tr>
    <tr><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>
  <div class="dochead">
    <div><div class="co">«CO_FULL»</div><div class="ttl">인사평가표</div></div><button class="pbtn" onclick="printOne(this)">이 문서만 인쇄</button>
  </div>
  <div style="font-size:8pt;color:#5A6472;text-align:right;margin:-3mm 0 4mm">
    문서번호 <b style="color:#B8942E">IMP-O-04</b> &nbsp;|&nbsp; 평가기간 20&nbsp;&nbsp;.&nbsp;&nbsp;. ~ 20&nbsp;&nbsp;.&nbsp;&nbsp;.
  </div>

  <table>
    <tr><td class="lb">부서</td><td style="width:44mm" contenteditable="true" spellcheck="false"></td><td class="lb">직위</td><td style="width:32mm" contenteditable="true" spellcheck="false"></td><td class="lb">성명</td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">입사일</td><td contenteditable="true" spellcheck="false"></td><td class="lb">담당 업무</td><td colspan="3" contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">1. 업적 평가 <span class="guide" style="font-weight:400">(60점)</span></h3>
  <table>
    <tr><th style="width:44mm">평가 항목</th><th style="width:34mm">목표</th><th style="width:34mm">실적</th><th style="width:20mm">배점</th><th style="width:20mm">획득</th><th>평가 근거</th></tr>
    <tr><td class="lb">핵심 목표 1</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td class="c" contenteditable="true" spellcheck="false">20</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">핵심 목표 2</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td class="c" contenteditable="true" spellcheck="false">20</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">핵심 목표 3</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td class="c" contenteditable="true" spellcheck="false">20</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">2. 역량 평가 <span class="guide" style="font-weight:400">(40점)</span></h3>
  <table>
    <tr><th style="width:44mm">평가 항목</th><th>평가 기준</th><th style="width:20mm">배점</th><th style="width:20mm">획득</th></tr>
    <tr><td class="lb">직무 전문성</td><td class="h" contenteditable="true" spellcheck="false" data-ph="담당 업무 지식 · 숙련도"></td><td class="c" contenteditable="true" spellcheck="false">10</td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">책임감 · 성실성</td><td class="h" contenteditable="true" spellcheck="false" data-ph="근태 · 업무 완결성"></td><td class="c" contenteditable="true" spellcheck="false">10</td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">협업 · 소통</td><td class="h" contenteditable="true" spellcheck="false" data-ph="부서 내외 협조"></td><td class="c" contenteditable="true" spellcheck="false">10</td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">개선 · 혁신 기여</td><td class="h" contenteditable="true" spellcheck="false" data-ph="제안 건수 · 개선 활동 참여"></td><td class="c" contenteditable="true" spellcheck="false">10</td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">3. 종합 결과</h3>
  <table>
    <tr><th style="width:30mm">업적</th><th style="width:30mm">역량</th><th style="width:30mm">합계</th><th style="width:30mm">등급</th><th>반영 사항</th></tr>
    <tr><td class="h c" contenteditable="true" spellcheck="false"></td><td class="c" contenteditable="true" spellcheck="false"></td><td class="c" contenteditable="true" spellcheck="false"></td><td class="c" contenteditable="true" spellcheck="false"></td><td class="c" contenteditable="true" spellcheck="false" data-ph="승진 / 성과급 / 교육"></td></tr>
  </table>

  <h3 class="sub">4. 평가자 의견 및 피평가자 확인</h3>
  <table>
    <tr><td class="lb">평가자 의견</td><td class="hhh" contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">본인 확인</td><td contenteditable="true" spellcheck="false">20&nbsp;&nbsp;&nbsp;.&nbsp;&nbsp;&nbsp;.&nbsp;&nbsp;&nbsp;. &nbsp;&nbsp; 성명 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (서명)</td></tr>
  </table>

  <div class="note"><b>문항 20번 핵심</b> — <b>'작성된 평가 결과물'</b>이 있어야 합니다. 양식만 있고 실제 작성본이 없으면 '계획' 등급입니다. 최소 <b>전 직원 1회분</b>은 작성해 두십시오. 등급: S(90↑) A(80↑) B(70↑) C(60↑) D(60미만)</div>

  <div class="foot"><span>보존연한 3년 · 대외비</span><span>IMP-O-04 · 문항 20</span></div>
</div>""",
},
{
 "docno": 'IMP-O-05',
 "title": '성과연동 보상 · 인센티브 지급대장',
 "loc": '보존연한 5년 · 대외비',
 "qs": [21],
 "posted": False,
 "html": r"""<div class="page">
  <table class="sign">
    <tr><th>작성</th><th>승인</th></tr>
    <tr><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>
  <div class="dochead">
    <div><div class="co">«CO_FULL»</div><div class="ttl">성과연동 보상 · 인센티브 지급대장</div></div><button class="pbtn" onclick="printOne(this)">이 문서만 인쇄</button>
  </div>
  <div style="font-size:8pt;color:#5A6472;text-align:right;margin:-3mm 0 4mm">
    문서번호 <b style="color:#B8942E">IMP-O-05</b> &nbsp;|&nbsp; 20&nbsp;&nbsp;&nbsp;년도 &nbsp;|&nbsp; 단위: 원
  </div>

  <h3 class="sub">1. 지급 기준</h3>
  <table>
    <tr><th style="width:26mm">평가 등급</th><th style="width:34mm">지급률 (기본급 대비)</th><th style="width:30mm">대상 인원</th><th>비고</th></tr>
    <tr><td class="lb">S</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">A</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">B</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">C 이하</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">2. 지급 내역</h3>
  <table>
    <tr>
      <th style="width:11mm">No</th><th style="width:24mm">부서</th><th style="width:24mm">성명</th>
      <th style="width:20mm">평가등급</th><th style="width:30mm">산정 근거</th><th style="width:28mm">지급액</th>
      <th style="width:24mm">지급일</th><th>수령 확인</th>
    </tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">1</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">2</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">3</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">4</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">5</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">6</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">7</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">8</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">9</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">10</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c" style="background:#EDF0F4" colspan="5" contenteditable="true" spellcheck="false"><b>합계</b></td><td class="h" style="background:#F6F8FA" contenteditable="true" spellcheck="false"></td><td style="background:#F6F8FA" contenteditable="true" spellcheck="false"></td><td style="background:#F6F8FA" contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <div class="note"><b>문항 21번</b> — '성과와 연동'이 핵심입니다. 전 직원 균등 지급이면 인정되지 않습니다. <b>평가등급별 차등</b>이 대장에서 눈으로 확인되어야 하며, 급여대장 · 이체증과 대조 가능해야 합니다.</div>

  <div class="foot"><span>보존연한 5년 · 대외비</span><span>IMP-O-05 · 문항 21</span></div>
</div>""",
},
{
 "docno": 'IMP-P-01',
 "title": '제품 · 서비스 개선 전 · 후 비교표',
 "loc": '주식회사 아이엠팩',
 "qs": [24],
 "posted": False,
 "html": r"""<div class="page">
  <table class="sign">
    <tr><th>작성</th><th>검토</th><th>승인</th></tr>
    <tr><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>
  <div class="dochead">
    <div><div class="co">«CO_FULL»</div><div class="ttl">제품 · 서비스 개선 전 · 후 비교표</div></div><button class="pbtn" onclick="printOne(this)">이 문서만 인쇄</button>
  </div>
  <div style="font-size:8pt;color:#5A6472;text-align:right;margin:-3mm 0 4mm">
    문서번호 <b style="color:#B8942E">IMP-P-01</b> &nbsp;|&nbsp; 개선번호 IMP-&nbsp;&nbsp;-&nbsp;&nbsp;&nbsp;
  </div>

  <table>
    <tr><td class="lb">대상 제품</td><td style="width:56mm" contenteditable="true" spellcheck="false"></td><td class="lb">개선 기간</td><td contenteditable="true" spellcheck="false">20&nbsp;&nbsp;.&nbsp;&nbsp;. ~ 20&nbsp;&nbsp;.&nbsp;&nbsp;.</td></tr>
    <tr><td class="lb">개선 담당</td><td contenteditable="true" spellcheck="false"></td><td class="lb">투입 비용</td><td contenteditable="true" spellcheck="false">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 천원</td></tr>
    <tr><td class="lb">개선 배경</td><td colspan="3" class="hh" contenteditable="true" spellcheck="false" data-ph="고객 클레임 / 불량 발생 / 원가 부담 / 경쟁사 대응 등"></td></tr>
  </table>

  <h3 class="sub">개선 전 · 후 수치 비교</h3>
  <table>
    <tr><th style="width:38mm">비교 항목</th><th style="width:30mm">개선 전</th><th style="width:30mm">개선 후</th><th style="width:24mm">개선율</th><th>측정 방법 · 근거</th></tr>
    <tr><td class="lb">불량률</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">단위 원가</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">생산 소요시간</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">성능 · 규격</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">클레임 건수</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">고객 만족도</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">개선 내용 및 사진</h3>
  <table>
    <tr><th style="width:50%">개선 전</th><th>개선 후</th></tr>
    <tr><td style="height:46mm" class="c" contenteditable="true" spellcheck="false" data-ph="사진 부착"></td><td class="c" contenteditable="true" spellcheck="false" data-ph="사진 부착"></td></tr>
    <tr><td class="hh" contenteditable="true" spellcheck="false" data-ph="문제점 서술"></td><td class="hh" contenteditable="true" spellcheck="false" data-ph="개선 내용 서술"></td></tr>
  </table>

  <div class="note"><b>문항 24번 핵심</b> — '개선 전 · 후를 <b>수치</b>로 관리'가 요건입니다. 정성적 서술만 있으면 '계획' 등급입니다. 표의 <b>숫자 칸을 반드시 채우고</b>, 최근 3년 내 개선 사례를 <b>3건 이상</b> 확보하십시오.</div>

  <div class="foot"><span>«CO_FULL»</span><span>IMP-P-01 · 문항 24</span></div>
</div>""",
},
{
 "docno": 'IMP-P-02',
 "title": '고객 요구사항 접수 · 반영 대장',
 "loc": '주식회사 아이엠팩',
 "qs": [25, 46],
 "posted": False,
 "html": r"""<div class="page">
  <div class="dochead">
    <div><div class="co">«CO_FULL»</div><div class="ttl">고객 요구사항 접수 · 반영 대장</div></div><button class="pbtn" onclick="printOne(this)">이 문서만 인쇄</button>
    <div class="meta">문서번호 <b>IMP-P-02</b><br>20&nbsp;&nbsp;&nbsp;년도</div>
  </div>

  <table>
    <tr>
      <th style="width:11mm">No</th><th style="width:22mm">접수일</th><th style="width:26mm">고객사</th>
      <th style="width:20mm">접수 경로</th><th>요구 · 불만 내용</th><th style="width:44mm">조치 내용</th>
      <th style="width:22mm">완료일</th><th style="width:20mm">고객<br>확인</th>
    </tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">1</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">2</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">3</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">4</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">5</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">6</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">7</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">8</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">9</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">10</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">11</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">12</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">13</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">14</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">처리 현황 집계 <span class="guide" style="font-weight:400">(문항 46번 클레임 감소 추세 증빙 겸용)</span></h3>
  <table>
    <tr><th style="width:30mm">구분</th><th>1분기</th><th>2분기</th><th>3분기</th><th>4분기</th><th style="width:24mm">합계</th></tr>
    <tr><td class="lb">접수 건수</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">완료 건수</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">평균 처리일</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <div class="note"><b>접수 경로</b> — 전화 / 이메일 / 방문 / 영업담당 로 구분 기재. 클레임이 <b>감소 추세</b>로 나타나면 문항 46번(양호 → 우수) 상향에도 직접 활용됩니다.</div>

  <div class="foot"><span>«CO_FULL»</span><span>IMP-P-02 · 문항 25 · 46</span></div>
</div>""",
},
{
 "docno": 'IMP-P-03',
 "title": '공정흐름도',
 "loc": '게시 위치: 생산 현장 주 통로',
 "qs": [29],
 "posted": True,
 "html": r"""<div class="page">
  <div class="dochead">
    <div><div class="co">«CO_FULL»</div><div class="ttl">공정흐름도</div></div><button class="pbtn" onclick="printOne(this)">이 문서만 인쇄</button>
    <div class="meta">문서번호 <b>IMP-P-03</b><br>제정 20&nbsp;&nbsp;.&nbsp;&nbsp;.&nbsp;&nbsp;.<br>게시용</div>
  </div>

  <table>
    <tr>
      <th style="width:11mm">순서</th><th style="width:34mm">공정명</th><th>공정 내용</th>
      <th style="width:26mm">사용 설비</th><th style="width:24mm">담당</th><th style="width:34mm">관리 포인트 · 기준</th><th style="width:22mm">검사<br>여부</th>
    </tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">1</td><td contenteditable="true" spellcheck="false" data-ph="수주 · 발주"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">2</td><td contenteditable="true" spellcheck="false" data-ph="자재 입고 · 검사"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">3</td><td contenteditable="true" spellcheck="false" data-ph="생산 준비"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">4</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">5</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">6</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">7</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">8</td><td contenteditable="true" spellcheck="false" data-ph="중간 검사"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">9</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">10</td><td contenteditable="true" spellcheck="false" data-ph="최종 검사"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">11</td><td contenteditable="true" spellcheck="false" data-ph="포장 · 출하"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">부적합품 처리 흐름</h3>
  <table>
    <tr><th style="width:30mm">발생 단계</th><th style="width:34mm">판정 기준</th><th style="width:34mm">처리 방법</th><th>재발 방지 조치</th></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false" data-ph="재작업 / 특채 / 폐기"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <div class="note"><b>게시 필수</b> — 공정흐름도는 <b>현장에 크게 출력해 부착</b>하는 것이 원칙입니다. 현장평가 시 평가위원이 가장 먼저 확인하는 문서이며, 실제 라인과 일치해야 합니다.</div>

  <div class="foot"><span>게시 위치: 생산 현장 주 통로</span><span>IMP-P-03 · 문항 29</span></div>
</div>""",
},
{
 "docno": 'IMP-P-04',
 "title": '표준작업지침서 (SOP)',
 "loc": '게시 위치: 해당 공정 설비 옆',
 "qs": [29],
 "posted": True,
 "html": r"""<div class="page">
  <table class="sign">
    <tr><th>작성</th><th>검토</th><th>승인</th></tr>
    <tr><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>
  <div class="dochead">
    <div><div class="co">«CO_FULL»</div><div class="ttl">표준작업지침서 (SOP)</div></div><button class="pbtn" onclick="printOne(this)">이 문서만 인쇄</button>
  </div>
  <div style="font-size:8pt;color:#5A6472;text-align:right;margin:-3mm 0 4mm">
    문서번호 <b style="color:#B8942E">IMP-P-04-&nbsp;&nbsp;&nbsp;</b> &nbsp;|&nbsp; 제정 20&nbsp;&nbsp;.&nbsp;&nbsp;.&nbsp;&nbsp;. &nbsp;|&nbsp; 개정 &nbsp;&nbsp;차
  </div>

  <table>
    <tr><td class="lb">공정명</td><td style="width:56mm" contenteditable="true" spellcheck="false"></td><td class="lb">적용 설비</td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">작업 목적</td><td colspan="3" class="h" contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">필요 인원</td><td contenteditable="true" spellcheck="false"></td><td class="lb">표준 소요시간</td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">안전 장비</td><td colspan="3" contenteditable="true" spellcheck="false" data-ph="보안경 · 안전화 · 방진마스크 · 절단방지 장갑 등"></td></tr>
  </table>

  <h3 class="sub">1. 작업 순서</h3>
  <table>
    <tr><th style="width:12mm">순서</th><th>작업 내용</th><th style="width:38mm">관리 기준 (수치)</th><th style="width:36mm">주의사항 · 안전</th></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">1</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">2</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">3</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">4</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">5</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">6</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">7</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">8</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">2. 이상 발생 시 조치</h3>
  <table>
    <tr><th style="width:44mm">이상 현상</th><th style="width:52mm">원인</th><th>조치 방법</th></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">3. 개정 이력</h3>
  <table>
    <tr><th style="width:22mm">차수</th><th style="width:26mm">개정일</th><th>개정 사유 및 내용</th><th style="width:24mm">승인</th></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <div class="note"><b>작성 범위</b> — 이 양식을 복사해 <b>주요 공정 5~10개</b>에 대해 각각 작성하십시오(IMP-P-04-01, -02 …). 완성본은 <b>해당 설비 옆에 코팅해 부착</b>하면 문항 29번이 '체계' 등급으로 확정됩니다.</div>

  <div class="foot"><span>게시 위치: 해당 공정 설비 옆</span><span>IMP-P-04 · 문항 29</span></div>
</div>""",
},
{
 "docno": 'IMP-P-05',
 "title": '품질검사 성적서 · 불량률 관리표',
 "loc": '게시 위치: 생산 현장 · 품질관리실',
 "qs": [30],
 "posted": True,
 "html": r"""<div class="page">
  <table class="sign">
    <tr><th>검사</th><th>승인</th></tr>
    <tr><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>
  <div class="dochead">
    <div><div class="co">«CO_FULL»</div><div class="ttl">품질검사 성적서 · 불량률 관리표</div></div><button class="pbtn" onclick="printOne(this)">이 문서만 인쇄</button>
  </div>
  <div style="font-size:8pt;color:#5A6472;text-align:right;margin:-3mm 0 4mm">
    문서번호 <b style="color:#B8942E">IMP-P-05</b> &nbsp;|&nbsp; 게시용
  </div>

  <h3 class="sub">1. 품질검사 기준</h3>
  <table>
    <tr><th style="width:30mm">검사 구분</th><th style="width:38mm">검사 항목</th><th style="width:34mm">규격 · 합격 기준</th><th style="width:26mm">검사 방법</th><th style="width:22mm">주기</th><th>담당</th></tr>
    <tr><td class="lb">수입 검사</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">공정 검사</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">최종 검사</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">출하 검사</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">2. 월별 불량률 추이 <span class="guide" style="font-weight:400">(단위: %)</span></h3>
  <table>
    <tr><th style="width:24mm">구분</th><th>1월</th><th>2월</th><th>3월</th><th>4월</th><th>5월</th><th>6월</th><th>7월</th><th>8월</th><th>9월</th><th>10월</th><th>11월</th><th>12월</th></tr>
    <tr><td class="lb">목표</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">실적</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">전년 동월</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">3. 주요 불량 유형 및 개선 조치</h3>
  <table>
    <tr><th style="width:11mm">No</th><th style="width:40mm">불량 유형</th><th style="width:22mm">발생 건수</th><th style="width:20mm">비중</th><th>원인 분석</th><th style="width:44mm">개선 조치</th></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">1</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">2</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">3</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">4</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">5</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <div class="note"><b>문항 30번</b> — '검사 기준 + 불량률 관리 체계'가 함께 있어야 합니다. 2번 표는 <b>현장 게시판에 확대 부착</b>하고 매월 손으로 채워 나가면 관리 흔적이 가장 확실하게 남습니다.</div>

  <div class="foot"><span>게시 위치: 생산 현장 · 품질관리실</span><span>IMP-P-05 · 문항 30</span></div>
</div>""",
},
{
 "docno": 'IMP-P-06',
 "title": '원가절감 실적 관리표',
 "loc": '주식회사 아이엠팩',
 "qs": [31],
 "posted": False,
 "html": r"""<div class="page">
  <table class="sign">
    <tr><th>작성</th><th>검토</th><th>승인</th></tr>
    <tr><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>
  <div class="dochead">
    <div><div class="co">«CO_FULL»</div><div class="ttl">원가절감 실적 관리표</div></div><button class="pbtn" onclick="printOne(this)">이 문서만 인쇄</button>
  </div>
  <div style="font-size:8pt;color:#5A6472;text-align:right;margin:-3mm 0 4mm">
    문서번호 <b style="color:#B8942E">IMP-P-06</b> &nbsp;|&nbsp; 20&nbsp;&nbsp;&nbsp;년도 &nbsp;|&nbsp; 단위: 천원
  </div>

  <table>
    <tr>
      <th style="width:11mm">No</th><th style="width:40mm">절감 과제</th><th style="width:22mm">구분</th>
      <th style="width:26mm">개선 전 원가</th><th style="width:26mm">개선 후 원가</th><th style="width:24mm">단위 절감액</th>
      <th style="width:22mm">연간 수량</th><th style="width:26mm">연간 절감액</th><th>산출 근거</th>
    </tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">1</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false" data-ph="재료비"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">2</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false" data-ph="노무비"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">3</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false" data-ph="경비"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">4</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">5</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">6</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">7</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">8</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td colspan="7" class="c" style="background:#EDF0F4" contenteditable="true" spellcheck="false"><b>연간 절감액 합계</b></td><td class="h" style="background:#F6F8FA" contenteditable="true" spellcheck="false"></td><td style="background:#F6F8FA" contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">분기별 절감 실적 추이</h3>
  <table>
    <tr><th style="width:30mm">구분</th><th>1분기</th><th>2분기</th><th>3분기</th><th>4분기</th><th style="width:26mm">누계</th></tr>
    <tr><td class="lb">목표 절감액</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">실제 절감액</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">달성률</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">매출액 대비</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <div class="note"><b>문항 31번 핵심</b> — '절감액을 <b>산출 · 관리</b>'가 요건입니다. 활동만 하고 금액 산출이 없으면 '계획' 등급입니다. <b>산출 근거</b> 칸을 반드시 채우십시오(예: "포장재 단가 120원→95원 × 연 40만개").</div>

  <div class="foot"><span>«CO_FULL»</span><span>IMP-P-06 · 문항 31</span></div>
</div>""",
},
{
 "docno": 'IMP-P-07',
 "title": '납기 · 리드타임 성과 관리표',
 "loc": '게시 위치: 생산 현장 · 영업부',
 "qs": [32],
 "posted": True,
 "html": r"""<div class="page">
  <div class="dochead">
    <div><div class="co">«CO_FULL»</div><div class="ttl">납기 · 리드타임 성과 관리표</div></div><button class="pbtn" onclick="printOne(this)">이 문서만 인쇄</button>
    <div class="meta">문서번호 <b>IMP-P-07</b><br>20&nbsp;&nbsp;&nbsp;년도<br>게시용</div>
  </div>

  <h3 class="sub">1. 월별 납기준수율</h3>
  <table>
    <tr><th style="width:28mm">구분</th><th>1월</th><th>2월</th><th>3월</th><th>4월</th><th>5월</th><th>6월</th><th>7월</th><th>8월</th><th>9월</th><th>10월</th><th>11월</th><th>12월</th></tr>
    <tr><td class="lb">총 납품 건수</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">지연 건수</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">납기준수율(%)</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">목표(%)</td><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">2. 리드타임 추이 <span class="guide" style="font-weight:400">(수주 → 출하, 단위: 일)</span></h3>
  <table>
    <tr><th style="width:34mm">제품군</th><th style="width:28mm">전전년</th><th style="width:28mm">전년</th><th style="width:28mm">당해년</th><th style="width:24mm">단축률</th><th>단축 요인</th></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">3. 납기 지연 사례 및 재발 방지</h3>
  <table>
    <tr><th style="width:22mm">발생일</th><th style="width:28mm">고객사</th><th style="width:20mm">지연 일수</th><th>지연 원인</th><th style="width:46mm">재발 방지 대책</th></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="h" contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <div class="note"><b>문항 32번</b> — '성과가 <b>수치로 관리</b>'가 요건이며, 현재 '부분' 등급입니다. 리드타임 3개년 추이(2번 표)에서 <b>단축 흐름</b>이 보이면 '체계'로 상향됩니다.</div>

  <div class="foot"><span>게시 위치: 생산 현장 · 영업부</span><span>IMP-P-07 · 문항 32</span></div>
</div>""",
},
{
 "docno": 'IMP-M-01',
 "title": '전시회 · 박람회 참가 상담일지',
 "loc": '주식회사 아이엠팩',
 "qs": [37],
 "posted": False,
 "html": r"""<div class="page">
  <table class="sign">
    <tr><th>작성</th><th>승인</th></tr>
    <tr><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>
  <div class="dochead">
    <div><div class="co">«CO_FULL»</div><div class="ttl">전시회 · 박람회 참가 상담일지</div></div><button class="pbtn" onclick="printOne(this)">이 문서만 인쇄</button>
  </div>
  <div style="font-size:8pt;color:#5A6472;text-align:right;margin:-3mm 0 4mm">
    문서번호 <b style="color:#B8942E">IMP-M-01</b>
  </div>

  <table>
    <tr><td class="lb">전시회명</td><td colspan="3" class="h" contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">기간</td><td style="width:52mm" contenteditable="true" spellcheck="false">20&nbsp;&nbsp;.&nbsp;&nbsp;.&nbsp;&nbsp;. ~ 20&nbsp;&nbsp;.&nbsp;&nbsp;.&nbsp;&nbsp;.</td>
        <td class="lb">장소 · 부스</td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="lb">참가 인원</td><td contenteditable="true" spellcheck="false"></td><td class="lb">참가 비용</td><td contenteditable="true" spellcheck="false">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 천원</td></tr>
    <tr><td class="lb">참가 목적</td><td colspan="3" class="h" contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">상담 내역</h3>
  <table>
    <tr>
      <th style="width:11mm">No</th><th style="width:22mm">일자</th><th style="width:34mm">상담 업체</th>
      <th style="width:26mm">담당자 · 연락처</th><th>상담 내용 · 관심 품목</th><th style="width:22mm">등급</th><th style="width:32mm">후속 조치</th>
    </tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">1</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">2</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">3</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">4</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">5</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">6</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">7</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">8</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">9</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><td class="c h" contenteditable="true" spellcheck="false">10</td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td><td contenteditable="true" spellcheck="false"></td></tr>
  </table>

  <h3 class="sub">참가 성과 및 사진</h3>
  <table>
    <tr><th style="width:34mm">상담 건수</th><td style="width:24mm" class="h" contenteditable="true" spellcheck="false"></td><th style="width:34mm">견적 요청 건수</th><td class="h" contenteditable="true" spellcheck="false"></td></tr>
    <tr><th>실제 수주 건수</th><td contenteditable="true" spellcheck="false"></td><th>수주 금액</th><td contenteditable="true" spellcheck="false"></td></tr>
    <tr><th>부스 사진</th><td colspan="3" style="height:40mm" class="c" contenteditable="true" spellcheck="false" data-ph="부스 전경 · 상담 장면 사진 2매 이상 부착"></td></tr>
  </table>

  <div class="note"><b>문항 37번</b> — '<b>정기적으로</b> 수행'이 요건입니다. 연 1~2회라도 <b>참가 계약서 + 부스 사진 + 상담일지</b> 세트가 3년치 누적되면 '체계' 등급입니다.</div>

  <div class="foot"><span>«CO_FULL»</span><span>IMP-M-01 · 문항 37</span></div>
</div>


<script>
(function(){
  var KEY = 'IMPACK_FORM_V1';
  var els = [];

  function collect(){
    els = Array.prototype.slice.call(
      document.querySelectorAll('[contenteditable="true"]')
    );
    els.forEach(function(el,i){ el.setAttribute('data-k','k'+i); });
  }

  function dump(){
    var o = {};
    els.forEach(function(el){
      var v = el.innerHTML.trim();
      if(v) o[el.getAttribute('data-k')] = v;
    });
    return o;
  }

  function apply(o){
    els.forEach(function(el){
      var k = el.getAttribute('data-k');
      if(o && o[k] !== undefined) el.innerHTML = o[k];
    });
  }

  function autosave(){
    try{ localStorage.setItem(KEY, JSON.stringify(dump())); status('자동 보관됨 · ' + time()); }
    catch(e){ status('자동 보관 불가 — [작성내용 저장] 버튼을 사용하세요'); }
  }

  function time(){
    var d = new Date();
    return ('0'+d.getHours()).slice(-2)+':'+('0'+d.getMinutes()).slice(-2);
  }
  function status(t){ var s=document.getElementById('st'); if(s) s.textContent=t; }

  var timer;
  document.addEventListener('input', function(e){
    if(!e.target.isContentEditable) return;
    clearTimeout(timer); timer = setTimeout(autosave, 600);
  });

  // 붙여넣기는 서식 없이
  document.addEventListener('paste', function(e){
    if(!e.target.isContentEditable) return;
    e.preventDefault();
    var t = (e.clipboardData||window.clipboardData).getData('text');
    document.execCommand('insertText', false, t);
  });

  // Tab 으로 다음 칸 이동
  document.addEventListener('keydown', function(e){
    if(e.key !== 'Tab' || !e.target.isContentEditable) return;
    e.preventDefault();
    var i = els.indexOf(e.target);
    var n = els[i + (e.shiftKey ? -1 : 1)];
    if(n){ n.focus(); n.scrollIntoView({block:'center', behavior:'smooth'}); }
  });

  window.jumpTo = function(id){
    if(!id) return;
    var el = document.getElementById(id);
    if(el) el.scrollIntoView({behavior:'smooth'});
  };

  window.printOne = function(btn){
    var pg = btn.closest('.page');
    pg.classList.add('only');
    document.body.classList.add('single');
    window.print();
    setTimeout(function(){
      pg.classList.remove('only');
      document.body.classList.remove('single');
    }, 400);
  };

  window.saveFile = function(){
    var blob = new Blob([JSON.stringify(dump(), null, 1)], {type:'application/json'});
    var a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = '«CO»_작성내용_' + new Date().toISOString().slice(0,10) + '.json';
    a.click();
    status('파일로 저장했습니다');
  };

  window.loadFile = function(ev){
    var f = ev.target.files[0];
    if(!f) return;
    var r = new FileReader();
    r.onload = function(){
      try{ apply(JSON.parse(r.result)); autosave(); status('불러왔습니다'); }
      catch(e){ status('파일을 읽을 수 없습니다'); }
    };
    r.readAsText(f);
    ev.target.value = '';
  };

  window.clearAll = function(){
    if(!confirm('작성한 내용을 모두 지웁니다. 계속할까요?')) return;
    els.forEach(function(el){ el.innerHTML = ''; });
    try{ localStorage.removeItem(KEY); }catch(e){}
    status('모두 지웠습니다');
  };

  collect();
  try{
    var s = localStorage.getItem(KEY);
    if(s){ apply(JSON.parse(s)); status('이전 작성내용을 불러왔습니다'); }
  }catch(e){
    status('자동 보관 불가 — 파일을 PC에 내려받아 여시면 자동 보관됩니다');
  }
})();
</script>""",
},
]
