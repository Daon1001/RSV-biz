"""
이노비즈 상세 평가문항 데이터
- 4개 분야 × 4개 항목 × 업종별(제조/서비스/건설) 세부 진단 문항
- 시스템 평가 1,000점 + 개별기술수준 14등급 평가 별도
- 자가진단 650점 + 현장평가 700점 + 기술등급 B 이상 모두 통과해야 인증
"""

# =====================================================================
# 분야 1: 기술혁신능력 (300점) — 업종 공통 (R&D 조직·인력·투자·IP)
# =====================================================================

INNOVATION_ITEMS = {
    "i1": {
        "category": "innovation",
        "category_name": "기술혁신능력",
        "name": "연구개발(R&D) 조직 운영",
        "max": 70,
        "questions": [
            {
                "id": "i1_q1",
                "text": "별도의 연구개발 조직(부설연구소, R&D팀)을 보유하고 있습니까?",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "비공식 TF 운영", "score": 10},
                    {"label": "사내 R&D 부서 설치", "score": 25},
                    {"label": "기업부설연구소 또는 연구개발전담부서 인정", "score": 40},
                ]
            },
            {
                "id": "i1_q2",
                "text": "R&D 조직의 운영 체계는?",
                "type": "single",
                "options": [
                    {"label": "체계 없음", "score": 0},
                    {"label": "프로젝트별 임시 운영", "score": 5},
                    {"label": "연간 R&D 계획 + 정기 회의", "score": 15},
                    {"label": "R&D 로드맵 + 단계별 게이트 관리", "score": 30},
                ]
            },
        ],
        "evidences": [
            "기업부설연구소·전담부서 인정서 (필수)",
            "R&D 조직도",
            "R&D 운영 규정·매뉴얼",
            "R&D 로드맵 문서",
        ]
    },
    "i2": {
        "category": "innovation",
        "category_name": "기술혁신능력",
        "name": "연구전담인력 보유",
        "max": 80,
        "questions": [
            {
                "id": "i2_q1",
                "text": "연구전담요원(인정 받은 연구원) 수는?",
                "type": "single",
                "options": [
                    {"label": "0명", "score": 0},
                    {"label": "1명", "score": 20},
                    {"label": "2명", "score": 35},
                    {"label": "3~5명", "score": 50},
                    {"label": "6명 이상", "score": 60},
                ]
            },
            {
                "id": "i2_q2",
                "text": "연구인력의 학위 보유 현황은? (중복 가능)",
                "type": "multi",
                "options": [
                    {"label": "박사 1명 이상", "score": 10},
                    {"label": "석사 2명 이상", "score": 5},
                    {"label": "관련 분야 기술자격증 보유", "score": 5},
                ]
            },
        ],
        "evidences": [
            "연구전담요원 명부 (필수)",
            "재직증명서",
            "학위증·자격증 사본",
            "4대보험 가입 내역",
        ]
    },
    "i3": {
        "category": "innovation",
        "category_name": "기술혁신능력",
        "name": "R&D 투자 비율",
        "max": 80,
        "questions": [
            {
                "id": "i3_q1",
                "text": "최근 3년 평균 매출액 대비 R&D 투자 비율은? (이노비즈 핵심지표)",
                "type": "single",
                "options": [
                    {"label": "1% 미만", "score": 0},
                    {"label": "1~2%", "score": 15},
                    {"label": "2~3%", "score": 30},
                    {"label": "3~5%", "score": 45},
                    {"label": "5% 이상", "score": 60},
                ]
            },
            {
                "id": "i3_q2",
                "text": "R&D 투자비 추이는?",
                "type": "single",
                "options": [
                    {"label": "감소 추세", "score": 0},
                    {"label": "정체", "score": 5},
                    {"label": "증가 추세 (3년 연속)", "score": 20},
                ]
            },
        ],
        "evidences": [
            "최근 3년 R&D 투자비 내역 (인건비+재료비+감가상각비)",
            "연구개발비 세액공제 신청 자료",
            "재무제표상 연구개발비 계정",
            "정부 R&D 과제 수행 실적",
        ]
    },
    "i4": {
        "category": "innovation",
        "category_name": "기술혁신능력",
        "name": "지식재산권 보유 현황",
        "max": 70,
        "questions": [
            {
                "id": "i4_q1",
                "text": "특허(등록·출원) 보유 현황은?",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "출원 1~2건", "score": 10},
                    {"label": "등록 1~2건", "score": 20},
                    {"label": "등록 3~5건", "score": 30},
                    {"label": "등록 6건 이상 (해외특허 포함)", "score": 40},
                ]
            },
            {
                "id": "i4_q2",
                "text": "보유한 기타 지식재산권은? (중복 가능)",
                "type": "multi",
                "options": [
                    {"label": "실용신안 등록", "score": 10},
                    {"label": "디자인권 등록", "score": 5},
                    {"label": "상표권 등록", "score": 5},
                    {"label": "소프트웨어 저작권", "score": 10},
                ]
            },
        ],
        "evidences": [
            "특허·실용신안 등록증 (필수, 다수 보유 시 가점)",
            "특허 출원 접수증",
            "지식재산권 일람표",
            "기술료 수입 내역 (해당 시)",
        ]
    },
}

# =====================================================================
# 분야 2: 기술사업화능력 (250점) — 업종별 차이 발생
# =====================================================================

