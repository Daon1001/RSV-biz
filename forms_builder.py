# -*- coding: utf-8 -*-
"""선택된 증빙 양식을 하나의 작성용 HTML 문서로 조립한다."""

from datetime import date
from forms_data import FORMS, FORM_CSS


def form_set(cert="mainbiz"):
    """인증 유형별 양식 목록"""
    if cert == "innobiz":
        from forms_innobiz import all_forms
        return all_forms()
    return FORMS

TOOLBAR_JS = r"""
<script>
(function(){
  var KEY = 'RSVFORM_' + (document.body.getAttribute('data-co') || 'X');
  var els = [];
  function collect(){
    els = Array.prototype.slice.call(document.querySelectorAll('[contenteditable="true"]'));
    els.forEach(function(el,i){ el.setAttribute('data-k','k'+i); });
  }
  function dump(){
    var o={}; els.forEach(function(el){ var v=el.innerHTML.trim(); if(v) o[el.getAttribute('data-k')]=v; }); return o;
  }
  function apply(o){
    els.forEach(function(el){ var k=el.getAttribute('data-k'); if(o&&o[k]!==undefined) el.innerHTML=o[k]; });
  }
  function status(t){ var s=document.getElementById('st'); if(s) s.textContent=t; }
  function time(){ var d=new Date(); return ('0'+d.getHours()).slice(-2)+':'+('0'+d.getMinutes()).slice(-2); }
  function autosave(){
    try{ localStorage.setItem(KEY, JSON.stringify(dump())); status('자동 보관됨 · '+time()); }
    catch(e){ status('자동 보관 불가 — [작성내용 저장] 버튼을 사용하세요'); }
  }
  var timer;
  document.addEventListener('input', function(e){
    if(!e.target.isContentEditable) return;
    clearTimeout(timer); timer=setTimeout(autosave,600);
  });
  document.addEventListener('paste', function(e){
    if(!e.target.isContentEditable) return;
    e.preventDefault();
    var t=(e.clipboardData||window.clipboardData).getData('text');
    document.execCommand('insertText', false, t);
  });
  document.addEventListener('keydown', function(e){
    if(e.key!=='Tab' || !e.target.isContentEditable) return;
    e.preventDefault();
    var i=els.indexOf(e.target), n=els[i+(e.shiftKey?-1:1)];
    if(n){ n.focus(); n.scrollIntoView({block:'center',behavior:'smooth'}); }
  });
  window.jumpTo=function(id){ if(!id) return; var el=document.getElementById(id); if(el) el.scrollIntoView({behavior:'smooth'}); };
  window.printOne=function(btn){
    var pg=btn.closest('.page');
    pg.classList.add('only'); document.body.classList.add('single');
    window.print();
    setTimeout(function(){ pg.classList.remove('only'); document.body.classList.remove('single'); },400);
  };
  window.printPosted=function(){
    var n=0;
    document.querySelectorAll('.page').forEach(function(p){ if(p.getAttribute('data-post')==='1'){ p.classList.add('only'); n++; } });
    if(!n){ alert('게시용 문서가 없습니다.'); return; }
    document.body.classList.add('single'); window.print();
    setTimeout(function(){ document.querySelectorAll('.page.only').forEach(function(p){p.classList.remove('only');}); document.body.classList.remove('single'); },400);
  };
  window.saveFile=function(){
    var blob=new Blob([JSON.stringify(dump(),null,1)],{type:'application/json'});
    var a=document.createElement('a');
    a.href=URL.createObjectURL(blob);
    a.download=(document.body.getAttribute('data-co')||'양식')+'_작성내용_'+new Date().toISOString().slice(0,10)+'.json';
    a.click(); status('파일로 저장했습니다');
  };
  window.loadFile=function(ev){
    var f=ev.target.files[0]; if(!f) return;
    var r=new FileReader();
    r.onload=function(){ try{ apply(JSON.parse(r.result)); autosave(); status('불러왔습니다'); }catch(e){ status('파일을 읽을 수 없습니다'); } };
    r.readAsText(f); ev.target.value='';
  };
  window.clearAll=function(){
    if(!confirm('작성한 내용을 모두 지웁니다. 계속할까요?')) return;
    els.forEach(function(el){ el.innerHTML=''; });
    try{ localStorage.removeItem(KEY); }catch(e){}
    status('모두 지웠습니다');
  };
  collect();
  try{ var s=localStorage.getItem(KEY); if(s){ apply(JSON.parse(s)); status('이전 작성내용을 불러왔습니다'); } }
  catch(e){ status('자동 보관 불가 — 파일을 PC에 내려받아 여시면 자동 보관됩니다'); }
})();
</script>
"""


