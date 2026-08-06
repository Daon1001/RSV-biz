# -*- coding: utf-8 -*-
"""이노비즈 진단 결과 → RSV 디자인 A4 가로 리포트"""

from datetime import date

import innobiz_questions as IQ
from report_builder import CSS, _bar, _hd, _ft
from forms_builder import form_set, weak_set

GRADE_LETTER = ["A", "B", "C", "D", "E"]


def _letter(no, idx):
    return "ABC"[idx] if IQ.is_fin(no) else GRADE_LETTER[idx]


def _gcls(no, idx):
    if IQ.is_fin(no):
        return ["g3", "g1", "g0"][idx]
    return ["g3", "g2", "g1", "g0", "g0"][idx]


ADVICE = {
    "I-1": "R&D 투자비율과 기술개발인력 비율은 결산 구조에서 결정됩니다. 연구개발비로 인정되는 계정(경상개발비·연구비·개발비 상각액·제조원가상 경상개발비)을 정확히 집계하고, 기능직·관리직을 제외한 순수 연구인력 명부를 별도 관리하십시오.",
    "I-2": "부설연구소 인정(3년 이상 보유가 최고 등급), 직무발명보상 규정, 대학·연구기관과의 계약 기반 공동연구가 핵심입니다. 구두 자문은 인정되지 않으니 협약서를 확보하십시오.",
    "I-3": "배점 105점 구간이며 그중 기술개발·사업화 실적 한 항목이 40점으로 62개 항목 중 최대입니다. 특허 ×3, 상용화 실적 ×3 가중치가 크므로 등록 특허 확보와 매출 5% 이상 기여 실적 정리가 최우선입니다.",
    "I-4": "기술 tree, 특허맵, 외부환경 분석, 중장기 전략서 — 네 가지 문서가 전부입니다. 분석에 그치지 말고 반영 결과를 전략 문서에 연결하십시오.",
    "II-1": "제품개발 절차서와 단계별 일정계획, 경합·대체제품 기능분석, 기술표준 제·개정 이력이 요건입니다. 표준화는 3년 실적이 있어야 최고 등급이므로 지금부터 누적해야 합니다.",
    "II-2": "배점 130점으로 단일 중항목 최대입니다. 제조공정도·QC공정도·작업표준서, 계측기 검교정 기록, 생산계획 대비 실적, 협력업체 평가체계가 핵심 증빙입니다.",
    "II-3": "마케팅 전략서, 채널 분석, 라이프사이클 분석, 선행기술조사를 포함한 지재권 관리가 요건입니다. 지재권은 법인 명의 확보 여부를 반드시 확인하십시오.",
    "III-1": "경영자 항목이 76점을 차지합니다. 기술혁신 방침 선포와 직원 숙지(평가위원이 직원 5명에게 질문해 3명 이상 확인), 경영자의 기술혁신 회의 참여율 1/3 이상이 판정 기준입니다.",
    "III-2": "경쟁사 동향 보고가 24점으로 이 구간 최대입니다. 분기 1회 이상 반복 작성된 보고서가 누적되어야 '주기적 시스템'으로 인정됩니다.",
    "III-3": "감점 방식 구간입니다. 가지급금·가수금이 총자산의 3% 이상이면 투명성에서 감점되므로 사전 정리가 가능합니다. 임금체불·거래조건 불이행 이력도 확인하십시오.",
    "IV-1": "기술경쟁력·시장경쟁력 향상도는 예측 항목이지만 근거가 필요합니다. 원가절감 실적표, 성능 비교시험 성적서, 지재권 등록원부를 근거로 제시하십시오.",
    "IV-2": "재무지표 8개 항목만 91점입니다. 업종평균은 한국은행 「기업경영분석」이 기준이며, 산출비율이 음수면 자동으로 최하등급입니다. 결산 전 시뮬레이션이 유효합니다.",
    "IV-3": "지적재산권의 사업화 가능성과 권리범위가 24점입니다. 청구범위가 넓고 타인 권리를 침해하지 않아야 최고 등급이므로, 선행기술조사와 회피설계 검토서를 갖추십시오.",
}