COMMERCIAL_ITEMS_MFG = {
    "c1": {
        "category": "commercialization",
        "category_name": "기술사업화능력",
        "name": "기술의 시장성 (제조업)",
        "max": 70,
        "questions": [
            {
                "id": "c1_q1",
                "text": "주력 제품·기술의 시장 위치는?",
                "type": "single",
                "options": [
                    {"label": "범용·저부가가치 시장", "score": 0},
                    {"label": "일반 경쟁시장", "score": 15},
                    {"label": "특화 틈새시장", "score": 30},
                    {"label": "독점적·차별화 시장 (기술선도)", "score": 45},
                ]
            },
            {
                "id": "c1_q2",
                "text": "주요 거래처 다변화 정도는?",
                "type": "single",
                "options": [
                    {"label": "특정 1개사 매출 비중 70% 이상", "score": 0},
                    {"label": "특정사 50~70%", "score": 10},
                    {"label": "균형 분산 (최대 50% 이하)", "score": 25},
                ]
            },
        ],
        "evidences": [
            "시장 분석 보고서",
            "주요 거래처 매출 비중표",
            "경쟁사 비교 자료",
            "주요 거래처 거래계약서",
        ]
    },
    "c2": {
        "category": "commercialization",
        "category_name": "기술사업화능력",
        "name": "사업화 계획 수립",
        "max": 60,
        "questions": [
            {
                "id": "c2_q1",
                "text": "신제품·신기술 사업화 계획서가 있습니까?",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "구두 수준", "score": 10},
                    {"label": "문서화 + 재무계획 포함", "score": 25},
                    {"label": "문서화 + 마일스톤 + KPI 설정", "score": 40},
                ]
            },
            {
                "id": "c2_q2",
                "text": "사업화 추진 조직(TFT 등)이 운영됩니까?",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "비공식 운영", "score": 5},
                    {"label": "공식 TF + 정기회의", "score": 20},
                ]
            },
        ],
        "evidences": [
            "신제품·신기술 사업화 계획서",
            "사업화 TF 조직도 및 회의록",
            "마일스톤 및 KPI 정의서",
        ]
    },
    "c3": {
        "category": "commercialization",
        "category_name": "기술사업화능력",
        "name": "신제품 매출 비중 (제조업)",
        "max": 70,
        "questions": [
            {
                "id": "c3_q1",
                "text": "최근 3년 내 출시 신제품의 매출 비중은? (제조업)",
                "type": "single",
                "options": [
                    {"label": "10% 미만", "score": 0},
                    {"label": "10~20%", "score": 20},
                    {"label": "20~40%", "score": 35},
                    {"label": "40% 이상", "score": 50},
                ]
            },
            {
                "id": "c3_q2",
                "text": "주력 제품의 라이프사이클 단계는?",
                "type": "single",
                "options": [
                    {"label": "쇠퇴기 (대안 미보유)", "score": 0},
                    {"label": "성숙기", "score": 10},
                    {"label": "성장기", "score": 20},
                ]
            },
        ],
        "evidences": [
            "신제품 매출 분석표 (최근 3년)",
            "제품군별 매출 비중표",
            "제품 출시 일자별 매출 자료",
        ]
    },
    "c4": {
        "category": "commercialization",
        "category_name": "기술사업화능력",
        "name": "사업화 인프라 (제조업)",
        "max": 50,
        "questions": [
            {
                "id": "c4_q1",
                "text": "생산설비·시설 보유 수준은?",
                "type": "single",
                "options": [
                    {"label": "외주 의존", "score": 0},
                    {"label": "기본 설비만", "score": 10},
                    {"label": "자체 생산라인 보유", "score": 20},
                    {"label": "자동화·스마트팩토리 구축", "score": 30},
                ]
            },
            {
                "id": "c4_q2",
                "text": "품질·인증 보유 현황은? (중복 가능)",
                "type": "multi",
                "options": [
                    {"label": "ISO 9001", "score": 5},
                    {"label": "KS / Q마크 / NEP·NET", "score": 10},
                    {"label": "해외 인증 (CE, UL, FDA 등)", "score": 10},
                ]
            },
        ],
        "evidences": [
            "생산설비 보유 목록 및 사진",
            "ISO 9001 인증서",
            "KS·NEP·NET 인증서 (해당 시)",
            "해외 인증서 (해당 시)",
        ]
    },
}

COMMERCIAL_ITEMS_SVC = {
    "c1": {
        "category": "commercialization",
        "category_name": "기술사업화능력",
        "name": "기술의 시장성 (서비스업)",
        "max": 70,
        "questions": [
            {
                "id": "c1_q1",
                "text": "주력 서비스의 시장 위치는?",
                "type": "single",
                "options": [
                    {"label": "범용 서비스 (가격 경쟁)", "score": 0},
                    {"label": "일반 경쟁시장", "score": 15},
                    {"label": "특화 영역 (전문성 보유)", "score": 30},
                    {"label": "독점적·차별화 서비스", "score": 45},
                ]
            },
            {
                "id": "c1_q2",
                "text": "주요 고객 다변화 정도는?",
                "type": "single",
                "options": [
                    {"label": "특정 1개사 매출 70% 이상", "score": 0},
                    {"label": "특정사 50~70%", "score": 10},
                    {"label": "균형 분산 (B2B+B2C 또는 다양한 산업군)", "score": 25},
                ]
            },
        ],
        "evidences": [
            "서비스 시장 분석 보고서",
            "주요 고객 매출 비중표",
            "경쟁 서비스 비교 자료",
        ]
    },
    "c2": {
        "category": "commercialization",
        "category_name": "기술사업화능력",
        "name": "사업화 계획 수립",
        "max": 60,
        "questions": [
            {
                "id": "c2_q1",
                "text": "신규 서비스 출시 계획서가 있습니까?",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "구두 수준", "score": 10},
                    {"label": "문서화 + 재무계획 포함", "score": 25},
                    {"label": "문서화 + 마일스톤 + KPI 설정", "score": 40},
                ]
            },
            {
                "id": "c2_q2",
                "text": "신서비스 추진 조직이 운영됩니까?",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "비공식 운영", "score": 5},
                    {"label": "공식 TF + 정기회의", "score": 20},
                ]
            },
        ],
        "evidences": [
            "신규 서비스 출시 계획서",
            "사업화 TF 조직도 및 회의록",
            "마일스톤 및 KPI 정의서",
        ]
    },
    "c3": {
        "category": "commercialization",
        "category_name": "기술사업화능력",
        "name": "신규 서비스 매출 비중 (서비스업)",
        "max": 70,
        "questions": [
            {
                "id": "c3_q1",
                "text": "최근 3년 내 출시 신서비스의 매출 비중은? (서비스업)",
                "type": "single",
                "options": [
                    {"label": "10% 미만", "score": 0},
                    {"label": "10~25%", "score": 20},
                    {"label": "25~50%", "score": 35},
                    {"label": "50% 이상", "score": 50},
                ]
            },
            {
                "id": "c3_q2",
                "text": "주력 서비스의 시장 단계는?",
                "type": "single",
                "options": [
                    {"label": "쇠퇴기 (대안 미보유)", "score": 0},
                    {"label": "성숙기", "score": 10},
                    {"label": "성장기 (신규 고객 유입 활발)", "score": 20},
                ]
            },
        ],
        "evidences": [
            "신규 서비스 매출 분석표 (최근 3년)",
            "서비스별 매출 비중표",
            "신규 서비스 출시 이력",
        ]
    },
    "c4": {
        "category": "commercialization",
        "category_name": "기술사업화능력",
        "name": "사업화 인프라 (서비스업)",
        "max": 50,
        "questions": [
            {
                "id": "c4_q1",
                "text": "서비스 제공 인프라 수준은?",
                "type": "single",
                "options": [
                    {"label": "기본 인프라만", "score": 0},
                    {"label": "자체 IT시스템·플랫폼 보유", "score": 15},
                    {"label": "자체 플랫폼 + 자동화 시스템", "score": 25},
                    {"label": "AI·빅데이터 등 첨단기술 적용", "score": 30},
                ]
            },
            {
                "id": "c4_q2",
                "text": "서비스 품질·인증 보유 현황은? (중복 가능)",
                "type": "multi",
                "options": [
                    {"label": "ISO 9001", "score": 5},
                    {"label": "ISO 27001 (정보보안)", "score": 10},
                    {"label": "서비스품질·고객만족경영 인증", "score": 10},
                ]
            },
        ],
        "evidences": [
            "서비스 인프라 구성도",
            "ISO 9001/27001 인증서 (해당 시)",
            "자체 시스템·플랫폼 화면 캡처",
            "서비스 운영 매뉴얼",
        ]
    },
}