def _co(name):
    """회사명 → (정식 표기, 약칭)"""
    full = name.strip()
    short = full
    for p in ("주식회사 ", "(주)", "㈜", " 주식회사"):
        short = short.replace(p, "")
    short = short.strip()
    if not full.startswith(("주식회사", "(주)", "㈜")):
        full = "주식회사 " + short
    return full, short


def selected_forms(docnos, cert="mainbiz"):
    src = form_set(cert)
    order = {f["docno"]: i for i, f in enumerate(src)}
    picked = [f for f in src if f["docno"] in set(docnos)]
    return sorted(picked, key=lambda f: order[f["docno"]])


def weak_set(result, cert="mainbiz", threshold=None):
    """보완이 필요한 문항 번호 집합"""
    weak = set()
    for v in result["sections"].values():
        for it in v["items"]:
            if cert == "innobiz":
                # idx 0=A(만점) … 4=E · C등급(2) 이하를 보완 대상으로
                if it["idx"] >= (2 if threshold is None else threshold):
                    weak.add(it["no"])
            else:
                if it["grade"] < (3 if threshold is None else threshold):
                    weak.add(it["no"])
    return weak


def recommend(result, cert="mainbiz", threshold=None):
    """진단 결과에서 등급 미달 문항에 대응하는 양식 문서번호 목록"""
    weak = weak_set(result, cert, threshold)
    return [f["docno"] for f in form_set(cert)
            if not f["qs"] or (set(f["qs"]) & weak)]


def _cover(full, short, prefix, n, posted_n, CERT="메인비즈"):
    return f"""
<div class="page cover" id="pg0">
  <div class="in">
    <div class="eyebrow">{"INNOBIZ" if CERT=="이노비즈" else "MAINBIZ"} CERTIFICATION</div>
    <h1>{"기술혁신형" if CERT=="이노비즈" else "경영혁신형"} 중소기업<br>증빙서류 양식집</h1>
    <div class="sub">{full}<br>{CERT} 현장평가 증빙 표준양식 {n}종</div>
    <div class="box">
      <p><b>사용 방법</b><br>
        ① 상단 툴바에서 문서를 선택해 화면에서 바로 입력합니다. Tab 키로 다음 칸 이동.<br>
        ② [게시용] 표시 문서 {posted_n}종은 출력 후 사내 게시판에 부착하고 <b>부착 사진</b>을 남깁니다.<br>
        ③ 나머지 양식은 작성 · 서명 후 문서번호 순으로 바인더에 편철합니다.<br>
        ④ 현장평가 당일 즉시 제출 가능한 상태여야 <b>'체계' 등급</b>이 인정됩니다.<br>
        ⑤ 회의록 · 대장류는 <b>최소 3개월분 이상 누적</b>되어야 실효성이 인정됩니다.
      </p>
    </div>
  </div>
  <div class="foot" style="border-color:#3A4A66;color:#8A96A8">
    <span>{full} · {CERT} 현장평가 대응</span><span>{date.today().strftime('%Y. %m. %d.')}</span>
  </div>
</div>"""


