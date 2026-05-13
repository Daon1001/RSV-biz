# 🏆 메인비즈·이노비즈 AI 마스터 컨설턴트 v2.4

RSV CONSULTING · 컨설턴트 내부용 통합 관리 시스템 (벤처/연구소 앱과 동일 인프라)

## ✨ v2.4 업데이트 (이메일 인증 + 사용량 추적)

벤처/연구소 앱과 동일한 **승인 시스템 + 관리자 대시보드 + 사용량 추적** 적용.

### 🔐 사용자 인증 시스템

**회원가입 (승인 신청)**
- 이메일 + 이름 + 회사명 + 사용 목적 입력
- `approved: false` 상태로 DB 저장
- 관리자 승인 전까지 로그인 불가

**로그인**
- 이메일만으로 로그인
- 정지(`suspended`) 계정 자동 차단
- 승인 대기 상태 안내

**관리자 자동 등록**
- `incheon00@gmail.com`은 첫 실행 시 자동 관리자 등록
- 관리자는 사용량 무제한

### 📊 관리자 대시보드 (4탭)

```
👑 관리자 대시보드
├── 📊 사용량 통계
│   ├── 전체 호출 / 입력·출력 토큰 / 누적 비용 (USD + KRW)
│   ├── 사용자별 비용 순위 TOP 10
│   ├── 모델별 사용 분포
│   └── 일별 추이 (최근 30일)
│
├── 👥 사용자 관리
│   ├── 승인된 사용자 목록 + 이번 달 사용 횟수
│   ├── ⛔ 정지 / ✓ 해제 버튼
│   └── 🗑️ 삭제 버튼
│
├── ✋ 승인 대기
│   ├── 가입 신청 정보 (이름·회사·목적·신청일)
│   ├── ✅ 승인 / ❌ 거부
│
└── 📜 상세 로그
    ├── 모든 API 호출 기록 (시간·사용자·모델·토큰·비용)
    ├── 사용자별 필터
    └── 📥 CSV 다운로드
```

### 💰 자동 사용량 추적

매번 AI 리포트 생성 시 자동으로 GitHub Gist에 기록:
```json
{
  "timestamp": "2026-05-13T01:30:00",
  "email": "user@example.com",
  "model": "claude-sonnet-4-6",
  "input_tokens": 1234,
  "output_tokens": 5678,
  "cost_usd": 0.089,
  "action": "메인비즈_AI리포트"
}
```

### 🤖 모델 선택 기능

진단 페이지에서 AI 리포트 생성 시 모델 선택:

| 모델 | 입력 비용 | 출력 비용 | 용도 |
|------|----------|----------|------|
| ⚡ Haiku 4.5 | $1/1M | $5/1M | 빠르고 저렴 |
| ⭐ Sonnet 4.6 | $3/1M | $15/1M | **기본 추천** |
| 👑 Opus 4.7 | $5/1M | $25/1M | 최고 품질 |

### 📈 사용량 한도

- **일반 사용자**: 월 **50회** 한도
- **관리자**: 무제한
- 매월 1일 자동 리셋
- 사이드바에 실시간 사용량 표시

## 📁 파일 구조 (6개 파일)

```
mainnoinno/
├── app.py                  # 메인 Streamlit 앱 (~1,800줄)
├── mainbiz_criteria.py     # 메인비즈 평가지표 (4개 업종)
├── innobiz_criteria.py     # 이노비즈 평가지표 + 14등급 평가
├── rsv_design.py           # RSV 디자인 + 보고서 + 가이드북
├── requirements.txt
└── README.md
```

## 🎯 전체 기능 (v2.4)

1. 🔐 **이메일 인증 + 승인 시스템**
2. 📊 **관리자 대시보드 (4탭)**
3. 💰 **자동 사용량 추적 + 비용 계산**
4. 🤖 **AI 모델 선택 (Haiku/Sonnet/Opus)**
5. 🎨 **RSV 디자인 시스템** (네이비 + 골드)
6. 📊 **4개 업종 평가** (제조·서비스·건설·IT)
7. 📥 **컨설팅 보고서 다운로드** (HTML → PDF)
8. 📖 **메인비즈/이노비즈 가이드북**
9. 🏢 **고객사 관리 (CRM)**
10. 📋 **신청 워크플로우 트래커**

## 🚀 배포 방법

### 1. GitHub에 6개 파일 업로드 (루트에 바로)
```
rsv-biz/
├── app.py
├── mainbiz_criteria.py
├── innobiz_criteria.py
├── rsv_design.py
├── requirements.txt
└── README.md
```

### 2. Streamlit Cloud Secrets 설정

```toml
anthropic_api_key = "sk-ant-api03-..."
github_token = "ghp_..."
gist_id = "958084eac7f7fcb31a441dcc7d0cd7cd"
mainnoinno_users_filename = "mainnoinno_users.json"
mainnoinno_companies_filename = "mainnoinno_companies.json"
mainnoinno_usage_filename = "mainnoinno_usage.json"
```

⚠️ **새 시크릿 추가**: `mainnoinno_usage_filename` (사용량 로그 파일명)

### 3. 첫 로그인
관리자 계정: `incheon00@gmail.com` (자동 등록됨)

## 💰 운영 비용

- Streamlit Cloud: 무료
- Claude API 사용 비용 (월 100건 기준):
  - Haiku 4.5: 약 1,500원
  - Sonnet 4.6: 약 8,000원
  - Opus 4.7: 약 15,000원

## ⚠️ 면책 조항

본 시스템의 진단 결과는 **참고용 시뮬레이션**입니다. 실제 현장평가는 평가기관(신보·기보·KPC·기술보증기금)의 전문 평가자가 별도 기준으로 진행하며, 결과가 본 시스템과 다를 수 있습니다.