COMMERCIAL_ITEMS_CON = {
    "c1": {
        "category": "commercialization",
        "category_name": "기술사업화능력",
        "name": "기술의 시장성 (건설업)",
        "max": 70,
        "questions": [
            {
                "id": "c1_q1",
                "text": "보유 시공기술의 시장 위치는?",
                "type": "single",
                "options": [
                    {"label": "범용 시공기술", "score": 0},
                    {"label": "일반 경쟁시장", "score": 15},
                    {"label": "특화 공법 보유", "score": 30},
                    {"label": "독점적·신공법 보유 (NET·NEP 등)", "score": 45},
                ]
            },
            {
                "id": "c1_q2",
                "text": "주요 발주처 다변화 정도는?",
                "type": "single",
                "options": [
                    {"label": "특정 발주처 70% 이상", "score": 0},
                    {"label": "특정사 50~70%", "score": 10},
                    {"label": "공공·민간 균형 분산", "score": 25},
                ]
            },
        ],
        "evidences": [
            "주요 시공실적 일람표",
            "발주처별 수주 비중표",
            "신공법·NET 인증서 (해당 시)",
            "기술 특허 (시공법 관련)",
        ]
    },
    "c2": {
        "category": "commercialization",
        "category_name": "기술사업화능력",
        "name": "사업화 계획 수립",
        "max": 60,
        "questions": [
            {
                "id": "c2_q1",
                "text": "신공법·신기술 적용 계획이 있습니까?",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "현장별 적용 시도", "score": 10},
                    {"label": "문서화된 적용 계획 + 검증 절차", "score": 25},
                    {"label": "신공법 개발·적용 로드맵 보유", "score": 40},
                ]
            },
            {
                "id": "c2_q2",
                "text": "기술 적용 추진 조직(기술팀)이 운영됩니까?",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "현장별 임시", "score": 5},
                    {"label": "공식 기술팀 + 정기회의", "score": 20},
                ]
            },
        ],
        "evidences": [
            "신공법 적용 계획서",
            "기술팀 조직도 및 회의록",
            "기술 적용 검증 절차서",
        ]
    },
    "c3": {
        "category": "commercialization",
        "category_name": "기술사업화능력",
        "name": "신공법 적용 비중 (건설업)",
        "max": 70,
        "questions": [
            {
                "id": "c3_q1",
                "text": "최근 3년 내 적용한 신공법·신기술의 매출 비중은?",
                "type": "single",
                "options": [
                    {"label": "10% 미만", "score": 0},
                    {"label": "10~20%", "score": 20},
                    {"label": "20~40%", "score": 35},
                    {"label": "40% 이상", "score": 50},
                ]
            },
            {
                "id": "c3_q2",
                "text": "주력 시공 분야의 시장 단계는?",
                "type": "single",
                "options": [
                    {"label": "포화·하락기", "score": 0},
                    {"label": "안정기", "score": 10},
                    {"label": "성장기 (스마트건설·친환경 등)", "score": 20},
                ]
            },
        ],
        "evidences": [
            "신공법 적용 실적 및 매출 자료",
            "시공실적증명서",
            "공사별 적용 기술 분석표",
        ]
    },
    "c4": {
        "category": "commercialization",
        "category_name": "기술사업화능력",
        "name": "사업화 인프라 (건설업)",
        "max": 50,
        "questions": [
            {
                "id": "c4_q1",
                "text": "시공 인프라 수준은?",
                "type": "single",
                "options": [
                    {"label": "외주·임대 의존", "score": 0},
                    {"label": "기본 장비 보유", "score": 10},
                    {"label": "전문 장비·기계 자체 보유", "score": 20},
                    {"label": "BIM·스마트건설 도입", "score": 30},
                ]
            },
            {
                "id": "c4_q2",
                "text": "건설 관련 인증·등급 보유 현황은? (중복 가능)",
                "type": "multi",
                "options": [
                    {"label": "ISO 9001", "score": 5},
                    {"label": "시공능력평가 상위 30% 이내", "score": 10},
                    {"label": "건설신기술·NET·NEP 보유", "score": 10},
                ]
            },
        ],
        "evidences": [
            "보유 장비·기계 목록",
            "시공능력평가서",
            "ISO 9001 인증서",
            "건설신기술·NET 지정서 (해당 시)",
            "BIM 적용 사례",
        ]
    },
}

# =====================================================================
# 분야 3: 기술혁신경영능력 (250점) — 업종 공통
# =====================================================================

