# -*- coding: utf-8 -*-
"""GitHub Gist DB 기반 인증 · 고객사 · 사용량 관리 (RSV 공통 패턴)"""

import json
from datetime import datetime

import requests
import streamlit as st

ADMIN_EMAIL = "incheon00@gmail.com"
API = "https://api.github.com/gists"
MONTHLY_LIMIT = 50


def _cfg(key, default=""):
    try:
        return st.secrets.get(key, default)
    except Exception:
        return default


def _files():
    return {
        "users": _cfg("diag_users_filename", "diag_users.json"),
        "companies": _cfg("diag_companies_filename", "diag_companies.json"),
        "usage": _cfg("diag_usage_filename", "diag_usage.json"),
    }


def _headers():
    return {"Authorization": f"token {_cfg('github_token')}",
            "Accept": "application/vnd.github+json"}


@st.cache_data(ttl=60, show_spinner=False)
def _fetch_gist():
    gid = _cfg("gist_id")
    if not gid:
        return {}
    try:
        r = requests.get(f"{API}/{gid}", headers=_headers(), timeout=15)
        r.raise_for_status()
        return r.json().get("files", {})
    except Exception:
        return {}


def load(kind):
    fname = _files()[kind]
    files = _fetch_gist()
    f = files.get(fname)
    if not f:
        return []
    try:
        content = f.get("content")
        if f.get("truncated") and f.get("raw_url"):
            content = requests.get(f["raw_url"], timeout=15).text
        return json.loads(content) if content else []
    except Exception:
        return []


def save(kind, data):
    gid = _cfg("gist_id")
    if not gid:
        st.error("gist_id 시크릿이 설정되지 않았습니다.")
        return False
    body = {"files": {_files()[kind]: {
        "content": json.dumps(data, ensure_ascii=False, indent=1)}}}
    try:
        r = requests.patch(f"{API}/{gid}", headers=_headers(),
                           json=body, timeout=20)
        r.raise_for_status()
        _fetch_gist.clear()
        return True
    except Exception as e:
        st.error(f"저장 실패: {e}")
        return False


# ─────────────────────────── 사용자
def ensure_admin():
    users = load("users")
    if not any(u.get("email") == ADMIN_EMAIL for u in users):
        users.append(dict(email=ADMIN_EMAIL, name="관리자", company="중소기업경영지원단",
                          purpose="시스템 관리", role="admin", approved=True,
                          suspended=False, created=datetime.now().isoformat(timespec="seconds")))
        save("users", users)
    return users


def find_user(email):
    email = (email or "").strip().lower()
    for u in load("users"):
        if u.get("email", "").lower() == email:
            return u
    return None


def signup(email, name, company, purpose):
    email = email.strip().lower()
    if find_user(email):
        return False, "이미 등록된 이메일입니다."
    users = load("users")
    users.append(dict(email=email, name=name, company=company, purpose=purpose,
                      role="user", approved=False, suspended=False,
                      created=datetime.now().isoformat(timespec="seconds")))
    if save("users", users):
        return True, "가입 신청이 접수되었습니다. 관리자 승인 후 이용할 수 있습니다."
    return False, "저장에 실패했습니다."


def login(email):
    u = find_user(email)
    if not u:
        return None, "등록되지 않은 이메일입니다. 먼저 가입 신청을 해주세요."
    if u.get("suspended"):
        return None, "정지된 계정입니다. 관리자에게 문의하십시오."
    if not u.get("approved"):
        return None, "승인 대기 중입니다. 관리자 승인 후 이용할 수 있습니다."
    return u, ""


def set_user(email, **kw):
    users = load("users")
    for u in users:
        if u.get("email", "").lower() == email.lower():
            u.update(kw)
    return save("users", users)


def delete_user(email):
    users = [u for u in load("users") if u.get("email", "").lower() != email.lower()]
    return save("users", users)


def is_admin(user):
    return bool(user) and (user.get("role") == "admin"
                           or user.get("email", "").lower() == ADMIN_EMAIL)


# ─────────────────────────── 고객사 · 진단 이력
def list_companies(owner=None):
    rows = load("companies")
    if owner:
        rows = [r for r in rows if r.get("owner", "").lower() == owner.lower()]
    return sorted(rows, key=lambda r: r.get("updated", ""), reverse=True)


def upsert_company(owner, name, biz_no="", industry="", note="",
                   answers=None, total=None, prefix=""):
    rows = load("companies")
    now = datetime.now().isoformat(timespec="seconds")
    hit = None
    for r in rows:
        if r.get("owner", "").lower() == owner.lower() and r.get("name") == name:
            hit = r
            break
    if hit is None:
        hit = dict(owner=owner, name=name, created=now)
        rows.append(hit)
    hit.update(biz_no=biz_no, industry=industry, note=note, prefix=prefix, updated=now)
    if answers is not None:
        hit["answers"] = {str(k): int(v) for k, v in answers.items()}
    if total is not None:
        hit["total"] = round(float(total), 1)
    return save("companies", rows)


def delete_company(owner, name):
    rows = [r for r in load("companies")
            if not (r.get("owner", "").lower() == owner.lower() and r.get("name") == name)]
    return save("companies", rows)


# ─────────────────────────── 사용량
PRICE = {  # USD per 1M tokens (in, out)
    "claude-haiku-4-5-20251001": (1.0, 5.0),
    "claude-sonnet-4-6": (3.0, 15.0),
    "claude-opus-4-7": (5.0, 25.0),
}


def log_usage(email, model, tin, tout, action):
    pin, pout = PRICE.get(model, (3.0, 15.0))
    cost = tin / 1e6 * pin + tout / 1e6 * pout
    rows = load("usage")
    rows.append(dict(timestamp=datetime.now().isoformat(timespec="seconds"),
                     email=email, model=model, input_tokens=tin,
                     output_tokens=tout, cost_usd=round(cost, 6), action=action))
    save("usage", rows)
    return cost


def month_count(email):
    tag = datetime.now().strftime("%Y-%m")
    return sum(1 for r in load("usage")
               if r.get("email", "").lower() == (email or "").lower()
               and str(r.get("timestamp", "")).startswith(tag))


def quota_left(user):
    if is_admin(user):
        return None
    return max(0, MONTHLY_LIMIT - month_count(user.get("email", "")))