def build(company, result, answers, consultant="", ai_text="", memo="",
          tech_grade="", has_lab=True, years=None):
    R = result
    S = R["sections"]
    v = R["verdict"]
    total = R["total"]
    co = company.strip()
    pages = []

    tech_ok = tech_grade in IQ.TECH_GRADES[:IQ.TECH_GRADES.index("B") + 1] if tech_grade else None
    final = (total >= 700) and (tech_ok is True)

    # ── 표지
    pages.append(f"""<div class="pg cover">
  <div class="eb">INNOBIZ TECHNOLOGY INNOVATION SYSTEM</div>
  <h1>기술혁신시스템<br>진단 결과 보고서</h1>
  <div class="sub">{co}<br>총점 {total:,.0f}점 / 1,000점 · 판정 「{v['label']}」</div>
  <div class="meta"><span>진단일 {date.today().strftime('%Y년 %m월 %d일')}</span>
  <span>{'진단자 ' + consultant if consultant else ''}</span>
  <span>RSV · 부자들의 비밀금고</span></div>
</div>""")

    # ── 요약
    marks = "".join(f'<div class="mark" style="left:{p/1000*100:.1f}%"></div>'
                    for p in (650, 700, 800))
    parts = "".join(_bar(f"부문 {k} · {vv['name']}", vv["got"], vv["alloc"], k == "Ⅳ")
                    for k, vv in R["parts"].items())
    a_cnt = sum(1 for no in IQ.Q_BY_NO if int(answers.get(no, 4)) == 0)
    low_cnt = sum(1 for no in IQ.Q_BY_NO if int(answers.get(no, 4)) >= 3
                  and not IQ.is_fin(no))
    tg = (f'<b style="color:{"#1B7A4B" if tech_ok else "#A83232"}">{tech_grade}</b>'
          if tech_grade else '<b style="color:#8A929C">미입력</b>')

    pages.append(f"""<div class="pg">
  {_hd("진단 결과 요약", "SUMMARY", co, 2)}
  <div class="score">
    <div class="dial">
      <div class="n">{total:,.0f}<span> / 1,000</span></div>
      <div class="v" style="background:{v['color']}">{v['label']}</div>
      <div class="d">{v['desc']}</div>
    </div>
    <div class="bars">
      <div class="bar"><div class="t"><b>기술혁신시스템 총점</b>
        <i>자가진단 650 · 현장평가 700 · AA 800</i></div>
        <div class="track"><div class="fill g" style="width:{min(total/1000,1)*100:.1f}%"></div>{marks}</div></div>
      {parts}
    </div>
  </div>
  <div class="kpi">
    <div><b>{R['gap650']:,.0f}점</b><span>자가진단 통과선(650)까지</span></div>
    <div><b>{R['gap700']:,.0f}점</b><span>현장평가 통과선(700)까지</span></div>
    <div><b>{a_cnt}항목</b><span>A등급 (만점)</span></div>
    <div><b>{low_cnt}항목</b><span>D · E등급</span></div>
    <div><b>{tg}</b><span>개별기술 평가등급</span></div>
  </div>
  <div class="note">
    <b>이노비즈는 두 가지 기준을 동시에 충족해야 선정됩니다.</b>
    ① 기술혁신시스템 평가 <b>700점 이상</b> ② 개별기술수준 평가 <b>B등급 이상</b>(14등급제).
    온라인 자가진단에서 650점 이상이어야 기술보증기금 현장평가 신청이 가능하며,
    현장평가에서는 동일 지표를 전문평가인력이 증빙 기준으로 재평가합니다.
    선정 시 등급은 900점 이상 AAA · 800~900점 AA · 700~800점 A로 부여됩니다.
    <br><b>현재 판정 — {'선정 요건 충족' if final else ('시스템 점수 미달' if total < 700 else ('개별기술 등급 미달' if tech_ok is False else '개별기술 평가등급 확인 필요'))}</b>
  </div>
  {_ft(co, "진단 결과 요약", 2)}
</div>""")

    # ── 중항목별
    rows = []
    for code, part, name, alloc, cnt in IQ.GROUPS:
        s = S[code]
        r = s["rate"]
        pill = "p-lo" if r >= .8 else ("p-md" if r >= .6 else "p-hi")
        lv = "양호" if r >= .8 else ("보통" if r >= .6 else "취약")
        rows.append(f"""<tr><td class="c">{part}</td><td class="l">{name}</td>
<td class="c">{cnt}</td><td class="c">{alloc}</td><td class="c"><b>{s['got']:,.1f}</b></td>
<td class="c">{s['lost']:,.1f}</td><td class="c">{r*100:.0f}%</td>
<td class="c"><span class="pill {pill}">{lv}</span></td>
<td><div class="track" style="height:4mm"><div class="fill{' g' if r>=.8 else ''}" style="width:{min(r,1)*100:.1f}%"></div></div></td></tr>""")

    pr = sorted(S.values(), key=lambda x: -x["lost"])[:3]
    prio = "".join(
        f'<tr><td class="c">{i+1}</td><td class="l">{p["name"]}</td>'
        f'<td class="c">{p["lost"]:,.1f}점</td><td>{ADVICE.get(p["code"],"")}</td></tr>'
        for i, p in enumerate(pr))

    pages.append(f"""<div class="pg">
  {_hd("중항목별 진단 결과", "BY GROUP", co, 3)}
  <table>
    <tr><th style="width:12mm">부문</th><th style="width:44mm">중항목</th><th style="width:14mm">항목</th>
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
  <h3>보완 우선순위 — 실점 규모 상위 3개 중항목</h3>
  <table>
    <tr><th style="width:14mm">순위</th><th style="width:44mm">중항목</th><th style="width:22mm">실점</th><th>보완 방향</th></tr>
    {prio}
  </table>
  <div class="note">{memo if memo else
    "이노비즈는 <b>배점 최소값이 0이 아니라 배점의 20%</b>(E등급 = 1점/5점)입니다. "
    "따라서 전 항목 최하등급이어도 200점이 확보되며, 실질 경쟁 구간은 200~1,000점입니다. "
    "달성률 60% 미만(C등급 이하) 항목을 먼저 끌어올리는 것이 점수 효율이 가장 높습니다."}</div>
  {_ft(co, "중항목별 진단 결과", 3)}
</div>""")

    # ── 문항별 (11개씩)
    N = 11
    QS = IQ.QUESTIONS
    chunks = [QS[i:i + N] for i in range(0, len(QS), N)]
    for ci, chunk in enumerate(chunks):
        gs = []
        for q in chunk:
            nm = IQ.GRP_BY_CODE[q[1]][2]
            if nm not in gs:
                gs.append(nm)
        tt = "항목별 진단 결과 — " + " · ".join(gs)
        rr = []
        for no, gc, pt, label, q, opts, ev in chunk:
            w = IQ.weights(no)
            i = min(max(int(answers.get(no, len(w) - 1)), 0), len(w) - 1)
            got = pt * w[i]
            rr.append(f"""<tr><td class="c">{no}</td><td class="c" style="font-size:8pt">{gc}</td>
<td><b>{label}</b><br><span style="color:#9AA3AE;font-size:7.5pt">{ev}</span></td>
<td class="c {_gcls(no,i)}"><b>{_letter(no,i)}</b></td>
<td style="font-size:8pt">{opts[i]}</td>
<td class="c">{pt}</td><td class="c">{got:.1f}</td>
<td class="c" style="color:{'#A83232' if pt-got>0 else '#B4BCC7'}">{pt-got:.1f}</td></tr>""")
        pages.append(f"""<div class="pg">
  {_hd(tt, "BY ITEM", co, 4+ci)}
  <table>
    <tr><th style="width:11mm">No</th><th style="width:14mm">구간</th><th>평가항목 · 확인 증빙</th>
    <th style="width:14mm">등급</th><th style="width:62mm">평가 내용</th>
    <th style="width:14mm">배점</th><th style="width:14mm">획득</th><th style="width:14mm">실점</th></tr>
    {''.join(rr)}
  </table>
  {_ft(co, tt, 4+ci)}
</div>""")

    pn = 4 + len(chunks)

    # ── 증빙서류
    weak = weak_set(R, "innobiz")
    need = [f for f in form_set("innobiz") if not f["qs"] or (set(f["qs"]) & weak)]
    half = (len(need) + 1) // 2

    def frows(items):
        return "".join(
            f'<tr><td class="c" style="font-size:7.5pt;color:#B8942E">'
            f'{f["docno"].replace("INO-","").replace("IMP-","공통 ")}</td>'
            f'<td>{f["title"]}{" <b style=color:#B8942E>★</b>" if f["posted"] else ""}</td>'
            f'<td class="c" style="font-size:8pt">{" · ".join(map(str,f["qs"])) if f["qs"] else "—"}</td></tr>'
            for f in items)

    pages.append(f"""<div class="pg">
  {_hd("준비해야 할 증빙서류", "EVIDENCE", co, pn)}
  <div style="display:flex;gap:6mm">
    <table style="flex:1"><tr><th style="width:20mm">문서</th><th>문서명</th><th style="width:22mm">해당항목</th></tr>
    {frows(need[:half])}</table>
    <table style="flex:1"><tr><th style="width:20mm">문서</th><th>문서명</th><th style="width:22mm">해당항목</th></tr>
    {frows(need[half:])}</table>
  </div>
  <div class="note">
    <b>★ {sum(1 for f in need if f['posted'])}종은 사내 · 연구소 게시 대상</b>입니다.
    '공통' 표시는 메인비즈 양식집과 공유되는 문서로, 이미 갖추셨다면 그대로 사용하십시오.
    이노비즈 현장평가는 기술보증기금 전문평가인력이 수행하며, <b>기술 관련 문서의 실재 여부</b>를
    직접 확인합니다. 특히 기술개발·사업화 실적(40점)과 재무지표(91점)는 사전 산출이 가능하므로
    현장평가 전에 반드시 정리해두십시오.
  </div>
  {_ft(co, "증빙서류 준비 목록", pn)}
</div>""")
    pn += 1

    if ai_text:
        body = "".join(f"<p style='margin-bottom:3mm'>{ln}</p>"
                       for ln in ai_text.strip().split("\n") if ln.strip())
        pages.append(f"""<div class="pg">
  {_hd("종합 컨설팅 소견", "ANALYSIS", co, pn)}
  <div style="font-size:9.5pt;line-height:1.9;color:#26313F;column-count:2;column-gap:10mm">{body}</div>
  {_ft(co, "종합 컨설팅 소견", pn)}
</div>""")
        pn += 1

    # ── 판정 기준
    dq = "".join(f'<li style="margin-bottom:2mm">{d}</li>' for d in IQ.DISQUALIFIERS)
    fee = "".join(f'<tr><td class="c l" style="width:44mm">{a}</td><td>{b}</td></tr>'
                  for a, b in IQ.FEES)
    grades = " · ".join(IQ.TECH_GRADES)

    pages.append(f"""<div class="pg">
  {_hd("판정 기준 및 유의사항", "CRITERIA", co, pn)}
  <div style="display:flex;gap:8mm">
    <div style="flex:1">
      <h3>선정 요건 — 두 가지를 동시에 충족</h3>
      <table>
        <tr><td class="c l" style="width:44mm">기술혁신시스템 평가</td><td>1,000점 만점 중 <b>700점 이상</b></td></tr>
        <tr><td class="c l">개별기술수준 평가</td><td>14등급 중 <b>B등급 이상</b></td></tr>
        <tr><td class="c l">온라인 자가진단</td><td>650점 이상이어야 현장평가 신청 가능</td></tr>
        <tr><td class="c l">선정 등급</td><td>900점 이상 AAA · 800~900 AA · 700~800 A</td></tr>
      </table>
      <h3>채점 방식</h3>
      <table>
        <tr><td class="c l" style="width:44mm">일반 항목</td><td>A 5점 · B 4점 · C 3점 · D 2점 · E 1점</td></tr>
        <tr><td class="c l">경영실적 재무지표</td><td>A 5점 · B 3점 · C 1점 (3단계)</td></tr>
        <tr><td class="c l">항목 점수</td><td>배점 × (평가점수 ÷ 5)</td></tr>
      </table>
      <div class="note">개별기술수준 평가는 <b>경영주 기술능력 · 기술성 · 시장성 · 사업성 및 수익성</b>
      4개 분야 34개 내외 항목으로 구성되며, 등급은 {grades} 순입니다.</div>
    </div>
    <div style="flex:1">
      <h3>신청 자체가 불가능한 결격 요건</h3>
      <ul style="font-size:9pt;padding-left:5mm;line-height:1.8">{dq}</ul>
      <h3>평가 수수료</h3>
      <table>{fee}</table>
      <h3>면책 고지</h3>
      <div style="font-size:8.5pt;color:#5A6472;line-height:1.8">
        본 보고서는 {co}가 제출한 자가진단 응답을 근거로, 중소벤처기업부 · 이노비즈협회의
        공식 「기술혁신시스템 평가지표(제조업종)」 배점 체계에 따라 산출한 결과입니다.
        실제 현장평가는 기술보증기금 전문평가인력이 증빙 확인을 거쳐 수행하므로 결과에 차이가 있을 수
        있으며, 업종(비제조 · 건설 · 소프트웨어 · 바이오 · 환경 · 전문디자인)에 따라 세부 배점이
        달라집니다. 개별기술수준 평가는 본 진단에 포함되지 않습니다. 최종 선정 여부는 평가기관과
        중소벤처기업부의 판단에 따르며, 본 보고서는 컨설팅 목적의 참고자료로 법적 효력을 갖지 않습니다.
      </div>
    </div>
  </div>
  {_ft(co, "판정 기준 및 유의사항", pn)}
</div>""")

    return f"""<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8">
<title>{co} · 이노비즈 기술혁신시스템 진단 결과 보고서</title><style>{CSS}</style></head>
<body>{''.join(pages)}</body></html>"""
