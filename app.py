# -*- coding: utf-8 -*-
"""
RSV 인증 진단 시스템 — 메인비즈 · 이노비즈
진단 → 결과 분석 리포트 → 맞춤 증빙양식집 자동 생성
"""

from datetime import datetime

import pandas as pd
import streamlit as st

import auth
import forms_builder as FB
import report_builder as RB
import report_innobiz as RI
import innobiz_questions as IQ
from questions import (QUESTIONS, SECTIONS, labels, label_desc, score,
                       DISQUALIFIERS)

st.set_page_config(page_title="RSV 인증 진단", page_icon="📊", layout="wide")

NAVY, GOLD = "#0F1E3D", "#B8942E"

st.markdown(f"""<style>
.stApp {{ background:#F4F6F9; }}
section[data-testid="stSidebar"] {{ background:{NAVY}; }}
section[data-testid="stSidebar"] * {{ color:#E8ECF3 !important; }}
section[data-testid="stSidebar"] .stButton button {{ background:#1B2E4F; border:1px solid #4A5A78; }}
h1,h2,h3 {{ color:{NAVY} !important; letter-spacing:-.5px; }}
.rsv-hero {{ background:{NAVY}; color:#fff; padding:22px 28px; border-radius:8px; margin-bottom:18px; }}
.rsv-hero .eb {{ color:{GOLD}; letter-spacing:6px; font-size:11px; font-weight:700; }}
.rsv-hero h1 {{ color:#fff !important; font-size:28px; margin:6px 0 4px; }}
.rsv-hero p {{ color:#B9C6D8; margin:0; font-size:14px; }}
div[data-testid="stMetricValue"] {{ color:{NAVY}; }}
.stButton button[kind="primary"] {{ background:{GOLD}; border:none; }}
.qcard {{ background:#fff; border:1px solid #DDE3EB; border-left:4px solid {GOLD};
  border-radius:6px; padding:12px 16px; margin-bottom:10px; }}
.qcard .qn {{ color:{GOLD}; font-weight:800; font-size:12px; }}
.qcard .qt {{ color:{NAVY}; font-weight:700; font-size:15px; margin:2px 0 4px; }}
.qcard .qe {{ color:#8A929C; font-size:12px; }}
</style>""", unsafe_allow_html=True)

SS = st.session_state
SS.setdefault("user", None)
SS.setdefault("cert", "mainbiz")
SS.setdefault("answers", {})
SS.setdefault("answers_i", {})
SS.setdefault("company", "")
SS.setdefault("prefix", "DOC")
SS.setdefault("tech_grade", "")

CERT_NAME = {"mainbiz": "메인비즈 · 경영혁신형", "innobiz": "이노비즈 · 기술혁신형"}


def cur_answers():
    return SS.answers_i if SS.cert == "innobiz" else SS.answers


def cur_score():
    return IQ.score(SS.answers_i) if SS.cert == "innobiz" else score(SS.answers)


# ───────────────────────────────────────── 로그인
def login_view():
    st.markdown(f"""<div class="rsv-hero">
      <div class="eb">RSV · 부자들의 비밀금고</div>
      <h1>메인비즈 · 이노비즈 인증 진단 시스템</h1>
      <p>공식 평가지표 기반 진단 → 결과 분석 리포트 → 맞춤 증빙양식집 자동 생성</p>
    </div>""", unsafe_allow_html=True)

    if not auth._cfg("gist_id"):
        st.error("Secrets(gist_id, github_token)가 설정되지 않았습니다. "
                 "Streamlit Cloud → Settings → Secrets 를 확인하십시오.")
        return

    auth.ensure_admin()
    t1, t2 = st.tabs(["로그인", "가입 신청"])
    with t1:
        e = st.text_input("이메일", key="li_email", placeholder="name@example.com")
        if st.button("로그인", type="primary", use_container_width=True):
            u, msg = auth.login(e)
            if u:
                SS.user = u
                st.rerun()
            else:
                st.error(msg)
    with t2:
        c1, c2 = st.columns(2)
        e = c1.text_input("이메일", key="su_email")
        n = c2.text_input("이름", key="su_name")
        co = c1.text_input("소속 회사", key="su_co")
        pp = c2.text_input("사용 목적", key="su_pp", placeholder="예: 고객사 인증 컨설팅")
        if st.button("가입 신청", use_container_width=True):
            if not (e and n):
                st.warning("이메일과 이름은 필수입니다.")
            else:
                ok, msg = auth.signup(e, n, co, pp)
                (st.success if ok else st.error)(msg)