MANAGEMENT_ITEMS = {
    "m1": {
        "category": "management",
        "category_name": "기술혁신경영능력",
        "name": "기술전략 수립",
        "max": 60,
        "questions": [
            {
                "id": "m1_q1",
                "text": "중장기 기술전략·기술로드맵을 보유하고 있습니까?",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "단순 R&D 과제 목록만", "score": 10},
                    {"label": "기술로드맵 문서 보유", "score": 25},
                    {"label": "TRM + 정기 갱신 + 경영전략 연계", "score": 40},
                ]
            },
            {
                "id": "m1_q2",
                "text": "기술전략 검토·갱신 주기는?",
                "type": "single",
                "options": [
                    {"label": "갱신 안 함", "score": 0},
                    {"label": "비정기", "score": 5},
                    {"label": "연 1회 이상 정기 갱신", "score": 20},
                ]
            },
        ],
        "evidences": [
            "기술로드맵(TRM) 문서 (필수)",
            "기술전략 수립 회의록",
            "경영전략·기술전략 연계 문서",
        ]
    },
    "m2": {
        "category": "management",
        "category_name": "기술혁신경영능력",
        "name": "기술 정보화 수준",
        "max": 60,
        "questions": [
            {
                "id": "m2_q1",
                "text": "기술자료 관리 시스템을 운영합니까? (ERP/PLM/문서관리 등)",
                "type": "single",
                "options": [
                    {"label": "수기·엑셀 관리", "score": 0},
                    {"label": "기본 문서관리 시스템", "score": 10},
                    {"label": "ERP 또는 PLM 도입", "score": 25},
                    {"label": "통합 정보시스템 (ERP+PLM+MES)", "score": 40},
                ]
            },
            {
                "id": "m2_q2",
                "text": "기술자료 백업·보안 체계가 있습니까?",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "기본 백업만", "score": 10},
                    {"label": "정기 백업 + 접근권한 관리", "score": 20},
                ]
            },
        ],
        "evidences": [
            "ERP/PLM 시스템 화면",
            "기술자료 관리 규정",
            "백업·보안 정책 문서",
            "정보시스템 도입·운영 내역",
        ]
    },
    "m3": {
        "category": "management",
        "category_name": "기술혁신경영능력",
        "name": "품질관리 체계",
        "max": 70,
        "questions": [
            {
                "id": "m3_q1",
                "text": "품질관리 체계 수준은?",
                "type": "single",
                "options": [
                    {"label": "체계 없음", "score": 0},
                    {"label": "검사 위주", "score": 10},
                    {"label": "공정관리 + 통계적 관리(SPC)", "score": 25},
                    {"label": "TQM·6시그마 등 전사 품질경영", "score": 45},
                ]
            },
            {
                "id": "m3_q2",
                "text": "품질 관련 인증 보유 (중복 가능)",
                "type": "multi",
                "options": [
                    {"label": "ISO 9001", "score": 10},
                    {"label": "ISO 14001 / 45001", "score": 5},
                    {"label": "Single PPM·6시그마 등", "score": 10},
                ]
            },
        ],
        "evidences": [
            "ISO 인증서",
            "품질매뉴얼·절차서",
            "품질관리 활동 기록 (Single PPM 등)",
            "공정관리·SPC 운영 자료",
        ]
    },
    "m4": {
        "category": "management",
        "category_name": "기술혁신경영능력",
        "name": "기술협력 네트워크",
        "max": 60,
        "questions": [
            {
                "id": "m4_q1",
                "text": "외부 기술협력 실적은? (최근 3년)",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "1~2건", "score": 10},
                    {"label": "3~5건", "score": 20},
                    {"label": "6건 이상 또는 정기 협력체계 보유", "score": 35},
                ]
            },
            {
                "id": "m4_q2",
                "text": "협력 대상은? (중복 가능)",
                "type": "multi",
                "options": [
                    {"label": "대학·연구기관", "score": 10},
                    {"label": "타 기업 (협력 R&D)", "score": 8},
                    {"label": "해외 기관·기업", "score": 7},
                ]
            },
        ],
        "evidences": [
            "산학협력·기술이전 계약서",
            "공동연구 협약서",
            "정부 R&D 컨소시엄 참여 실적",
            "해외 협력 MOU·계약서",
        ]
    },
}

# =====================================================================
# 분야 4: 기술혁신성과 (200점) — 업종별 차이
# =====================================================================

ACHIEVEMENT_ITEMS_MFG = {
    "a1": {
        "category": "achievement",
        "category_name": "기술혁신성과",
        "name": "매출액 증가율 (제조업)",
        "max": 60,
        "questions": [
            {
                "id": "a1_q1",
                "text": "최근 3년 매출액 연평균 증가율은? (제조업 기준)",
                "type": "single",
                "options": [
                    {"label": "마이너스", "score": 0},
                    {"label": "0~5%", "score": 15},
                    {"label": "5~15%", "score": 30},
                    {"label": "15% 이상", "score": 45},
                ]
            },
            {
                "id": "a1_q2",
                "text": "기술집약 제품의 매출 비중 추이는?",
                "type": "single",
                "options": [
                    {"label": "감소 또는 정체", "score": 0},
                    {"label": "증가 추세", "score": 15},
                ]
            },
        ],
        "evidences": [
            "최근 3년 재무제표 (국세청 신고분)",
            "매출액 증가 추이표",
            "제품군별 매출 분석",
        ]
    },
    "a2": {
        "category": "achievement",
        "category_name": "기술혁신성과",
        "name": "수익성 — 영업이익률 (제조업)",
        "max": 50,
        "questions": [
            {
                "id": "a2_q1",
                "text": "최근 영업이익률은? (제조업 평균 5% 기준)",
                "type": "single",
                "options": [
                    {"label": "영업적자", "score": 0},
                    {"label": "0~3%", "score": 10},
                    {"label": "3~7%", "score": 25},
                    {"label": "7% 이상", "score": 35},
                ]
            },
            {
                "id": "a2_q2",
                "text": "부채비율 수준은?",
                "type": "single",
                "options": [
                    {"label": "300% 이상", "score": 0},
                    {"label": "200~300%", "score": 5},
                    {"label": "100~200%", "score": 10},
                    {"label": "100% 미만", "score": 15},
                ]
            },
        ],
        "evidences": [
            "최근 3년 손익계산서",
            "재무상태표 (부채비율 계산)",
            "수익성 분석 자료",
        ]
    },
    "a3": {
        "category": "achievement",
        "category_name": "기술혁신성과",
        "name": "고용 증가율",
        "max": 40,
        "questions": [
            {
                "id": "a3_q1",
                "text": "최근 3년 임직원 수 변화는?",
                "type": "single",
                "options": [
                    {"label": "감소", "score": 0},
                    {"label": "정체", "score": 5},
                    {"label": "10% 미만 증가", "score": 15},
                    {"label": "10% 이상 증가", "score": 25},
                ]
            },
            {
                "id": "a3_q2",
                "text": "연구인력 증가율은?",
                "type": "single",
                "options": [
                    {"label": "감소 또는 정체", "score": 0},
                    {"label": "증가", "score": 15},
                ]
            },
        ],
        "evidences": [
            "고용보험 가입자 명부 (최근 3년)",
            "연구전담요원 변동 내역",
            "급여대장 (확인용)",
        ]
    },
    "a4": {
        "category": "achievement",
        "category_name": "기술혁신성과",
        "name": "기술인증·수상실적",
        "max": 50,
        "questions": [
            {
                "id": "a4_q1",
                "text": "기술 관련 정부 인증·지정 보유는? (중복 가능)",
                "type": "multi",
                "options": [
                    {"label": "벤처기업 확인", "score": 10},
                    {"label": "기업부설연구소", "score": 10},
                    {"label": "NET·NEP·녹색기술 등", "score": 15},
                ]
            },
            {
                "id": "a4_q2",
                "text": "기술 관련 수상실적은? (최근 3년)",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "지자체·협회 수상", "score": 5},
                    {"label": "정부 부처·장관 수상", "score": 15},
                ]
            },
        ],
        "evidences": [
            "벤처기업 확인서, 부설연구소 인정서",
            "NET·NEP 지정서",
            "수상 증서",
            "기술인증 일람표",
        ]
    },
}

