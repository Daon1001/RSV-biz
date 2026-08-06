# -*- coding: utf-8 -*-
"""진단 결과 → RSV 디자인 A4 가로 컨설팅 리포트 HTML"""

from datetime import date
from questions import (SECTIONS, QUESTIONS, Q_BY_NO, SEC_BY_CODE, labels,
                       VERDICTS, DISQUALIFIERS, PART_NAME)
from forms_data import FORMS

NAVY = "#0F1E3D"
GOLD = "#B8942E"

CSS = r"""
@page { size: A4 landscape; margin: 0; }
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:"Pretendard","Malgun Gothic","맑은 고딕","Apple SD Gothic Neo",sans-serif;
 color:#1A1A1A;font-size:10pt;line-height:1.55;background:#8A8F98}
.pg{width:297mm;height:210mm;padding:14mm 16mm;margin:0 auto 8mm;background:#fff;
 page-break-after:always;position:relative;display:flex;flex-direction:column;overflow:hidden}
.pg:last-child{page-break-after:auto}
.hd{display:flex;justify-content:space-between;align-items:flex-end;
 border-bottom:2.2pt solid #0F1E3D;padding-bottom:3mm;margin-bottom:5mm}
.hd h2{font-size:16pt;color:#0F1E3D;font-weight:800;letter-spacing:-.5px}
.hd h2 small{color:#B8942E;font-size:9pt;font-weight:700;margin-left:3mm;letter-spacing:2px}
.hd .r{text-align:right;font-size:8pt;color:#5A6472;line-height:1.6}
.ft{margin-top:auto;padding-top:3mm;border-top:.5pt solid #C9CFD8;display:flex;
 justify-content:space-between;font-size:7.5pt;color:#8A929C}
table{width:100%;border-collapse:collapse;font-size:9pt}
th,td{border:.5pt solid #B4BCC7;padding:1.8mm 2mm}
th{background:#EDF0F4;color:#0F1E3D;font-weight:700;text-align:center;font-size:8.5pt}
td.l{background:#F6F8FA;font-weight:700;color:#0F1E3D}
.c{text-align:center}.r{text-align:right}
h3{font-size:10.5pt;color:#0F1E3D;font-weight:700;margin:4mm 0 2.5mm;
 border-left:3pt solid #B8942E;padding-left:2.5mm}
.note{background:#F6F8FA;border-left:3pt solid #B8942E;padding:3mm 4mm;font-size:8.5pt;
 color:#3C4655;line-height:1.7;margin-top:3mm}
.note b{color:#0F1E3D}

/* 표지 */
.cover{background:#0F1E3D;color:#fff;justify-content:center}
.cover .eb{font-size:9pt;letter-spacing:8px;color:#B8942E}
.cover h1{font-size:42pt;font-weight:800;margin:8mm 0 5mm;letter-spacing:-2px;line-height:1.15}
.cover .sub{font-size:14pt;color:#C3CBD6;line-height:2}
.cover .meta{position:absolute;bottom:16mm;left:16mm;right:16mm;display:flex;
 justify-content:space-between;font-size:9.5pt;color:#9FB0C8;
 border-top:.8pt solid #3A4A66;padding-top:4mm}

/* 스코어 */
.score{display:flex;gap:8mm;align-items:stretch}
.dial{width:86mm;background:#0F1E3D;color:#fff;border-radius:2mm;padding:7mm;text-align:center;
 display:flex;flex-direction:column;justify-content:center}
.dial .n{font-size:52pt;font-weight:800;line-height:1;letter-spacing:-3px}
.dial .n span{font-size:16pt;color:#8FA0BC;font-weight:400}
.dial .v{margin-top:5mm;font-size:13pt;font-weight:700;padding:2.5mm;border-radius:1mm}
.dial .d{margin-top:3mm;font-size:8.5pt;color:#B9C6D8;line-height:1.6}
.bars{flex:1}
.bar{margin-bottom:4.5mm}
.bar .t{display:flex;justify-content:space-between;font-size:9pt;margin-bottom:1.2mm}
.bar .t b{color:#0F1E3D}
.bar .t i{font-style:normal;color:#5A6472}
.track{height:6mm;background:#E8ECF1;border-radius:1mm;overflow:hidden;position:relative}
.fill{height:100%;background:linear-gradient(90deg,#0F1E3D,#2E4670)}
.fill.g{background:linear-gradient(90deg,#B8942E,#D8B454)}
.mark{position:absolute;top:0;bottom:0;width:1.2pt;background:#C0392B}

.kpi{display:flex;gap:4mm;margin-top:4mm}
.kpi div{flex:1;border:.8pt solid #C9CFD8;border-radius:1.5mm;padding:3.5mm;text-align:center}
.kpi div b{display:block;font-size:18pt;color:#0F1E3D;font-weight:800;letter-spacing:-1px}
.kpi div span{font-size:8pt;color:#6B7684}

.g0{color:#A83232}.g1{color:#C4711F}.g2{color:#1F6FB2}.g3{color:#1B7A4B;font-weight:700}
.pill{display:inline-block;padding:.4mm 2mm;border-radius:1mm;font-size:7.5pt;font-weight:700}
.p-hi{background:#FBE9E7;color:#A83232}
.p-md{background:#FFF4E0;color:#9A6B12}
.p-lo{background:#E9F3EC;color:#1B7A4B}
@media print{body{background:#fff}.pg{margin:0;box-shadow:none}}
"""