# ───────────────────────────────────────── 고객사
def page_company():
    st.subheader("고객사 관리")
    u = SS.user
    rows = auth.list_companies(u["email"])

    with st.expander("＋ 고객사 등록 · 수정", expanded=not rows):
        c1, c2, c3 = st.columns([2, 1.2, 1])
        name = c1.text_input("회사명", placeholder="예: 주식회사 아이엠팩")
        biz = c2.text_input("사업자등록번호", placeholder="000-00-00000")
        pfx = c3.text_input("문서번호 접두어", value="", max_chars=6,
                            placeholder="예: IMP", help="증빙양식 문서번호에 사용됩니다. 비우면 DOC")
        c4, c5 = st.columns([1, 2])
        ind = c4.text_input("업종", placeholder="예: 플라스틱 포장재 제조")
        note = c5.text_input("메모", placeholder="상담 메모 · 특이사항")
        if st.button("저장", type="primary"):
            if not name.strip():
                st.warning("회사명을 입력하십시오.")
            else:
                auth.upsert_company(u["email"], name.strip(), biz, ind, note,
                                    prefix=(pfx or "DOC").upper())
                st.success(f"{name} 저장 완료")
                st.rerun()

    if not rows:
        st.info("등록된 고객사가 없습니다. 위에서 먼저 등록하십시오.")
        return

    st.markdown("##### 등록된 고객사")
    for r in rows:
        c1, c2, c3, c4, c5 = st.columns([3, 1.7, 1.2, 1.1, 0.9])
        c1.markdown(f"**{r['name']}**  \n<span style='color:#8A929C;font-size:12px'>"
                    f"{r.get('industry','')} · {r.get('biz_no','')}</span>",
                    unsafe_allow_html=True)
        mb, ib = r.get("total"), r.get("total_i")
        c2.caption(f"메인비즈 {f'{mb:,.0f}점' if mb else '—'} · "
                   f"이노비즈 {f'{ib:,.0f}점' if ib else '—'}")
        c3.caption(f"수정 {r.get('updated','')[:10]}")
        if c4.button("불러오기", key=f"ld{r['name']}", use_container_width=True):
            SS.company = r["name"]
            SS.prefix = r.get("prefix", "DOC")
            SS.answers = {int(k): int(v) for k, v in (r.get("answers") or {}).items()}
            SS.answers_i = {int(k): int(v) for k, v in (r.get("answers_i") or {}).items()}
            SS.tech_grade = r.get("tech_grade", "")
            st.success(f"{r['name']} 불러왔습니다.")
            st.rerun()
        if c5.button("삭제", key=f"dl{r['name']}", use_container_width=True):
            auth.delete_company(u["email"], r["name"])
            st.rerun()


# ───────────────────────────────────────── 진단
def _save_company(**kw):
    rows = auth.load("companies")
    now = datetime.now().isoformat(timespec="seconds")
    owner, name = SS.user["email"], SS.company.strip()
    hit = None
    for r in rows:
        if r.get("owner", "").lower() == owner.lower() and r.get("name") == name:
            hit = r
            break
    if hit is None:
        hit = dict(owner=owner, name=name, created=now)
        rows.append(hit)
    if "answers" in kw:
        kw["answers"] = {str(k): int(v) for k, v in kw["answers"].items()}
    if "answers_i" in kw:
        kw["answers_i"] = {str(k): int(v) for k, v in kw["answers_i"].items()}
    hit.update(prefix=SS.prefix, updated=now, **kw)
    auth.save("companies", rows)