ACHIEVEMENT_ITEMS_SVC = {
    "a1": {
        "category": "achievement",
        "category_name": "기술혁신성과",
        "name": "매출액 증가율 (서비스업)",
        "max": 60,
        "questions": [
            {
                "id": "a1_q1",
                "text": "최근 3년 매출액 연평균 증가율은? (서비스업 기준)",
                "type": "single",
                "options": [
                    {"label": "마이너스", "score": 0},
                    {"label": "0~10%", "score": 15},
                    {"label": "10~20%", "score": 30},
                    {"label": "20% 이상", "score": 45},
                ]
            },
            {
                "id": "a1_q2",
                "text": "신규 서비스 매출 비중 추이는?",
                "type": "single",
                "options": [
                    {"label": "감소 또는 정체", "score": 0},
                    {"label": "증가 추세", "score": 15},
                ]
            },
        ],
        "evidences": [
            "최근 3년 재무제표 (국세청 신고분)",
            "매출액 증가 추이표",
            "서비스별 매출 분석",
        ]
    },
    "a2": {
        "category": "achievement",
        "category_name": "기술혁신성과",
        "name": "수익성 — 영업이익률 (서비스업)",
        "max": 50,
        "questions": [
            {
                "id": "a2_q1",
                "text": "최근 영업이익률은? (서비스업 평균 7% 기준)",
                "type": "single",
                "options": [
                    {"label": "영업적자", "score": 0},
                    {"label": "0~5%", "score": 10},
                    {"label": "5~10%", "score": 25},
                    {"label": "10% 이상", "score": 35},
                ]
            },
            {
                "id": "a2_q2",
                "text": "부채비율 수준은?",
                "type": "single",
                "options": [
                    {"label": "300% 이상", "score": 0},
                    {"label": "200~300%", "score": 5},
                    {"label": "100~200%", "score": 10},
                    {"label": "100% 미만", "score": 15},
                ]
            },
        ],
        "evidences": [
            "최근 3년 손익계산서",
            "재무상태표 (부채비율 계산)",
            "수익성 분석 자료",
        ]
    },
    "a3": {
        "category": "achievement",
        "category_name": "기술혁신성과",
        "name": "고용 증가율",
        "max": 40,
        "questions": [
            {
                "id": "a3_q1",
                "text": "최근 3년 임직원 수 변화는?",
                "type": "single",
                "options": [
                    {"label": "감소", "score": 0},
                    {"label": "정체", "score": 5},
                    {"label": "10% 미만 증가", "score": 15},
                    {"label": "10% 이상 증가", "score": 25},
                ]
            },
            {
                "id": "a3_q2",
                "text": "전문인력(기술인력) 증가율은?",
                "type": "single",
                "options": [
                    {"label": "감소 또는 정체", "score": 0},
                    {"label": "증가", "score": 15},
                ]
            },
        ],
        "evidences": [
            "고용보험 가입자 명부 (최근 3년)",
            "전문인력 변동 내역",
            "급여대장 (확인용)",
        ]
    },
    "a4": {
        "category": "achievement",
        "category_name": "기술혁신성과",
        "name": "기술인증·수상실적",
        "max": 50,
        "questions": [
            {
                "id": "a4_q1",
                "text": "기술·서비스 관련 정부 인증·지정 보유는? (중복 가능)",
                "type": "multi",
                "options": [
                    {"label": "벤처기업 확인", "score": 10},
                    {"label": "기업부설연구소", "score": 10},
                    {"label": "서비스품질·고객만족 우수기업 지정", "score": 15},
                ]
            },
            {
                "id": "a4_q2",
                "text": "관련 수상실적은? (최근 3년)",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "지자체·협회 수상", "score": 5},
                    {"label": "정부 부처·장관 수상", "score": 15},
                ]
            },
        ],
        "evidences": [
            "벤처기업 확인서, 부설연구소 인정서",
            "서비스품질 인증서",
            "수상 증서",
        ]
    },
}

ACHIEVEMENT_ITEMS_CON = {
    "a1": {
        "category": "achievement",
        "category_name": "기술혁신성과",
        "name": "매출액 증가율 (건설업)",
        "max": 60,
        "questions": [
            {
                "id": "a1_q1",
                "text": "최근 3년 매출액 연평균 증가율은? (건설업 기준)",
                "type": "single",
                "options": [
                    {"label": "마이너스", "score": 0},
                    {"label": "0~5%", "score": 15},
                    {"label": "5~10%", "score": 30},
                    {"label": "10% 이상", "score": 45},
                ]
            },
            {
                "id": "a1_q2",
                "text": "신공법·신기술 적용 매출 비중 추이는?",
                "type": "single",
                "options": [
                    {"label": "감소 또는 정체", "score": 0},
                    {"label": "증가 추세", "score": 15},
                ]
            },
        ],
        "evidences": [
            "최근 3년 재무제표 (국세청 신고분)",
            "시공능력평가서",
            "공사별 매출 분석",
        ]
    },
    "a2": {
        "category": "achievement",
        "category_name": "기술혁신성과",
        "name": "수익성 — 영업이익률 (건설업)",
        "max": 50,
        "questions": [
            {
                "id": "a2_q1",
                "text": "최근 영업이익률은? (건설업 평균 4% 기준)",
                "type": "single",
                "options": [
                    {"label": "영업적자", "score": 0},
                    {"label": "0~2%", "score": 10},
                    {"label": "2~5%", "score": 25},
                    {"label": "5% 이상", "score": 35},
                ]
            },
            {
                "id": "a2_q2",
                "text": "부채비율 수준은?",
                "type": "single",
                "options": [
                    {"label": "300% 이상", "score": 0},
                    {"label": "200~300%", "score": 5},
                    {"label": "100~200%", "score": 10},
                    {"label": "100% 미만", "score": 15},
                ]
            },
        ],
        "evidences": [
            "최근 3년 손익계산서",
            "재무상태표 (부채비율 계산)",
            "수익성 분석 자료",
        ]
    },
    "a3": {
        "category": "achievement",
        "category_name": "기술혁신성과",
        "name": "고용 증가율",
        "max": 40,
        "questions": [
            {
                "id": "a3_q1",
                "text": "최근 3년 임직원 수 변화는?",
                "type": "single",
                "options": [
                    {"label": "감소", "score": 0},
                    {"label": "정체", "score": 5},
                    {"label": "10% 미만 증가", "score": 15},
                    {"label": "10% 이상 증가", "score": 25},
                ]
            },
            {
                "id": "a3_q2",
                "text": "기술인력(기술자) 증가율은?",
                "type": "single",
                "options": [
                    {"label": "감소 또는 정체", "score": 0},
                    {"label": "증가", "score": 15},
                ]
            },
        ],
        "evidences": [
            "고용보험 가입자 명부 (최근 3년)",
            "기술인력 보유증명서",
            "건설기술인 등록부",
        ]
    },
    "a4": {
        "category": "achievement",
        "category_name": "기술혁신성과",
        "name": "기술인증·수상실적",
        "max": 50,
        "questions": [
            {
                "id": "a4_q1",
                "text": "건설기술 관련 정부 인증·지정은? (중복 가능)",
                "type": "multi",
                "options": [
                    {"label": "벤처기업 확인", "score": 10},
                    {"label": "기업부설연구소", "score": 10},
                    {"label": "건설신기술·NET 지정", "score": 15},
                ]
            },
            {
                "id": "a4_q2",
                "text": "관련 수상실적은? (최근 3년)",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "지자체·협회 수상", "score": 5},
                    {"label": "정부 부처·장관 수상", "score": 15},
                ]
            },
        ],
        "evidences": [
            "벤처기업 확인서, 부설연구소 인정서",
            "건설신기술 지정서",
            "수상 증서",
        ]
    },
}

