# 🏆 메인비즈·이노비즈 AI 마스터 컨설턴트

컨설턴트 내부용 메인비즈·이노비즈 인증 통합 관리 시스템

## 🎯 주요 기능

### 1. 자가진단 시뮬레이터
- **메인비즈**: 4개 분야(전략·성과·조직·ESG) 1,000점 만점
- **이노비즈**: 4개 분야(기술혁신·사업화·경영·성과) 1,000점 만점
- 통과 기준 실시간 판정 (자가진단/현장평가)
- 항목별 점수 조정으로 시뮬레이션

### 2. 고객사 관리 (CRM 라이트)
- 회사 정보 등록 및 관리
- 진단 이력 보관
- 진행 인증 트래킹

### 3. 신청 워크플로우 트래커
- 단계별 체크리스트
- 각 단계 메모 + 완료일 기록
- 진행률 시각화

### 4. AI 컨설팅 리포트
- Claude Sonnet 4.5 기반 자동 분석
- 강점/약점/우선 개선 과제 도출
- 신청 전략 제안

### 5. 관리자 패널
- 사용자 승인 관리
- 평가지표 버전 관리

## 🚀 배포 방법 (Streamlit Cloud)

### 1단계: GitHub 레포 생성
```bash
git init
git add app.py requirements.txt README.md
git commit -m "Initial commit"
git remote add origin https://github.com/[YOUR_ID]/mainnoinno.git
git push -u origin main
```

### 2단계: Streamlit Cloud 앱 생성
1. https://share.streamlit.io 접속
2. **New app** 클릭
3. 설정:
   - Repository: `[YOUR_ID]/mainnoinno`
   - Branch: `main`
   - Main file: `app.py`
   - App URL: 원하는 이름 (예: `mainnoinno-consultant`)

### 3단계: Secrets 설정
앱 생성 후 **⋮ → Settings → Secrets** 에 입력:

```toml
anthropic_api_key = "sk-ant-api03-..."
github_token = "ghp_..."
gist_id = "958084eac7f7fcb31a441dcc7d0cd7cd"
mainnoinno_users_filename = "mainnoinno_users.json"
mainnoinno_companies_filename = "mainnoinno_companies.json"
```

**중요**: 기존 벤처/연구소 앱과 **같은 Gist ID**를 사용하되, 파일명만 분리합니다. 이로써:
- 같은 API 키/토큰을 공유
- 사용자 DB는 각 앱별로 독립
- 비용도 통합 관리

### 4단계: 초기 관리자 로그인
첫 배포 시 자동으로 `incheon00@gmail.com`이 관리자로 등록됩니다.
다른 관리자 이메일이 필요하면 `app.py`의 `get_default_users_db()` 함수에서 수정하세요.

## 📊 평가지표 정기 동기화 (향후 개발)

현재는 2026.01 버전 평가지표가 하드코딩되어 있습니다.
향후 GitHub Actions 크론으로 매주 메인비즈넷/이노비즈넷 공지를 체크하여 변경 감지 시 관리자에게 알림을 보내는 기능을 추가할 예정입니다.

## 💰 운영 비용 예상

- **Streamlit Cloud**: 무료 (Community Cloud)
- **Claude API (Sonnet 4.5)**: 컨설팅 리포트 1건당 약 30~50원
- **GitHub**: 무료 (Gist 활용)

월 100건 컨설팅 기준 약 5,000원 내외

## 🔗 관련 앱

- 벤처인증 AI 마스터 컨설턴트
- 기업부설연구소 AI 컨설턴트

모두 동일한 인증/스토리지 인프라를 공유합니다.