def _diagnose_main():
    quick = st.columns(5)
    quick[0].caption("일괄 입력")
    for i, (lab, g) in enumerate([("모두 없음", 0), ("모두 계획", 1),
                                  ("모두 부분", 2), ("모두 체계", 3)]):
        if quick[i + 1].button(lab, use_container_width=True, key=f"qm{g}"):
            SS.answers = {q[0]: g for q in QUESTIONS}
            st.rerun()

    tabs = st.tabs([f"{c}  {n}" for c, _, n, *_ in SECTIONS])
    for tab, (code, part, name, alloc, cnt, perf) in zip(tabs, SECTIONS):
        with tab:
            labs, descs = labels(code), label_desc(code)
            st.caption(f"부문 {part} · {name} — 배점 {alloc}점 / {cnt}문항 · "
                       f"{labs[0]} 0% · {labs[1]} 40% · {labs[2]} 70% · {labs[3]} 100%")
            for no, sc, pt, q, ev in QUESTIONS:
                if sc != code:
                    continue
                st.markdown(f"""<div class="qcard">
                  <div class="qn">Q{no:02d} · {pt}점</div>
                  <div class="qt">{q}</div>
                  <div class="qe">확인 증빙 — {ev}</div>
                </div>""", unsafe_allow_html=True)
                SS.answers[no] = st.radio(
                    f"Q{no}", options=[0, 1, 2, 3],
                    format_func=lambda g, L=labs, D=descs: f"{L[g]} — {D[g]}",
                    index=int(SS.answers.get(no, 0)),
                    key=f"q{no}", label_visibility="collapsed")


def _diagnose_inno():
    c1, c2 = st.columns([1.4, 3])
    opts = [""] + IQ.TECH_GRADES
    SS.tech_grade = c1.selectbox(
        "개별기술수준 평가등급 (14등급)", opts,
        index=opts.index(SS.tech_grade) if SS.tech_grade in opts else 0,
        help="기술보증기금 개별기술 평가 결과. B등급 이상이어야 선정됩니다.")
    c2.caption("이노비즈는 기술혁신시스템 700점 이상 **그리고** 개별기술 B등급 이상을 "
               "동시에 충족해야 선정됩니다. 등급을 모르면 비워두십시오.")

    quick = st.columns(6)
    quick[0].caption("일괄 입력")
    for i, (lab, g) in enumerate([("모두 A", 0), ("모두 B", 1), ("모두 C", 2),
                                  ("모두 D", 3), ("모두 E", 4)]):
        if quick[i + 1].button(lab, use_container_width=True, key=f"qi{g}"):
            SS.answers_i = {q[0]: min(g, len(IQ.weights(q[0])) - 1) for q in IQ.QUESTIONS}
            st.rerun()

    tabs = st.tabs([f"부문 {p}  {n}" for p, n, _, _ in IQ.PARTS])
    for tab, (pcode, pname, palloc, pcnt) in zip(tabs, IQ.PARTS):
        with tab:
            st.caption(f"{pname} — 배점 {palloc}점 / {pcnt}항목 · "
                       "A 100% · B 80% · C 60% · D 40% · E 20% "
                       "(경영실적 재무지표는 A 100% · B 60% · C 20%)")
            for gcode, gpart, gname, galloc, gcnt in IQ.GROUPS:
                if gpart != pcode:
                    continue
                st.markdown(f"**{gcode}. {gname}** — {galloc}점 / {gcnt}항목")
                for no, gc, pt, label, q, opt, ev in IQ.QUESTIONS:
                    if gc != gcode:
                        continue
                    st.markdown(f"""<div class="qcard">
                      <div class="qn">{no:02d} · {label} · {pt}점</div>
                      <div class="qt">{q}</div>
                      <div class="qe">확인 증빙 — {ev}</div>
                    </div>""", unsafe_allow_html=True)
                    n_opt = len(opt)
                    letters = "ABC" if IQ.is_fin(no) else "ABCDE"
                    SS.answers_i[no] = st.radio(
                        f"I{no}", options=list(range(n_opt)),
                        format_func=lambda i, O=opt, L=letters: f"{L[i]} — {O[i]}",
                        index=min(int(SS.answers_i.get(no, n_opt - 1)), n_opt - 1),
                        key=f"i{no}", label_visibility="collapsed")