def _checklist(full, forms, prefix, CERT="메인비즈"):
    rows = []
    cur = None
    for f in forms:
        grp = f["docno"].split("-")[1]
        gname = {"L": "리더십 · 조직문화", "S": "혁신전략", "R": "경영자원 · 인력",
                 "O": "조직 혁신역량", "P": "제품 · 프로세스", "M": "마케팅",
                 "A": "기술혁신능력", "B": "기술사업화능력",
                 "C": "기술혁신경영능력", "D": "기술혁신성과"}.get(grp, "기타")
        if grp != cur:
            rows.append(f'<tr><td colspan="6" style="background:#0F1E3D;color:#fff;'
                        f'font-weight:700;font-size:8.5pt;padding:1.6mm 2mm">{gname}</td></tr>')
            cur = grp
        tag = ' <span class="guide">[게시용]</span>' if f["posted"] else ""
        qs = " · ".join(str(q) for q in f["qs"]) if f["qs"] else "—"
        dno = f["docno"].replace("IMP-", prefix + "-").replace("INO-", prefix + "-").replace("INO-", prefix + "-")
        rows.append(
            f'<tr><td class="no">{dno}</td><td>{f["title"]}{tag}</td>'
            f'<td class="q">{qs}</td><td class="box">☐</td>'
            f'<td class="box">{"☐" if f["posted"] else "–"}</td><td class="box">☐</td></tr>')
    return f"""
<div class="page" id="pg1">
  <div class="dochead">
    <div><div class="co">{full}</div><div class="ttl">증빙서류 준비 체크리스트</div></div>
    <div class="meta">문서번호 <b>{prefix}-CHK-01</b><br>작성일 {date.today().strftime('%Y. %m. %d.')}</div>
  </div>
  <button class="pbtn" onclick="printOne(this)">이 문서만 인쇄</button>
  <table class="chk">
    <tr><th class="no">문서번호</th><th>문서명</th><th class="q">해당문항</th>
        <th class="box">작성</th><th class="box">게시</th><th class="box">편철</th></tr>
    {''.join(rows)}
  </table>
  <div class="note">
    <b>게시판 부착 원칙</b> — 게시용 문서는 <b>직원 전원이 상시 볼 수 있는 위치</b>(사무실 주 출입구 · 현장 휴게실)에
    부착하고, 부착 상태를 사진으로 촬영해 함께 편철하십시오. 현장평가 시 <b>게시 사진 + 원본 문서</b>가
    한 세트로 제출되면 '체계' 등급 인정이 확실해집니다.
  </div>
  <div class="foot"><span>{full}</span><span>{prefix}-CHK-01</span></div>
</div>"""


def build(company, docnos, prefix=None, cert="mainbiz"):
    """회사명 + 선택 문서번호 → 작성용 HTML 문자열"""
    full, short = _co(company)
    prefix = (prefix or "DOC").upper()
    forms = selected_forms(docnos, cert)
    CERT = "이노비즈" if cert == "innobiz" else "메인비즈"
    posted_n = sum(1 for f in forms if f["posted"])

    pages = [_cover(full, short, prefix, len(forms), posted_n, CERT),
             _checklist(full, forms, prefix, CERT)]

    opts = ['<option value="pg0">00. 표지</option>',
            '<option value="pg1">00. 증빙서류 체크리스트</option>']
    for i, f in enumerate(forms):
        html = (f["html"]
                .replace("«CO_FULL»", full)
                .replace("«CO»", short)
                .replace("IMP-", prefix + "-").replace("INO-", prefix + "-")
                .replace('<div class="page', f'<div data-post="{1 if f["posted"] else 0}" class="page', 1))
        html = html.replace('<div class="dochead">', f'<div class="dochead" id="pg{i+2}">', 1)
        pages.append(html)
        tag = " ★" if f["posted"] else ""
        opts.append(f'<option value="pg{i+2}">{i+1:02d}. {f["title"]}{tag}</option>')

    toolbar = f"""
<div id="bar">
  <b>{short} 양식집</b>
  <select id="jump" onchange="jumpTo(this.value)">
    <option value="">— 문서 바로가기 —</option>
    {chr(10).join('    ' + o for o in opts)}
  </select>
  <button onclick="window.print()">전체 인쇄</button>
  <button onclick="printPosted()">★ 게시용만 인쇄</button>
  <button onclick="saveFile()">작성내용 저장</button>
  <label class="fb">불러오기<input type="file" accept=".json" onchange="loadFile(event)"></label>
  <button onclick="clearAll()">전체 지우기</button>
  <span class="st" id="st">입력한 내용은 이 브라우저에 자동 보관됩니다</span>
</div>"""

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>{full} · {CERT} 증빙서류 양식집</title>
<style>{FORM_CSS}</style>
</head>
<body data-co="{short}">
{toolbar}
{''.join(pages)}
{TOOLBAR_JS}
</body>
</html>"""
