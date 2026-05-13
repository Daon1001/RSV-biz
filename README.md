# 🏆 메인비즈·이노비즈 AI 마스터 컨설턴트 v2.0

컨설턴트 내부용 메인비즈 인증 통합 관리 시스템

## ✨ v2.0 핵심 변경사항

기존 슬라이더 방식의 추상적 진단을 **객관적 측정 문항**으로 전면 개편:

### Before (v1.0)
```
전략기획 및 이행관리: [━━━━━━━━━━] 70/250점
  ↑ 컨설턴트 주관적 판단
```

### After (v2.0)
```
중장기 경영전략 수립 (70점)
  Q1. 중장기(3년 이상) 경영전략 문서가 존재합니까?
      ● 외부 컨설팅 검증을 거친 종합 전략 보유 (40점)
  Q2. 전략 수립 과정에 참여한 인원 범위는?
      ● 전 임직원 의견 수렴 (20점)
  Q3. 환경 분석(SWOT, PEST 등)을 수행했습니까?
      ● SWOT + 시장분석 + 경쟁사 분석 (10점)

  → 자동 계산: 70/70점 ✅

  📎 필요 증빙자료
    - 중장기 경영전략 문서 (필수)
    - 전략 수립 회의록
    - 시장·경쟁사 분석 자료
```

## 🎯 주요 기능

### 1. 업종별 맞춤 평가지표 (🏭 제조 / 💼 서비스 / 🏗️ 건설)
- 4개 분야 × 4개 항목 = **16개 항목, 40여 개 객관식 문항**
- 업종별 성과지표 차별화 (제조업은 불량률·생산성, 서비스업은 NPS·CSI, 건설업은 안전·공기)
- 1,000점 만점 자동 계산

### 2. 증빙자료 체크리스트
각 항목마다 현장평가 시 필요한 증빙자료를 자동 안내
- 항목별 3~5개 증빙자료 목록
- 현장평가 대응 가이드 역할

### 3. 점수 향상 우선순위 자동 도출
- 가장 큰 점수 차이가 나는 항목 TOP 5 자동 표시
- 컨설턴트가 어디부터 손대야 할지 명확

### 4. AI 컨설팅 리포트 (Claude Sonnet 4.5)
- 업종 특성 반영한 맞춤 분석
- 우선 개선 과제 TOP 3 (액션 / 방법 / 효과 / 기간)
- 증빙자료 우선순위
- 신청 전략 (시점, 평가기관 선택)

### 5. 고객사 관리 (CRM 라이트)
- 회사 정보 등록 (업종, 사업자번호, 대표 등)
- 진단 이력 보관
- 진행 인증 트래킹

### 6. 신청 워크플로우 트래커
- 메인비즈 10단계 체크리스트
- 각 단계 메모 + 완료일 기록
- 진행률 시각화

## 📁 파일 구조

```
mainnoinno/
├── app.py                  # 메인 Streamlit 앱
├── mainbiz_criteria.py     # 메인비즈 평가지표 데이터 (3개 업종)
├── requirements.txt
└── README.md
```

## 🚀 배포 방법

### 1. GitHub 레포 생성 및 업로드
```bash
git init
git add app.py mainbiz_criteria.py requirements.txt README.md
git commit -m "v2.0 - 상세 진단 문항 추가"
git remote add origin https://github.com/[YOUR_ID]/mainnoinno.git
git push -u origin main
```

### 2. Streamlit Cloud 앱 생성
1. https://share.streamlit.io 접속 → **New app**
2. Repository: `[YOUR_ID]/mainnoinno`
3. Main file: `app.py`

### 3. Secrets 설정 (⋮ → Settings → Secrets)

```toml
anthropic_api_key = "sk-ant-api03-..."
github_token = "ghp_..."
gist_id = "958084eac7f7fcb31a441dcc7d0cd7cd"
mainnoinno_users_filename = "mainnoinno_users.json"
mainnoinno_companies_filename = "mainnoinno_companies.json"
```

기존 벤처/연구소 앱과 **같은 Gist를 공유**하되 파일명만 분리.

### 4. 첫 로그인
관리자 계정: `incheon00@gmail.com` (자동 등록됨)

## 🛠️ 향후 개선 계획

- [ ] **이노비즈 모듈 추가** (메인비즈 안정화 후)
- [ ] **평가지표 정기 동기화** (GitHub Actions 크론)
- [ ] **증빙자료 PDF 업로드**
- [ ] **PDF 리포트 출력** (고객사 제출용)
- [ ] **재무비율 자동 계산**

## 💰 운영 비용

- Streamlit Cloud: 무료
- Claude API (Sonnet 4.5): 컨설팅 리포트 1건당 약 50~80원
- 월 100건 기준 약 8,000원