def page_diagnose():
    st.subheader(f"{CERT_NAME[SS.cert]} 진단")

    c1, c2, c3 = st.columns([2.4, 1, 1])
    SS.company = c1.text_input("진단 대상 회사명", value=SS.company,
                               placeholder="예: 주식회사 아이엠팩")
    SS.prefix = (c2.text_input("문서번호 접두어", value=SS.prefix, max_chars=6) or "DOC").upper()
    if c3.button("응답 초기화", use_container_width=True):
        if SS.cert == "innobiz":
            SS.answers_i = {}
        else:
            SS.answers = {}
        st.rerun()

    dq = IQ.DISQUALIFIERS if SS.cert == "innobiz" else DISQUALIFIERS
    with st.expander("결격 요건 사전 확인 — 하나라도 해당되면 신청 자체가 불가합니다"):
        for d in dq:
            st.markdown(f"- {d}")

    st.markdown("---")
    if SS.cert == "innobiz":
        _diagnose_inno()
    else:
        _diagnose_main()

    st.markdown("---")
    r = cur_score()
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("현재 총점", f"{r['total']:,.0f} / 1,000")
    c2.metric("판정", r["verdict"]["label"])
    if SS.cert == "innobiz":
        c3.metric("자가진단선(650)까지", f"{r['gap650']:,.0f}점")
        c4.metric("현장평가선(700)까지", f"{r['gap700']:,.0f}점")
    else:
        c3.metric("700점까지", f"{r['gap700']:,.0f}점")
        c4.metric("780점까지", f"{r['gap780']:,.0f}점")

    if st.button("진단 결과 저장", type="primary", use_container_width=True):
        if not SS.company.strip():
            st.warning("회사명을 입력하십시오.")
        else:
            kw = ({"answers_i": SS.answers_i, "total_i": r["total"],
                   "tech_grade": SS.tech_grade}
                  if SS.cert == "innobiz" else
                  {"answers": SS.answers, "total": r["total"]})
            _save_company(**kw)
            st.success("저장했습니다. '결과 · 리포트' 메뉴에서 보고서를 발행하십시오.")


# ───────────────────────────────────────── 결과 · 리포트
def gen_ai(co, r, model, inno):
    try:
        import anthropic
    except ImportError:
        st.error("anthropic 패키지가 설치되지 않았습니다.")
        return ""
    key = auth._cfg("anthropic_api_key")
    if not key:
        st.error("anthropic_api_key 시크릿이 없습니다.")
        return ""
    lines = [f"- {s['name']}: {s['got']:.1f}/{s['alloc']}점 "
             f"({s['rate']*100:.0f}%), 실점 {s['lost']:.1f}점"
             for s in r["sections"].values()]
    if inno:
        head = (f"이노비즈(기술혁신형 중소기업) 기술혁신시스템 평가 결과입니다.\n"
                f"총점 {r['total']:.0f}/1,000점. 자가진단 통과선 650점, 현장평가 통과선 700점.\n"
                f"650점까지 {r['gap650']:.0f}점, 700점까지 {r['gap700']:.0f}점 부족.")
        role = "이노비즈 인증 컨설팅 전문가"
    else:
        head = (f"메인비즈(경영혁신형 중소기업) 진단 결과입니다.\n"
                f"총점 {r['total']:.0f}/1,000점. 신청 가능선 700점, 실무 목표선 780점.\n"
                f"700점까지 {r['gap700']:.0f}점, 780점까지 {r['gap780']:.0f}점 부족.")
        role = "메인비즈 인증 컨설팅 전문가"

    prompt = f"""당신은 {role}입니다. 아래는 {co}의 진단 결과입니다.

{head}
{chr(10).join(lines)}

이 기업의 컨설턴트로서 종합 소견을 작성하십시오.
- 한국어 존댓말, 문단당 3~4문장, 총 5~6문단
- 첫 문단은 전체 진단 총평
- 이후 취약 구간의 원인 진단과 구체적 보완 방향
- 마지막 문단은 8~12주 준비 로드맵 제안
- 마크다운 기호(#, *, -) 사용 금지, 순수 문장만
- 과장 없이 실무적으로, 리스크도 함께 언급"""
    try:
        cl = anthropic.Anthropic(api_key=key)
        res = cl.messages.create(model=model, max_tokens=2000,
                                 messages=[{"role": "user", "content": prompt}])
        txt = "".join(b.text for b in res.content if b.type == "text")
        auth.log_usage(SS.user["email"], model, res.usage.input_tokens,
                       res.usage.output_tokens,
                       "이노비즈_AI소견" if inno else "메인비즈_AI소견")
        return txt
    except Exception as e:
        st.error(f"생성 실패: {e}")
        return ""