# =====================================================================
# 분야 2 (IT업종): 기술사업화능력 — 소프트웨어업 특화
# =====================================================================

COMMERCIAL_ITEMS_IT = {
    "c1": {
        "category": "commercialization",
        "category_name": "기술사업화능력",
        "name": "기술의 시장성 (IT/SW업)",
        "max": 70,
        "questions": [
            {
                "id": "c1_q1",
                "text": "주력 소프트웨어·플랫폼의 시장 위치는?",
                "type": "single",
                "options": [
                    {"label": "외주개발·SI 위주 (자체 솔루션 없음)", "score": 0},
                    {"label": "일반 경쟁시장", "score": 15},
                    {"label": "특화 솔루션 (버티컬 SaaS 등)", "score": 30},
                    {"label": "독점적·차별화 (AI·플랫폼 선도)", "score": 45},
                ]
            },
            {
                "id": "c1_q2",
                "text": "주요 고객 다변화 정도는?",
                "type": "single",
                "options": [
                    {"label": "특정 1개사 매출 70% 이상", "score": 0},
                    {"label": "특정사 50~70%", "score": 10},
                    {"label": "균형 분산 (B2B SaaS 다수 고객 또는 B2C)", "score": 25},
                ]
            },
        ],
        "evidences": [
            "SW 시장 분석 보고서",
            "주요 고객/구독자 매출 비중표",
            "경쟁 솔루션 비교 자료",
            "유료 고객 리스트 (B2B SaaS)",
        ]
    },
    "c2": {
        "category": "commercialization",
        "category_name": "기술사업화능력",
        "name": "사업화 계획 수립",
        "max": 60,
        "questions": [
            {
                "id": "c2_q1",
                "text": "신규 SW·서비스 출시 계획서가 있습니까?",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "구두 수준", "score": 10},
                    {"label": "PRD/로드맵 문서 보유 + 재무계획", "score": 25},
                    {"label": "PRD + 마일스톤 + KPI/OKR 설정", "score": 40},
                ]
            },
            {
                "id": "c2_q2",
                "text": "제품 개발 조직(PM/PO + 개발팀)이 운영됩니까?",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "비공식 운영", "score": 5},
                    {"label": "공식 제품팀 + 스프린트 운영", "score": 20},
                ]
            },
        ],
        "evidences": [
            "제품 로드맵 / PRD 문서",
            "스프린트 회고록 / 데일리 스탠드업 기록",
            "제품팀 조직도",
            "마일스톤·OKR 정의서",
        ]
    },
    "c3": {
        "category": "commercialization",
        "category_name": "기술사업화능력",
        "name": "자체 솔루션 매출 비중 (IT/SW업)",
        "max": 70,
        "questions": [
            {
                "id": "c3_q1",
                "text": "자체 솔루션·SaaS 매출 비중은? (SI/외주 매출 대비)",
                "type": "single",
                "options": [
                    {"label": "10% 미만 (외주·SI 위주)", "score": 0},
                    {"label": "10~30%", "score": 20},
                    {"label": "30~60%", "score": 35},
                    {"label": "60% 이상 (자체 제품 중심)", "score": 50},
                ]
            },
            {
                "id": "c3_q2",
                "text": "주력 제품의 시장 단계는?",
                "type": "single",
                "options": [
                    {"label": "Pre-PMF (PMF 미달성)", "score": 0},
                    {"label": "PMF 달성·초기 성장", "score": 10},
                    {"label": "본격 성장기 (MoM/YoY 성장률 견조)", "score": 20},
                ]
            },
        ],
        "evidences": [
            "자체 솔루션 vs SI 매출 분석표 (최근 3년)",
            "MRR/ARR 추이 (SaaS의 경우)",
            "유료 전환율·해지율 지표",
            "신규 서비스 출시 이력",
        ]
    },
    "c4": {
        "category": "commercialization",
        "category_name": "기술사업화능력",
        "name": "사업화 인프라 (IT/SW업)",
        "max": 50,
        "questions": [
            {
                "id": "c4_q1",
                "text": "개발·운영 인프라 수준은?",
                "type": "single",
                "options": [
                    {"label": "기본 환경만 (개발만 가능)", "score": 0},
                    {"label": "CI/CD 도입 + 클라우드 운영", "score": 15},
                    {"label": "CI/CD + 모니터링·로깅 자동화", "score": 25},
                    {"label": "DevOps·SRE 체계 + IaC", "score": 30},
                ]
            },
            {
                "id": "c4_q2",
                "text": "IT/SW 인증·표준 보유 (중복 가능)",
                "type": "multi",
                "options": [
                    {"label": "ISO 9001", "score": 5},
                    {"label": "ISO 27001 (정보보안)", "score": 5},
                    {"label": "ISMS-P 인증", "score": 10},
                    {"label": "CSAP / GS인증 / SW품질인증", "score": 10},
                ]
            },
        ],
        "evidences": [
            "개발·운영 인프라 구성도 (AWS/Azure/GCP)",
            "CI/CD 파이프라인 문서",
            "ISO 27001, ISMS-P, CSAP 인증서 (해당 시)",
            "GS인증·SW품질인증서 (해당 시)",
            "보안 점검·취약점 관리 기록",
        ]
    },
}

# =====================================================================
# 분야 4 (IT업종): 기술혁신성과 — 소프트웨어업 특화
# =====================================================================