def _bar(name, got, alloc, gold=False):
    r = got / alloc if alloc else 0
    return f"""<div class="bar"><div class="t"><b>{name}</b>
<i>{got:,.1f} / {alloc} · {r*100:.0f}%</i></div>
<div class="track"><div class="fill{' g' if gold else ''}" style="width:{min(r,1)*100:.1f}%"></div></div></div>"""


def _hd(title, eyebrow, company, page):
    return f"""<div class="hd"><h2>{title}<small>{eyebrow}</small></h2>
<div class="r">{company}<br>메인비즈 경영혁신진단 · {date.today().strftime('%Y. %m. %d.')}</div></div>"""


def _ft(company, txt, page):
    return f"""<div class="ft"><span>RSV · 부자들의 비밀금고 &nbsp;|&nbsp; 중소기업경영지원단</span>
<span>{txt}</span><span>{page:02d}</span></div>"""


def build(company, result, answers, consultant="", ai_text="", memo=""):
    R, S = result, result["sections"]
    v = R["verdict"]
    total = R["total"]
    co = company.strip()
    pages = []

    # ── 표지
    pages.append(f"""<div class="pg cover">
  <div class="eb">MANAGEMENT INNOVATION DIAGNOSIS</div>
  <h1>경영혁신 진단<br>결과 보고서</h1>
  <div class="sub">{co}<br>총점 {total:,.0f}점 / 1,000점 · 판정 「{v['label']}」</div>
  <div class="meta"><span>진단일 {date.today().strftime('%Y년 %m월 %d일')}</span>
  <span>{'진단자 ' + consultant if consultant else ''}</span>
  <span>RSV · 부자들의 비밀금고</span></div>
</div>""")

    # ── 요약
    marks = "".join(
        f'<div class="mark" style="left:{p/1000*100:.1f}%"></div>' for p in (700, 780))
    parts = "".join(_bar(f"부문 {k} · {vv['name']}", vv["got"], vv["alloc"], k == "Ⅲ")
                    for k, vv in R["parts"].items())
    pages.append(f"""<div class="pg">
  {_hd("진단 결과 요약", "SUMMARY", co, 2)}
  <div class="score">
    <div class="dial">
      <div class="n">{total:,.0f}<span> / 1,000</span></div>
      <div class="v" style="background:{v['color']}">{v['label']}</div>
      <div class="d">{v['desc']}</div>
    </div>
    <div class="bars">
      <div class="bar"><div class="t"><b>총점</b><i>합격선 700 · 실무 목표 780</i></div>
        <div class="track"><div class="fill g" style="width:{min(total/1000,1)*100:.1f}%"></div>{marks}</div></div>
      {parts}
    </div>
  </div>
  <div class="kpi">
    <div><b>{R['gap700']:,.0f}점</b><span>신청 가능선(700)까지</span></div>
    <div><b>{R['gap780']:,.0f}점</b><span>실무 목표선(780)까지</span></div>
    <div><b>{sum(1 for a in answers.values() if int(a)==1)}문항</b><span>'계획' 단계 정체</span></div>
    <div><b>{sum(1 for a in answers.values() if int(a)==0)}문항</b><span>미구축 · 무응답</span></div>
    <div><b>{sum(1 for a in answers.values() if int(a)==3)}문항</b><span>체계 완비</span></div>
  </div>
  <div class="note">
    <b>판정 기준</b> — 780점 이상 즉시 신청 권장 &nbsp;|&nbsp; 700~779점 신청 가능(취약 부문 보완 후)
    &nbsp;|&nbsp; 600~699점 8~10주 보완 후 재진단 &nbsp;|&nbsp; 600점 미만 인프라 · 활동 구축부터 착수.
    온라인 자가진단은 600점이면 현장평가 신청이 가능하지만, <b>현장평가는 증빙으로 감점되는 구조</b>이므로
    780점을 실무 목표선으로 잡으십시오.
  </div>
  {_ft(co, "진단 결과 요약", 2)}
</div>""")

    # ── 구간별 상세
    rows = []
    for code, part, name, alloc, cnt, perf in SECTIONS:
        s = S[code]
        r = s["rate"]
        pill = "p-lo" if r >= .8 else ("p-md" if r >= .5 else "p-hi")
        lv = "양호" if r >= .8 else ("보통" if r >= .5 else "취약")
        rows.append(f"""<tr><td class="c">{code}</td><td class="l">{name}</td>
<td class="c">{cnt}</td><td class="c">{alloc}</td><td class="c"><b>{s['got']:,.1f}</b></td>
<td class="c">{s['lost']:,.1f}</td><td class="c">{r*100:.0f}%</td>
<td class="c"><span class="pill {pill}">{lv}</span></td>
<td><div class="track" style="height:4mm"><div class="fill{' g' if r>=.8 else ''}" style="width:{min(r,1)*100:.1f}%"></div></div></td></tr>""")

    pr = sorted(S.values(), key=lambda x: -x["lost"])[:3]
    prio = "".join(
        f'<tr><td class="c">{i+1}</td><td class="l">{p["code"]} {p["name"]}</td>'
        f'<td class="c">{p["lost"]:,.1f}점</td><td>{_advice(p["code"])}</td></tr>'
        for i, p in enumerate(pr))

    pages.append(f"""<div class="pg">
  {_hd("구간별 진단 결과", "BY SECTION", co, 3)}
  <table>
    <tr><th style="width:16mm">코드</th><th style="width:44mm">구간</th><th style="width:14mm">문항</th>
    <th style="width:16mm">배점</th><th style="width:18mm">획득</th><th style="width:18mm">실점</th>
    <th style="width:16mm">달성률</th><th style="width:18mm">평가</th><th>달성 수준</th></tr>
    {''.join(rows)}
    <tr><td class="c" colspan="3" style="background:#0F1E3D;color:#fff"><b>합계</b></td>
    <td class="c" style="background:#0F1E3D;color:#fff"><b>1,000</b></td>
    <td class="c" style="background:#0F1E3D;color:#fff"><b>{total:,.1f}</b></td>
    <td class="c" style="background:#0F1E3D;color:#fff"><b>{1000-total:,.1f}</b></td>
    <td class="c" style="background:#0F1E3D;color:#fff"><b>{total/10:.0f}%</b></td>
    <td colspan="2" style="background:#0F1E3D;color:#fff"></td></tr>
  </table>
  <h3>보완 우선순위 — 실점 규모 상위 3개 구간</h3>
  <table>
    <tr><th style="width:14mm">순위</th><th style="width:52mm">구간</th><th style="width:22mm">실점</th><th>보완 방향</th></tr>
    {prio}
  </table>
  <div class="note">{memo if memo else
    "실점 규모가 큰 구간부터 착수하는 것이 점수 효율이 가장 높습니다. "
    "특히 '계획' 등급에 정체된 문항은 대부분 <b>활동은 하고 있으나 증빙 문서가 없는</b> 경우로, "
    "문서 정비만으로 '체계' 등급 전환이 가능합니다."}</div>
  {_ft(co, "구간별 진단 결과", 3)}
</div>""")

    # ── 문항별 결과 (12문항씩 분할)
    N = 12
    chunks = [QUESTIONS[i:i + N] for i in range(0, len(QUESTIONS), N)]
    titles = []
    for ch in chunks:
        secs = []
        for q in ch:
            nm = SEC_BY_CODE[q[1]][2]
            if nm not in secs:
                secs.append(nm)
        titles.append("문항별 진단 결과 — " + " · ".join(secs))
    for ci, (chunk, tt) in enumerate(zip(chunks, titles)):
        rr = []
        for no, sc, pt, q, ev in chunk:
            g = int(answers.get(no, 0))
            lab = labels(sc)[g]
            got = pt * (0, .4, .7, 1.0)[g]
            rr.append(f"""<tr><td class="c">{no}</td><td class="c">{sc}</td>
<td>{q}<br><span style="color:#9AA3AE;font-size:7.5pt">{ev}</span></td>
<td class="c g{g}"><b>{lab}</b></td><td class="c">{pt}</td>
<td class="c">{got:.1f}</td><td class="c" style="color:{'#A83232' if pt-got>0 else '#B4BCC7'}">{pt-got:.1f}</td></tr>""")
        pages.append(f"""<div class="pg">
  {_hd(tt, "BY QUESTION", co, 4+ci)}
  <table>
    <tr><th style="width:12mm">No</th><th style="width:16mm">구간</th><th>질문 · 확인 증빙</th>
    <th style="width:20mm">등급</th><th style="width:16mm">배점</th>
    <th style="width:16mm">획득</th><th style="width:16mm">실점</th></tr>
    {''.join(rr)}
  </table>
  {_ft(co, tt, 4+ci)}
</div>""")

    # ── 증빙서류 준비 목록
    weak = {no for no in Q_BY_NO if int(answers.get(no, 0)) < 3}
    need = [f for f in FORMS if not f["qs"] or (set(f["qs"]) & weak)]
    half = (len(need) + 1) // 2

    def frows(items):
        return "".join(
            f'<tr><td class="c" style="font-size:7.5pt;color:#B8942E">{f["docno"].replace("IMP-","")}</td>'
            f'<td>{f["title"]}{" <b style=color:#B8942E>★</b>" if f["posted"] else ""}</td>'
            f'<td class="c" style="font-size:8pt">{" · ".join(map(str,f["qs"])) if f["qs"] else "—"}</td></tr>'
            for f in items)

    pages.append(f"""<div class="pg">
  {_hd("준비해야 할 증빙서류", "EVIDENCE", co, 7)}
  <div style="display:flex;gap:6mm">
    <table style="flex:1"><tr><th style="width:18mm">문서</th><th>문서명</th><th style="width:20mm">해당문항</th></tr>
    {frows(need[:half])}</table>
    <table style="flex:1"><tr><th style="width:18mm">문서</th><th>문서명</th><th style="width:20mm">해당문항</th></tr>
    {frows(need[half:])}</table>
  </div>
  <div class="note">
    <b>★ 표시 {sum(1 for f in need if f['posted'])}종은 사내 게시판 부착 대상</b>입니다.
    부착 후 반드시 사진을 촬영해 원본 문서와 한 세트로 편철하십시오.
    현장평가는 '했다'는 진술이 아니라 <b>즉시 제출 가능한 증빙</b>으로 등급을 판정합니다.
    회의록 · 대장류는 최소 3개월분 이상 누적되어야 실효성이 인정됩니다.
    본 목록에 해당하는 작성용 양식집을 별도 파일로 함께 제공합니다.
  </div>
  {_ft(co, "증빙서류 준비 목록", 7)}
</div>""")

    # ── AI 소견 (선택)
    if ai_text:
        body = "".join(f"<p style='margin-bottom:3mm'>{ln}</p>"
                       for ln in ai_text.strip().split("\n") if ln.strip())
        pages.append(f"""<div class="pg">
  {_hd("종합 컨설팅 소견", "ANALYSIS", co, 8)}
  <div style="font-size:9.5pt;line-height:1.9;color:#26313F;column-count:2;column-gap:10mm">{body}</div>
  {_ft(co, "종합 컨설팅 소견", 8)}
</div>""")

    # ── 결격 요건 · 면책
    dq = "".join(f'<li style="margin-bottom:2mm">{d}</li>' for d in DISQUALIFIERS)
    vd = "".join(f'<tr><td class="c l">{a}점 이상</td><td>{b} — {c}</td></tr>'
                 for a, b, c, _ in VERDICTS[:-1])
    pages.append(f"""<div class="pg">
  {_hd("판정 기준 및 유의사항", "CRITERIA", co, 9)}
  <div style="display:flex;gap:8mm">
    <div style="flex:1">
      <h3>총점 판정 기준</h3>
      <table>{vd}<tr><td class="c l">600점 미만</td><td>준비 단계 — 인프라 · 활동 구축부터 착수</td></tr></table>
      <h3>등급 판정 원칙</h3>
      <table>
        <tr><td class="c l" style="width:24mm">체계 100%</td><td>체계적으로 운영되고 증빙이 완비됨</td></tr>
        <tr><td class="c l">부분 70%</td><td>운영 중이나 증빙이 일부만 확보됨</td></tr>
        <tr><td class="c l">계획 40%</td><td>계획 · 준비 중이거나 구두로만 존재</td></tr>
        <tr><td class="c l">없음 0%</td><td>해당 활동이나 문서가 존재하지 않음</td></tr>
      </table>
      <div class="note">'체계' 등급은 <b>현장평가 당일 즉시 제출 가능한 증빙</b>이 있을 때만 해당됩니다.
      구두 설명만 가능한 항목은 '부분' 이하로 평가하십시오.</div>
    </div>
    <div style="flex:1">
      <h3>신청 자체가 불가능한 결격 요건</h3>
      <ul style="font-size:9pt;padding-left:5mm;line-height:1.8">{dq}</ul>
      <div class="note">탈락 시 수수료(신규 55만원)는 원칙적으로 환불되지 않습니다.
      결격 요건은 진단 착수 전 최우선 확인 항목입니다.</div>
      <h3>면책 고지</h3>
      <div style="font-size:8.5pt;color:#5A6472;line-height:1.8">
        본 보고서는 {co}가 제출한 자가진단 응답을 근거로 RSV가 실무 기준에 따라 산출한 결과입니다.
        실제 메인비즈 평가지표 및 배점(인프라 350 · 활동 400 · 성과 250)을 기준으로 구성하였으나,
        중소기업기술정보진흥원의 공식 온라인 자가진단 및 현장평가 결과와는 차이가 있을 수 있습니다.
        최종 인증 여부는 공식 심사기관의 판단에 따릅니다. 본 보고서는 컨설팅 목적의 참고자료이며,
        법적 효력을 갖지 않습니다.
      </div>
    </div>
  </div>
  {_ft(co, "판정 기준 및 유의사항", 9)}
</div>""")

    return f"""<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8">
<title>{co} · 경영혁신 진단 결과 보고서</title><style>{CSS}</style></head>
<body>{''.join(pages)}</body></html>"""