def page_result():
    ans = cur_answers()
    if not ans:
        st.info("먼저 '진단' 메뉴에서 응답하십시오.")
        return
    co = SS.company.strip() or "고객사"
    r = cur_score()
    v = r["verdict"]
    inno = SS.cert == "innobiz"

    st.markdown(f"""<div class="rsv-hero">
      <div class="eb">{'INNOBIZ' if inno else 'MAINBIZ'} DIAGNOSIS RESULT</div>
      <h1>{co} — {r['total']:,.0f}점 / 1,000점</h1>
      <p>판정 「{v['label']}」 · {v['desc']}</p>
    </div>""", unsafe_allow_html=True)

    cols = st.columns(len(r["parts"]))
    for i, (k, p) in enumerate(r["parts"].items()):
        cols[i].metric(f"부문 {k} · {p['name']}",
                       f"{p['got']:,.1f} / {p['alloc']}", f"{p['rate']*100:.0f}%")

    if inno and SS.tech_grade:
        ok = IQ.TECH_GRADES.index(SS.tech_grade) <= IQ.TECH_GRADES.index("B")
        (st.success if (ok and r["total"] >= 700) else st.warning)(
            f"개별기술 평가등급 **{SS.tech_grade}** — "
            f"{'B등급 이상 충족' if ok else 'B등급 미달'} / 시스템 점수 "
            f"{'700점 이상 충족' if r['total'] >= 700 else '700점 미달'}")

    st.markdown("##### 구간별 달성률")
    df = pd.DataFrame([
        dict(구간=(s["name"] if inno else f"{s['code']} {s['name']}"), 배점=s["alloc"],
             획득=round(s["got"], 1), 실점=round(s["lost"], 1),
             달성률=round(s["rate"] * 100, 1))
        for s in r["sections"].values()])
    st.dataframe(df, use_container_width=True, hide_index=True,
                 column_config={"달성률": st.column_config.ProgressColumn(
                     "달성률", format="%.0f%%", min_value=0, max_value=100)})

    st.markdown("##### 보완 우선순위 — 실점 규모 상위 3개")
    for i, s in enumerate(sorted(r["sections"].values(), key=lambda x: -x["lost"])[:3]):
        st.markdown(f"**{i+1}. {s['name']}** — 실점 {s['lost']:,.1f}점 "
                    f"(달성률 {s['rate']*100:.0f}%)")
        st.caption(RI.ADVICE.get(s["code"], "") if inno else RB._advice(s["code"]))

    st.markdown("---")
    st.markdown("##### 리포트 발행")
    consultant = st.text_input("진단자 표기", value=SS.user.get("name", ""))
    memo = st.text_area("컨설턴트 코멘트 (선택) — 리포트에 반영됩니다", height=80)

    ai_text = ""
    key_ai = f"ai_{SS.cert}"
    with st.expander("AI 종합 소견 추가 (선택)"):
        model = st.selectbox("모델", ["claude-haiku-4-5-20251001", "claude-sonnet-4-6"],
                             format_func=lambda m: {
                                 "claude-haiku-4-5-20251001": "Haiku 4.5 — 빠르고 저렴",
                                 "claude-sonnet-4-6": "Sonnet 4.6 — 기본 추천"}[m])
        left = auth.quota_left(SS.user)
        st.caption("이번 달 잔여 " + ("무제한" if left is None else f"{left}회"))
        if st.button("AI 소견 생성"):
            if left == 0:
                st.error("이번 달 사용 한도를 초과했습니다.")
            else:
                t = gen_ai(co, r, model, inno)
                if t:
                    SS[key_ai] = t
                    st.success("생성 완료.")
        if SS.get(key_ai):
            st.text_area("생성된 소견", SS[key_ai], height=200)
            ai_text = SS[key_ai]

    if inno:
        html = RI.build(co, r, SS.answers_i, consultant=consultant,
                        ai_text=ai_text, memo=memo, tech_grade=SS.tech_grade)
        fn = f"{co}_이노비즈_진단결과보고서_{datetime.now():%y%m%d}.html"
    else:
        html = RB.build(co, r, SS.answers, consultant=consultant,
                        ai_text=ai_text, memo=memo)
        fn = f"{co}_메인비즈_진단결과보고서_{datetime.now():%y%m%d}.html"

    st.download_button("진단 결과 보고서 내려받기 (HTML)", html.encode("utf-8"),
                       file_name=fn, mime="text/html", type="primary",
                       use_container_width=True)
    st.caption("브라우저에서 열고 Ctrl+P → 대상을 'PDF로 저장', 용지 A4 가로, 배경 그래픽 켜기.")


