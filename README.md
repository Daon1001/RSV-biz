# 🏆 메인비즈·이노비즈 AI 마스터 컨설턴트 v2.3

RSV CONSULTING · 컨설턴트 내부용 메인비즈·이노비즈 인증 통합 관리 시스템

## ✨ v2.3 업데이트 (RSV 디자인 + 보고서 + 가이드북)

### 🎨 RSV 디자인 시스템 적용
- **다크 네이비 (#0b1f52) + 골드 (#d4af37)** 럭셔리 컬러
- **Pretendard 폰트** 한국어 최적화
- **그라데이션 헤더 + 골드 보더** 프리미엄 카드
- 모든 화면에 일관된 RSV 브랜드 적용

### 📥 컨설팅 보고서 다운로드 (NEW)
진단 완료 후 **5~6페이지 A4 보고서** HTML 다운로드:
1. **표지** — 다크 네이비 + 골드 그라데이션
2. **진단 요약** — 총점, 통과 여부, 분야별 점수 분포
3. **SWOT 분석** — 강점·약점 + 우선 개선 과제 TOP 5
4. **증빙자료 체크리스트** — 현장평가 대응 가이드
5. **AI 전문가 분석** — Claude AI 컨설팅 리포트 (생성 시)
6. **유의사항 및 다음 단계** — 면책조항 + 액션플랜

> 다운로드한 HTML을 브라우저에서 열어 **Ctrl+P → PDF로 저장**하면 PDF 보고서로 변환됩니다.

### 📖 가이드북 (NEW)
메인비즈/이노비즈 각각의 완벽한 가이드북 페이지:
- 💡 **제도 개요** — 법적 근거 및 도입 취지
- ✅ **신청 자격 요건** — 4가지 필수 조건
- 📋 **신청 절차** — 7~10단계 상세 가이드
- 📊 **평가 항목** — 4개 핵심 분야 설명
- 🎓 **개별기술수준 평가** (이노비즈) — 14등급 체계 안내
- 🎁 **인증 혜택** — 금융·세제·R&D·인력·판로 등 5개 카테고리
- 💎 **합격 팁** — 컨설턴트 노하우 기반 실무 팁

## 📁 파일 구조 (5개 파일)

```
mainnoinno/
├── app.py                  # 메인 Streamlit 앱
├── mainbiz_criteria.py     # 메인비즈 평가지표 (4개 업종)
├── innobiz_criteria.py     # 이노비즈 평가지표 + 14등급 평가
├── rsv_design.py           # 🆕 RSV 디자인 + 보고서 생성 + 가이드북
├── requirements.txt
└── README.md
```

## 🎯 전체 기능

### 1. 4개 업종 맞춤 평가
🏭 제조업 · 💼 서비스업 · 🏗️ 건설업 · 💻 IT/소프트웨어업

### 2. 메인비즈 진단 (16개 항목)
전략기획 · 성과관리 · 조직인력 · ESG경영 (각 250점)

### 3. 이노비즈 진단 (16개 항목)
기술혁신능력(300) · 기술사업화(250) · 기술혁신경영(250) · 기술혁신성과(200)

### 4. 이노비즈 개별기술수준 평가 (14등급)
경영주 기술능력 · 기술성 · 시장성 · 사업성 → AAA~D 등급 산출

### 5. AI 컨설팅 리포트 (Claude Sonnet 4.5)
업종 특성 반영 + 우선 개선 과제 + 기술등급 확보 전략

### 6. 📥 컨설팅 보고서 다운로드
RSV 디자인 기반 A4 출력 가능 HTML 보고서

### 7. 📖 가이드북
메인비즈/이노비즈 각각의 완전 가이드

### 8. 고객사 관리 (CRM 라이트)
회사 정보 + 진단 이력 + 기술등급 결과 통합 관리

### 9. 신청 워크플로우 트래커
인증별 10단계 체크리스트

### 10. 통합 대시보드
메인비즈·이노비즈 통계 한눈에 확인

## 🚀 배포 방법

### 1. GitHub 레포에 6개 파일 업로드
```bash
git init
git add app.py mainbiz_criteria.py innobiz_criteria.py rsv_design.py requirements.txt README.md
git commit -m "v2.3 - RSV 디자인 + 보고서 + 가이드북"
git remote add origin https://github.com/[YOUR_ID]/mainnoinno.git
git push -u origin main
```

### 2. Streamlit Cloud Secrets 설정
```toml
anthropic_api_key = "sk-ant-api03-..."
github_token = "ghp_..."
gist_id = "958084eac7f7fcb31a441dcc7d0cd7cd"
mainnoinno_users_filename = "mainnoinno_users.json"
mainnoinno_companies_filename = "mainnoinno_companies.json"
```

## 🎨 디자인 시스템

### 컬러 팔레트
```css
--navy-dark:   #0A1628  /* 배경, 보고서 표지 */
--navy:        #0b1f52  /* 메인 브랜드 */
--navy-mid:    #1a3a7a  /* 그라데이션 중간 */
--navy-light:  #2a5298  /* 그라데이션 끝 */
--gold:        #d4af37  /* 액센트, 다운로드 버튼 */
--gold-light:  #F4D98A  /* 하이라이트 */
--gold-dark:   #8B6F3E  /* 텍스트 강조 */
```

### 보고서 구성 페이지 (A4)
```
Page 1: 표지 (다크 네이비 + 골드 그라데이션)
Page 2: Executive Summary (메트릭 카드 + 점수 분포)
Page 3: SWOT Analysis (강점/약점 + 액션 카드)
Page 4: Evidence Checklist (증빙자료 가이드)
Page 5: AI Expert Analysis (AI 리포트 생성 시)
Page 6: Disclaimer & Contact (유의사항 + 다음 단계)
```

## 💰 운영 비용

- Streamlit Cloud: 무료
- Claude API (Sonnet 4.5): 메인비즈 리포트 50~80원, 이노비즈 리포트 70~100원
- 월 100건 기준 약 8,000~12,000원

## ⚠️ 면책 조항

본 시스템의 진단 결과는 **참고용 시뮬레이션**입니다. 실제 현장평가는 평가기관(신보·기보·KPC·기술보증기금)의 전문 평가자가 별도 기준으로 진행하며, 결과가 본 시스템과 다를 수 있습니다.