ACHIEVEMENT_ITEMS_IT = {
    "a1": {
        "category": "achievement",
        "category_name": "기술혁신성과",
        "name": "매출액 증가율 (IT/SW업)",
        "max": 60,
        "questions": [
            {
                "id": "a1_q1",
                "text": "최근 3년 매출액 연평균 증가율은? (IT업 기준)",
                "type": "single",
                "options": [
                    {"label": "마이너스", "score": 0},
                    {"label": "0~15%", "score": 15},
                    {"label": "15~30%", "score": 30},
                    {"label": "30% 이상 (고성장)", "score": 45},
                ]
            },
            {
                "id": "a1_q2",
                "text": "자체 SaaS·라이선스 매출 비중 추이는?",
                "type": "single",
                "options": [
                    {"label": "감소 또는 정체", "score": 0},
                    {"label": "증가 추세 (반복매출 확대)", "score": 15},
                ]
            },
        ],
        "evidences": [
            "최근 3년 재무제표 (국세청 신고분)",
            "매출 유형별 분석 (SI/라이선스/구독/유지보수)",
            "MRR/ARR 추이 (SaaS의 경우)",
        ]
    },
    "a2": {
        "category": "achievement",
        "category_name": "기술혁신성과",
        "name": "수익성 — 영업이익률 (IT/SW업)",
        "max": 50,
        "questions": [
            {
                "id": "a2_q1",
                "text": "최근 영업이익률은? (IT업 평균 10% 기준)",
                "type": "single",
                "options": [
                    {"label": "영업적자", "score": 0},
                    {"label": "0~7%", "score": 10},
                    {"label": "7~15%", "score": 25},
                    {"label": "15% 이상", "score": 35},
                ]
            },
            {
                "id": "a2_q2",
                "text": "부채비율 수준은?",
                "type": "single",
                "options": [
                    {"label": "300% 이상", "score": 0},
                    {"label": "200~300%", "score": 5},
                    {"label": "100~200%", "score": 10},
                    {"label": "100% 미만", "score": 15},
                ]
            },
        ],
        "evidences": [
            "최근 3년 손익계산서",
            "재무상태표 (부채비율 계산)",
            "수익성 분석 자료",
        ]
    },
    "a3": {
        "category": "achievement",
        "category_name": "기술혁신성과",
        "name": "고용 증가율 — 개발인력 중심",
        "max": 40,
        "questions": [
            {
                "id": "a3_q1",
                "text": "최근 3년 임직원 수 변화는?",
                "type": "single",
                "options": [
                    {"label": "감소", "score": 0},
                    {"label": "정체", "score": 5},
                    {"label": "10% 미만 증가", "score": 15},
                    {"label": "10% 이상 증가", "score": 25},
                ]
            },
            {
                "id": "a3_q2",
                "text": "개발·연구인력(R&D 인력) 증가율은?",
                "type": "single",
                "options": [
                    {"label": "감소 또는 정체", "score": 0},
                    {"label": "증가 (전체 인력의 50% 이상)", "score": 15},
                ]
            },
        ],
        "evidences": [
            "고용보험 가입자 명부 (최근 3년)",
            "개발·연구인력 변동 내역",
            "직군별 인력 구성표",
        ]
    },
    "a4": {
        "category": "achievement",
        "category_name": "기술혁신성과",
        "name": "기술인증·수상실적 (IT/SW업)",
        "max": 50,
        "questions": [
            {
                "id": "a4_q1",
                "text": "IT/SW 관련 정부 인증·지정 보유는? (중복 가능)",
                "type": "multi",
                "options": [
                    {"label": "벤처기업 확인", "score": 10},
                    {"label": "기업부설연구소", "score": 10},
                    {"label": "GS인증·SW품질인증·CSAP 등", "score": 15},
                ]
            },
            {
                "id": "a4_q2",
                "text": "기술 관련 수상실적은? (최근 3년)",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "지자체·협회 수상", "score": 5},
                    {"label": "정부 부처·장관 수상 (또는 해외 기술상)", "score": 15},
                ]
            },
        ],
        "evidences": [
            "벤처기업 확인서, 부설연구소 인정서",
            "GS인증·SW품질인증서·CSAP 인증서",
            "SW 저작권 등록증",
            "수상 증서",
        ]
    },
}

# =====================================================================
# 통합 평가지표 반환 함수
# =====================================================================

def get_innobiz_criteria(industry: str) -> dict:
    """업종별 이노비즈 평가지표 반환

    industry: 'manufacturing' | 'service' | 'construction' | 'it'
    """
    industry_commercial = {
        "manufacturing": COMMERCIAL_ITEMS_MFG,
        "service": COMMERCIAL_ITEMS_SVC,
        "construction": COMMERCIAL_ITEMS_CON,
        "it": COMMERCIAL_ITEMS_IT,
    }.get(industry, COMMERCIAL_ITEMS_MFG)

    industry_achievement = {
        "manufacturing": ACHIEVEMENT_ITEMS_MFG,
        "service": ACHIEVEMENT_ITEMS_SVC,
        "construction": ACHIEVEMENT_ITEMS_CON,
        "it": ACHIEVEMENT_ITEMS_IT,
    }.get(industry, ACHIEVEMENT_ITEMS_MFG)

    # 16개 항목 통합 (i1~i4, c1~c4, m1~m4, a1~a4)
    items = {}
    items.update(INNOVATION_ITEMS)
    items.update(industry_commercial)
    items.update(MANAGEMENT_ITEMS)
    items.update(industry_achievement)

    return {
        "version": "2026.01",
        "industry": industry,
        "industry_name": {
            "manufacturing": "제조업",
            "service": "서비스업",
            "construction": "건설업",
            "it": "IT/소프트웨어업",
        }[industry],
        "total_score": 1000,
        "self_pass": 650,  # 이노비즈는 메인비즈(600)보다 높음
        "field_pass": 700,
        "tech_grade_min": "B",  # 추가 요건: 개별기술수준 B등급 이상
        "items": items,
        "categories": [
            {"id": "innovation", "name": "기술혁신능력", "items": ["i1", "i2", "i3", "i4"]},
            {"id": "commercialization", "name": "기술사업화능력", "items": ["c1", "c2", "c3", "c4"]},
            {"id": "management", "name": "기술혁신경영능력", "items": ["m1", "m2", "m3", "m4"]},
            {"id": "achievement", "name": "기술혁신성과", "items": ["a1", "a2", "a3", "a4"]},
        ]
    }


# =====================================================================
# 개별기술수준 평가 (14등급 평가) — 이노비즈 추가 요건
# =====================================================================