# ───────────────────────────────────────── 증빙양식집
def page_forms():
    co = SS.company.strip()
    if not co:
        st.info("먼저 '진단' 메뉴에서 회사명을 입력하십시오.")
        return

    cert = SS.cert
    src = FB.form_set(cert)
    st.subheader("증빙양식집 생성")
    st.caption(f"{co} · {CERT_NAME[cert]} · 문서번호 접두어 {SS.prefix} · 전체 {len(src)}종")

    ans = cur_answers()
    rec = set(FB.recommend(cur_score(), cert)) if ans else {f["docno"] for f in src}
    mode = st.radio("포함 범위",
                    ["진단 결과 기반 자동 추천", f"전체 {len(src)}종", "직접 선택"],
                    horizontal=True)

    if mode.startswith("전체"):
        picked = [f["docno"] for f in src]
    elif mode == "진단 결과 기반 자동 추천":
        picked = [f["docno"] for f in src if f["docno"] in rec]
        crit = "C등급 이하" if cert == "innobiz" else "'체계' 등급 미달"
        st.info(f"{crit}로 평가된 항목에 대응하는 **{len(picked)}종**이 선택되었습니다.")
    else:
        picked = []
        grp = {"L": "리더십 · 조직문화", "S": "혁신전략", "R": "경영자원 · 인력",
               "O": "조직 혁신역량", "P": "제품 · 프로세스", "M": "마케팅",
               "A": "기술혁신능력", "B": "기술사업화능력",
               "C": "기술혁신경영능력", "D": "기술혁신성과"}
        cur = None
        for f in src:
            g = f["docno"].split("-")[1]
            if g != cur:
                st.markdown(f"**{grp.get(g, g)}**")
                cur = g
            tag = " ★게시용" if f["posted"] else ""
            sh = " (공통)" if f.get("shared") else ""
            qs = " · ".join(map(str, f["qs"])) if f["qs"] else "—"
            if st.checkbox(f"{f['title']}{tag}{sh}  ·  항목 {qs}",
                           value=f["docno"] in rec, key=f"ck{cert}{f['docno']}"):
                picked.append(f["docno"])

    if not picked:
        st.warning("최소 1종 이상 선택하십시오.")
        return

    n_post = sum(1 for f in src if f["docno"] in picked and f["posted"])
    c1, c2, c3 = st.columns(3)
    c1.metric("포함 문서", f"{len(picked)}종")
    c2.metric("게시판 부착 대상", f"{n_post}종")
    c3.metric("총 페이지", f"{len(picked)+2}쪽")

    html = FB.build(co, picked, prefix=SS.prefix, cert=cert)
    tag = "이노비즈" if cert == "innobiz" else "메인비즈"
    st.download_button("증빙양식집(작성용) 내려받기 — HTML", html.encode("utf-8"),
                       file_name=f"{co}_{tag}_증빙양식집_작성용_{datetime.now():%y%m%d}.html",
                       mime="text/html", type="primary", use_container_width=True)

    st.markdown("""
**사용 안내**
- 파일을 PC에 내려받아 크롬·엣지로 열면 화면에서 바로 입력됩니다. Tab 키로 다음 칸 이동.
- 상단 툴바 — 문서 바로가기 · 전체 인쇄 · ★게시용만 인쇄 · 작성내용 저장(JSON) · 불러오기.
- 문서마다 오른쪽 위 「이 문서만 인쇄」 버튼이 있습니다.
- 인쇄 미리보기에서 **배경 그래픽 켜기**를 체크해야 제목띠가 출력됩니다.
""")

    with st.expander("포함된 문서 목록"):
        st.dataframe(pd.DataFrame([
            dict(문서번호=f["docno"].replace("IMP-", SS.prefix + "-").replace("INO-", SS.prefix + "-"),
                 문서명=f["title"], 해당항목=" · ".join(map(str, f["qs"])) or "—",
                 게시="★" if f["posted"] else "",
                 공통="○" if f.get("shared") else "")
            for f in src if f["docno"] in picked]),
            use_container_width=True, hide_index=True)