def _advice(code):
    return {
        "I-1": "비전 선언문 게시, 중장기 경영계획서(연도별 목표 수치 포함), 대표이사 주관 월례 경영회의록, 노사협의회 회의록, 윤리강령 제정 및 교육 기록 — 대부분 문서 정비만으로 해결됩니다.",
        "I-2": "3개년 혁신 로드맵, 과제별 담당자·기한·KPI 정의서, 분기 점검 회의록, SWOT 보고서, 혁신 예산 별도 편성 — 세트로 한 번에 구축하는 것이 효율적입니다.",
        "I-3": "지식재산권 법인 명의 확보, 정보화 시스템 도입, ISO 9001 취득(2~3개월 소요), 연간 교육계획 수립 및 예산 집행, 직무기술서 작성.",
        "II-1": "조직도·업무분장표 최신화, 인사평가 실제 작성본 확보, 성과 연동 차등 보상 대장, 교육 이수 대장 관리.",
        "II-2": "신제품 개발 기록, 개선 전·후 수치 비교표, 고객 요구사항 접수·반영 대장, 규격·시험성적서 확보.",
        "II-3": "공정흐름도 및 SOP 정비, 품질검사 기준과 불량률 추이 관리, 원가절감액 산출 근거, 리드타임 추이 수치화.",
        "II-4": "신규 판로 개척 실적, 홈페이지·카탈로그 정비, 고객 DB 구축, 시장조사 결과의 영업전략 반영, 전시회 참가 상담일지.",
        "III-1": "재무 지표는 단기 개선이 어려우므로, 가지급금·가수금 정리와 부채비율 관리 등 정상화 가능한 항목부터 착수하십시오.",
        "III-2": "상시근로자 증가, 고객만족도 조사 실시(설문지·회수본·집계표 3종), 클레임 감소 추세 관리, 대외 인증·표창 취득.",
    }.get(code, "")