TECH_GRADE_CRITERIA = {
    "version": "2026.01",
    "min_grade": "B",
    "grades": [
        "AAA", "AA", "A+", "A",
        "BBB+", "BBB", "BB+", "BB", "B+", "B",
        "CCC", "CC", "C", "D"
    ],
    "pass_grades": ["AAA", "AA", "A+", "A", "BBB+", "BBB", "BB+", "BB", "B+", "B"],
    "categories": [
        {
            "id": "ceo",
            "name": "경영주 기술능력",
            "weight": 200,
            "questions": [
                {
                    "id": "ceo_q1",
                    "text": "경영주의 관련 분야 학력은?",
                    "type": "single",
                    "options": [
                        {"label": "비전공", "score": 0},
                        {"label": "관련 학사", "score": 30},
                        {"label": "관련 석사", "score": 50},
                        {"label": "관련 박사", "score": 80},
                    ]
                },
                {
                    "id": "ceo_q2",
                    "text": "경영주의 관련 업종 경력은?",
                    "type": "single",
                    "options": [
                        {"label": "3년 미만", "score": 0},
                        {"label": "3~7년", "score": 30},
                        {"label": "7~15년", "score": 60},
                        {"label": "15년 이상", "score": 80},
                    ]
                },
                {
                    "id": "ceo_q3",
                    "text": "경영주의 기술 관련 수상·자격증은?",
                    "type": "single",
                    "options": [
                        {"label": "없음", "score": 0},
                        {"label": "1~2개", "score": 20},
                        {"label": "3개 이상", "score": 40},
                    ]
                },
            ],
        },
        {
            "id": "tech",
            "name": "기술성",
            "weight": 300,
            "questions": [
                {
                    "id": "tech_q1",
                    "text": "보유 기술의 혁신성·차별성 수준은?",
                    "type": "single",
                    "options": [
                        {"label": "범용 기술", "score": 0},
                        {"label": "개선 기술", "score": 50},
                        {"label": "차별화 기술", "score": 100},
                        {"label": "선도 기술 (특허 보유)", "score": 150},
                    ]
                },
                {
                    "id": "tech_q2",
                    "text": "기술의 완성도(상용화 단계)는?",
                    "type": "single",
                    "options": [
                        {"label": "연구단계", "score": 0},
                        {"label": "시제품", "score": 30},
                        {"label": "상용화 진행", "score": 60},
                        {"label": "상용화 완료·판매중", "score": 100},
                    ]
                },
                {
                    "id": "tech_q3",
                    "text": "기술 모방난이도는?",
                    "type": "single",
                    "options": [
                        {"label": "낮음", "score": 0},
                        {"label": "보통", "score": 25},
                        {"label": "높음 (진입장벽 보유)", "score": 50},
                    ]
                },
            ],
        },
        {
            "id": "market",
            "name": "시장성",
            "weight": 250,
            "questions": [
                {
                    "id": "market_q1",
                    "text": "목표 시장 규모는?",
                    "type": "single",
                    "options": [
                        {"label": "100억 미만", "score": 0},
                        {"label": "100~500억", "score": 40},
                        {"label": "500~3000억", "score": 80},
                        {"label": "3000억 이상", "score": 120},
                    ]
                },
                {
                    "id": "market_q2",
                    "text": "시장 성장률은?",
                    "type": "single",
                    "options": [
                        {"label": "정체·하락", "score": 0},
                        {"label": "연 5% 미만 성장", "score": 30},
                        {"label": "연 5~15% 성장", "score": 70},
                        {"label": "연 15% 이상 성장", "score": 100},
                    ]
                },
                {
                    "id": "market_q3",
                    "text": "경쟁 강도는?",
                    "type": "single",
                    "options": [
                        {"label": "치열 (다수 강자)", "score": 0},
                        {"label": "보통", "score": 15},
                        {"label": "약함 (틈새 또는 선점)", "score": 30},
                    ]
                },
            ],
        },
        {
            "id": "biz",
            "name": "사업성 및 수익성",
            "weight": 250,
            "questions": [
                {
                    "id": "biz_q1",
                    "text": "사업화 매출 실적은?",
                    "type": "single",
                    "options": [
                        {"label": "매출 없음 (연구단계)", "score": 0},
                        {"label": "초기 매출 발생", "score": 40},
                        {"label": "안정적 매출 확보", "score": 80},
                        {"label": "급성장·확대 추세", "score": 120},
                    ]
                },
                {
                    "id": "biz_q2",
                    "text": "투자수익률(ROI) 전망은?",
                    "type": "single",
                    "options": [
                        {"label": "회수 불투명", "score": 0},
                        {"label": "장기 회수 (5년 이상)", "score": 30},
                        {"label": "중기 회수 (3~5년)", "score": 60},
                        {"label": "단기 회수 (3년 이내)", "score": 80},
                    ]
                },
                {
                    "id": "biz_q3",
                    "text": "자금 조달 능력은?",
                    "type": "single",
                    "options": [
                        {"label": "외부 의존 (취약)", "score": 0},
                        {"label": "자체+융자 가능", "score": 20},
                        {"label": "투자유치·자체 자금 충분", "score": 50},
                    ]
                },
            ],
        },
    ],
}


def calculate_tech_grade(answers: dict) -> dict:
    """개별기술수준 평가 결과 산출 (14등급)"""
    total_score = 0
    for cat in TECH_GRADE_CRITERIA["categories"]:
        for q in cat["questions"]:
            q_id = q["id"]
            if q_id in answers:
                if q["type"] == "single":
                    idx = answers[q_id]
                    if isinstance(idx, int) and 0 <= idx < len(q["options"]):
                        total_score += q["options"][idx]["score"]

    # 14등급 산출 로직 (점수 구간별)
    if total_score >= 950:
        grade = "AAA"
    elif total_score >= 900:
        grade = "AA"
    elif total_score >= 850:
        grade = "A+"
    elif total_score >= 800:
        grade = "A"
    elif total_score >= 750:
        grade = "BBB+"
    elif total_score >= 700:
        grade = "BBB"
    elif total_score >= 650:
        grade = "BB+"
    elif total_score >= 600:
        grade = "BB"
    elif total_score >= 550:
        grade = "B+"
    elif total_score >= 500:
        grade = "B"
    elif total_score >= 400:
        grade = "CCC"
    elif total_score >= 300:
        grade = "CC"
    elif total_score >= 200:
        grade = "C"
    else:
        grade = "D"

    return {
        "total_score": total_score,
        "grade": grade,
        "passed": grade in TECH_GRADE_CRITERIA["pass_grades"]
    }


# calculate_item_score는 mainbiz_criteria와 공통이므로 재사용
def calculate_item_score(item: dict, answers: dict) -> int:
    """문항별 답변을 기반으로 점수 계산"""
    total = 0
    for question in item["questions"]:
        q_id = question["id"]
        if q_id not in answers:
            continue

        if question["type"] == "single":
            selected_idx = answers[q_id]
            if isinstance(selected_idx, int) and 0 <= selected_idx < len(question["options"]):
                total += question["options"][selected_idx]["score"]
        elif question["type"] == "multi":
            selected_indices = answers[q_id]
            if isinstance(selected_indices, list):
                for idx in selected_indices:
                    if 0 <= idx < len(question["options"]):
                        total += question["options"][idx]["score"]

    return min(total, item["max"])