# ───────────────────────────────────────── 관리자
def page_admin():
    st.subheader("관리자 대시보드")
    t1, t2, t3, t4 = st.tabs(["사용량 통계", "사용자 관리", "승인 대기", "상세 로그"])
    usage = auth.load("usage")
    users = auth.load("users")

    with t1:
        if not usage:
            st.info("사용 기록이 없습니다.")
        else:
            df = pd.DataFrame(usage)
            df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
            df = df.dropna(subset=["timestamp"])
            c = st.columns(4)
            c[0].metric("전체 호출", f"{len(df):,}")
            c[1].metric("입력 토큰", f"{df['input_tokens'].sum():,}")
            c[2].metric("출력 토큰", f"{df['output_tokens'].sum():,}")
            c[3].metric("누적 비용", f"${df['cost_usd'].sum():,.2f}")
            st.markdown("###### 사용자별")
            g = df.groupby("email").agg(호출=("email", "size"),
                                        비용USD=("cost_usd", "sum")).reset_index()
            st.dataframe(g.sort_values("비용USD", ascending=False),
                         use_container_width=True, hide_index=True)
            st.markdown("###### 일별 추이")
            st.bar_chart(df.set_index("timestamp").resample("D")["cost_usd"].sum().tail(30))

    with t2:
        for u in [x for x in users if x.get("approved")]:
            c = st.columns([2.4, 1.6, 1, 1, 1])
            c[0].markdown(f"**{u.get('name','')}** · {u['email']}")
            c[1].caption(f"{u.get('company','')} · {u.get('role','user')}")
            c[2].caption(f"이번달 {auth.month_count(u['email'])}회")
            if u.get("suspended"):
                if c[3].button("정지 해제", key=f"un{u['email']}"):
                    auth.set_user(u["email"], suspended=False); st.rerun()
            else:
                if c[3].button("정지", key=f"sp{u['email']}"):
                    auth.set_user(u["email"], suspended=True); st.rerun()
            if u["email"] != auth.ADMIN_EMAIL and c[4].button("삭제", key=f"rm{u['email']}"):
                auth.delete_user(u["email"]); st.rerun()

    with t3:
        pend = [x for x in users if not x.get("approved")]
        if not pend:
            st.info("승인 대기 중인 신청이 없습니다.")
        for u in pend:
            c = st.columns([3, 2, 1, 1])
            c[0].markdown(f"**{u.get('name','')}** · {u['email']}")
            c[1].caption(f"{u.get('company','')} · {u.get('purpose','')}")
            if c[2].button("승인", key=f"ap{u['email']}", type="primary"):
                auth.set_user(u["email"], approved=True); st.rerun()
            if c[3].button("거부", key=f"rj{u['email']}"):
                auth.delete_user(u["email"]); st.rerun()

    with t4:
        if usage:
            df = pd.DataFrame(usage).sort_values("timestamp", ascending=False)
            st.dataframe(df, use_container_width=True, hide_index=True)
            st.download_button("CSV 다운로드", df.to_csv(index=False).encode("utf-8-sig"),
                               "rsv_diag_usage.csv", "text/csv")


# ───────────────────────────────────────── 라우팅
if SS.user is None:
    login_view()
else:
    u = SS.user
    with st.sidebar:
        st.markdown("### RSV 인증 진단")
        st.caption(f"{u.get('name','')} · {u['email']}")
        st.markdown("---")
        cert = st.radio("인증 유형", ["mainbiz", "innobiz"],
                        format_func=lambda c: CERT_NAME[c],
                        index=0 if SS.cert == "mainbiz" else 1)
        if cert != SS.cert:
            SS.cert = cert
            st.rerun()
        st.markdown("---")
        menu = ["고객사", "진단", "결과 · 리포트", "증빙양식집"]
        if auth.is_admin(u):
            menu.append("관리자")
        choice = st.radio("메뉴", menu, label_visibility="collapsed")
        st.markdown("---")
        if SS.company:
            st.caption(f"작업 중  \n**{SS.company}**")
        left = auth.quota_left(u)
        st.caption("AI 사용 " + ("무제한 (관리자)" if left is None else f"잔여 {left}회 / 월 50회"))
        if st.button("로그아웃", use_container_width=True):
            SS.user = None
            st.rerun()

    {"고객사": page_company, "진단": page_diagnose,
     "결과 · 리포트": page_result, "증빙양식집": page_forms,
     "관리자": page_admin}[choice]()
