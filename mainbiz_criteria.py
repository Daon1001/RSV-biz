"""
메인비즈 상세 평가문항 데이터
- 4개 분야 × 4개 항목 × 업종별(제조/서비스/건설) 세부 진단 문항
- 각 항목은 객관적 측정 가능한 질문으로 구성
- 증빙자료 체크리스트 포함
"""

# =====================================================================
# 공통 영역: 업종 무관 (전략, 조직, ESG의 비기술 분야)
# =====================================================================

COMMON_ITEMS = {
    # ─────────────── 분야 1: 전략기획 및 이행관리 (250점) ───────────────
    "s1": {
        "category": "strategy",
        "category_name": "전략기획 및 이행관리",
        "name": "비전·미션 수립 및 공유",
        "max": 50,
        "questions": [
            {
                "id": "s1_q1",
                "text": "비전·미션이 문서화되어 있습니까?",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "구두로만 공유", "score": 10},
                    {"label": "문서화되어 있으나 게시·공유 안 함", "score": 20},
                    {"label": "문서화 + 사내 게시·공유", "score": 30},
                ]
            },
            {
                "id": "s1_q2",
                "text": "비전·미션을 임직원이 인지하고 있는 정도는?",
                "type": "single",
                "options": [
                    {"label": "대표만 인지", "score": 0},
                    {"label": "경영진까지 공유", "score": 5},
                    {"label": "전 직원 교육·공지 완료", "score": 15},
                ]
            },
            {
                "id": "s1_q3",
                "text": "비전·미션 검토·갱신 주기는?",
                "type": "single",
                "options": [
                    {"label": "갱신 안 함", "score": 0},
                    {"label": "3년 이상 주기", "score": 2},
                    {"label": "연 1회 검토", "score": 5},
                ]
            },
        ],
        "evidences": [
            "비전·미션 문서 (경영방침서, 사훈집 등)",
            "사내 게시물 사진 또는 인트라넷 캡처",
            "전사 교육·공지 회의록",
        ]
    },
    "s2": {
        "category": "strategy",
        "category_name": "전략기획 및 이행관리",
        "name": "중장기 경영전략 수립",
        "max": 70,
        "questions": [
            {
                "id": "s2_q1",
                "text": "중장기(3년 이상) 경영전략 문서가 존재합니까?",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "단순 매출목표만 있음", "score": 10},
                    {"label": "사업·재무·인력 등 종합 전략 문서 보유", "score": 30},
                    {"label": "외부 컨설팅 검증을 거친 종합 전략 보유", "score": 40},
                ]
            },
            {
                "id": "s2_q2",
                "text": "전략 수립 과정에 참여한 인원 범위는?",
                "type": "single",
                "options": [
                    {"label": "대표 단독", "score": 0},
                    {"label": "경영진 회의", "score": 10},
                    {"label": "전 임직원 의견 수렴", "score": 20},
                ]
            },
            {
                "id": "s2_q3",
                "text": "환경 분석(SWOT, PEST 등)을 수행했습니까?",
                "type": "single",
                "options": [
                    {"label": "안 함", "score": 0},
                    {"label": "간단한 SWOT만", "score": 5},
                    {"label": "SWOT + 시장분석 + 경쟁사 분석", "score": 10},
                ]
            },
        ],
        "evidences": [
            "중장기 경영전략 문서 (필수)",
            "전략 수립 회의록",
            "시장·경쟁사 분석 자료",
            "외부 컨설팅 보고서 (해당 시)",
        ]
    },
    "s3": {
        "category": "strategy",
        "category_name": "전략기획 및 이행관리",
        "name": "연간 사업계획 수립 및 실행",
        "max": 70,
        "questions": [
            {
                "id": "s3_q1",
                "text": "연간 사업계획서를 매년 작성합니까?",
                "type": "single",
                "options": [
                    {"label": "작성 안 함", "score": 0},
                    {"label": "매출 목표만 설정", "score": 10},
                    {"label": "부서별 목표·예산 포함 사업계획서", "score": 30},
                    {"label": "월별 KPI까지 분해된 사업계획서", "score": 40},
                ]
            },
            {
                "id": "s3_q2",
                "text": "사업계획 대비 실적 달성률은? (전년도 기준)",
                "type": "single",
                "options": [
                    {"label": "60% 미만", "score": 0},
                    {"label": "60~80%", "score": 10},
                    {"label": "80~100%", "score": 20},
                    {"label": "100% 이상", "score": 30},
                ]
            },
        ],
        "evidences": [
            "전년도·당해 연간 사업계획서",
            "부서별 목표·예산 배분 자료",
            "실적 대비 분석 보고서",
        ]
    },
    "s4": {
        "category": "strategy",
        "category_name": "전략기획 및 이행관리",
        "name": "전략 실행 모니터링 체계",
        "max": 60,
        "questions": [
            {
                "id": "s4_q1",
                "text": "전략 실행 점검 회의 주기는?",
                "type": "single",
                "options": [
                    {"label": "정기 점검 없음", "score": 0},
                    {"label": "연 1회", "score": 10},
                    {"label": "반기별", "score": 20},
                    {"label": "분기별 이상", "score": 30},
                ]
            },
            {
                "id": "s4_q2",
                "text": "점검 결과를 기반으로 전략을 수정·보완한 사례가 있습니까?",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "1회 이상", "score": 15},
                    {"label": "정기적으로 PDCA 사이클 가동", "score": 30},
                ]
            },
        ],
        "evidences": [
            "전략 점검 회의록 (분기별)",
            "전략 수정·보완 의사결정 문서",
            "PDCA 사이클 운영 자료",
        ]
    },

    # ─────────────── 분야 3: 조직 및 인력관리 (250점) ───────────────
    "o1": {
        "category": "organization",
        "category_name": "조직 및 인력관리",
        "name": "조직구조 및 직무체계",
        "max": 60,
        "questions": [
            {
                "id": "o1_q1",
                "text": "조직도가 명확히 정의되어 있습니까?",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "단순 부서 구분만", "score": 10},
                    {"label": "조직도 + 보고체계 명시", "score": 20},
                    {"label": "조직도 + 보고체계 + 권한·책임 매트릭스", "score": 30},
                ]
            },
            {
                "id": "o1_q2",
                "text": "직무기술서(JD)가 작성된 직무 비율은?",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "일부 직무 (50% 미만)", "score": 10},
                    {"label": "주요 직무 (50~80%)", "score": 20},
                    {"label": "전 직무 (80% 이상)", "score": 30},
                ]
            },
        ],
        "evidences": [
            "조직도 (현행)",
            "직무기술서(JD) 샘플",
            "권한·책임 매트릭스 (RACI 등)",
        ]
    },
    "o2": {
        "category": "organization",
        "category_name": "조직 및 인력관리",
        "name": "인사평가 및 보상체계",
        "max": 70,
        "questions": [
            {
                "id": "o2_q1",
                "text": "정기적인 인사평가 제도가 있습니까?",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "비공식 평가", "score": 10},
                    {"label": "연 1회 공식 평가", "score": 25},
                    {"label": "반기 이상 + 평가 결과 피드백 면담", "score": 35},
                ]
            },
            {
                "id": "o2_q2",
                "text": "성과 기반 보상(인센티브, 성과급) 제도가 있습니까?",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "비정기적 지급", "score": 10},
                    {"label": "정기 성과급 + 지급 기준 문서화", "score": 25},
                    {"label": "성과급 + 스톡옵션·우리사주 등 장기 인센티브", "score": 35},
                ]
            },
        ],
        "evidences": [
            "인사평가 규정·매뉴얼",
            "최근 평가 결과 샘플",
            "성과급 지급 내역·기준표",
            "스톡옵션·우리사주 부여 내역 (해당 시)",
        ]
    },
    "o3": {
        "category": "organization",
        "category_name": "조직 및 인력관리",
        "name": "교육훈련 및 역량개발",
        "max": 60,
        "questions": [
            {
                "id": "o3_q1",
                "text": "연간 1인당 교육시간은? (직접계산: 총 교육시간÷직원수)",
                "type": "single",
                "options": [
                    {"label": "교육 없음", "score": 0},
                    {"label": "10시간 미만", "score": 10},
                    {"label": "10~30시간", "score": 20},
                    {"label": "30시간 이상", "score": 30},
                ]
            },
            {
                "id": "o3_q2",
                "text": "교육훈련 예산이 책정되어 있습니까?",
                "type": "single",
                "options": [
                    {"label": "예산 없음", "score": 0},
                    {"label": "비공식 집행", "score": 10},
                    {"label": "연간 예산 책정 (인건비의 1% 미만)", "score": 20},
                    {"label": "연간 예산 책정 (인건비의 1% 이상)", "score": 30},
                ]
            },
        ],
        "evidences": [
            "연간 교육훈련 계획서",
            "교육 이수 내역(수료증, 참석부)",
            "교육비 집행 내역",
        ]
    },
    "o4": {
        "category": "organization",
        "category_name": "조직 및 인력관리",
        "name": "조직문화 및 소통",
        "max": 60,
        "questions": [
            {
                "id": "o4_q1",
                "text": "정기적 전사 소통 채널이 있습니까? (조회·타운홀·뉴스레터 등)",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "분기 1회 이상", "score": 15},
                    {"label": "월 1회 이상", "score": 25},
                ]
            },
            {
                "id": "o4_q2",
                "text": "직원만족도 조사를 실시합니까?",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "비정기 실시", "score": 10},
                    {"label": "연 1회 이상 + 결과 공유", "score": 20},
                    {"label": "연 1회 이상 + 결과 기반 개선 활동", "score": 35},
                ]
            },
        ],
        "evidences": [
            "전사 소통 채널 운영 기록 (타운홀 회의록 등)",
            "직원만족도 조사 결과",
            "조직문화 개선 활동 자료",
        ]
    },

    # ─────────────── 분야 4: 사회 신뢰 활동 (ESG경영) (250점) ───────────────
    "e1": {
        "category": "esg",
        "category_name": "사회 신뢰 활동 (ESG경영)",
        "name": "환경경영 (Environment)",
        "max": 70,
        "questions": [
            {
                "id": "e1_q1",
                "text": "환경경영 방침·정책이 문서화되어 있습니까?",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "구두 공유", "score": 5},
                    {"label": "문서화 + 사내 공지", "score": 20},
                    {"label": "ISO 14001 등 인증 보유", "score": 35},
                ]
            },
            {
                "id": "e1_q2",
                "text": "에너지·자원 사용량을 측정·관리합니까?",
                "type": "single",
                "options": [
                    {"label": "측정 안 함", "score": 0},
                    {"label": "전기·가스 사용량만 모니터링", "score": 10},
                    {"label": "에너지·물·폐기물 종합 관리", "score": 20},
                    {"label": "탄소배출량 산정·감축 목표 설정", "score": 35},
                ]
            },
        ],
        "evidences": [
            "환경경영 방침서",
            "ISO 14001 인증서 (해당 시)",
            "에너지·자원 사용 모니터링 자료",
            "탄소배출량 산정 보고서 (해당 시)",
        ]
    },
    "e2": {
        "category": "esg",
        "category_name": "사회 신뢰 활동 (ESG경영)",
        "name": "사회적 책임 (Social)",
        "max": 70,
        "questions": [
            {
                "id": "e2_q1",
                "text": "사회공헌 활동 실적이 있습니까?",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "비정기 기부", "score": 10},
                    {"label": "정기 사회공헌 프로그램", "score": 25},
                    {"label": "정기 프로그램 + 임직원 참여 봉사", "score": 35},
                ]
            },
            {
                "id": "e2_q2",
                "text": "협력업체와의 상생 활동이 있습니까? (공정거래·동반성장 등)",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "단순 거래만", "score": 5},
                    {"label": "협력사 교육·기술지원", "score": 20},
                    {"label": "상생협력 협약 체결", "score": 35},
                ]
            },
        ],
        "evidences": [
            "사회공헌 활동 보고서",
            "기부금 영수증",
            "협력사 상생협약서",
            "임직원 봉사활동 사진·기록",
        ]
    },
    "e3": {
        "category": "esg",
        "category_name": "사회 신뢰 활동 (ESG경영)",
        "name": "지배구조 (Governance)",
        "max": 60,
        "questions": [
            {
                "id": "e3_q1",
                "text": "이사회 또는 경영진 회의가 정기적으로 개최됩니까?",
                "type": "single",
                "options": [
                    {"label": "비정기", "score": 0},
                    {"label": "분기 1회 이상", "score": 15},
                    {"label": "월 1회 이상", "score": 25},
                ]
            },
            {
                "id": "e3_q2",
                "text": "윤리경영 규정(행동강령)이 있습니까?",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "문서화", "score": 15},
                    {"label": "문서화 + 임직원 교육 + 위반 신고 채널", "score": 35},
                ]
            },
        ],
        "evidences": [
            "이사회·경영진 회의록",
            "윤리경영 규정·행동강령",
            "윤리교육 이수 기록",
            "내부 신고 채널 운영 자료",
        ]
    },
    "e4": {
        "category": "esg",
        "category_name": "사회 신뢰 활동 (ESG경영)",
        "name": "이해관계자 관계",
        "max": 50,
        "questions": [
            {
                "id": "e4_q1",
                "text": "고객 의견 수렴 채널이 운영됩니까?",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "전화·이메일 접수", "score": 10},
                    {"label": "고객만족도 정기 조사", "score": 20},
                    {"label": "고객만족도 + VOC 분석·개선 시스템", "score": 30},
                ]
            },
            {
                "id": "e4_q2",
                "text": "지역사회·정부와의 협력 사례가 있습니까?",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "1~2건", "score": 10},
                    {"label": "정기적 협력", "score": 20},
                ]
            },
        ],
        "evidences": [
            "고객만족도 조사 결과",
            "VOC 분석·처리 기록",
            "지역사회 협력 사업 자료",
        ]
    },
}

# =====================================================================
# 분야 2: 성과관리 — 업종별 차이 발생
# =====================================================================

PERFORMANCE_ITEMS_MFG = {
    "p1": {
        "category": "performance",
        "category_name": "성과관리",
        "name": "성과지표(KPI) 설정",
        "max": 60,
        "questions": [
            {
                "id": "p1_q1",
                "text": "전사 KPI가 설정·관리되고 있습니까?",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "매출만 관리", "score": 10},
                    {"label": "재무·생산·품질·납기 등 다차원 KPI", "score": 25},
                    {"label": "BSC 등 체계화된 KPI 시스템 운영", "score": 35},
                ]
            },
            {
                "id": "p1_q2",
                "text": "부서별·개인별 KPI가 연계되어 있습니까?",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "부서까지", "score": 10},
                    {"label": "개인 KPI까지 연계", "score": 25},
                ]
            },
        ],
        "evidences": [
            "전사·부서·개인 KPI 정의서",
            "KPI 모니터링 대시보드 화면",
        ]
    },
    "p2": {
        "category": "performance",
        "category_name": "성과관리",
        "name": "성과 측정 및 분석",
        "max": 60,
        "questions": [
            {
                "id": "p2_q1",
                "text": "성과 측정 주기는?",
                "type": "single",
                "options": [
                    {"label": "측정 안 함", "score": 0},
                    {"label": "연 1회", "score": 10},
                    {"label": "분기별", "score": 20},
                    {"label": "월별 이상", "score": 30},
                ]
            },
            {
                "id": "p2_q2",
                "text": "성과 분석 결과를 의사결정에 활용한 사례가 있습니까?",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "비정기 활용", "score": 10},
                    {"label": "정기적 분석·반영", "score": 30},
                ]
            },
        ],
        "evidences": [
            "성과 측정·분석 보고서 (월/분기)",
            "성과 기반 의사결정 사례 (회의록)",
        ]
    },
    "p3": {
        "category": "performance",
        "category_name": "성과관리",
        "name": "재무성과 — 매출액 영업이익률 (제조업)",
        "max": 70,
        "questions": [
            {
                "id": "p3_q1",
                "text": "최근 3년 매출액 평균 증가율은? (제조업 기준)",
                "type": "single",
                "options": [
                    {"label": "마이너스 또는 정체", "score": 0},
                    {"label": "0~5%", "score": 15},
                    {"label": "5~15%", "score": 30},
                    {"label": "15% 이상", "score": 40},
                ]
            },
            {
                "id": "p3_q2",
                "text": "최근 영업이익률은? (제조업 평균 5% 기준)",
                "type": "single",
                "options": [
                    {"label": "영업적자", "score": 0},
                    {"label": "0~3%", "score": 10},
                    {"label": "3~7%", "score": 20},
                    {"label": "7% 이상", "score": 30},
                ]
            },
        ],
        "evidences": [
            "최근 3년 재무제표 (국세청 신고분 필수)",
            "손익계산서·재무상태표",
            "부가가치세 신고서",
        ]
    },
    "p4": {
        "category": "performance",
        "category_name": "성과관리",
        "name": "비재무성과 — 품질·생산성 (제조업)",
        "max": 60,
        "questions": [
            {
                "id": "p4_q1",
                "text": "불량률 또는 클레임률 추이는?",
                "type": "single",
                "options": [
                    {"label": "측정 안 함", "score": 0},
                    {"label": "측정만 하고 개선 없음", "score": 5},
                    {"label": "지속 감소 추세", "score": 20},
                    {"label": "업계 평균 대비 우수", "score": 30},
                ]
            },
            {
                "id": "p4_q2",
                "text": "품질 관련 인증을 보유하고 있습니까? (중복 가능)",
                "type": "multi",
                "options": [
                    {"label": "ISO 9001", "score": 10},
                    {"label": "KS 인증", "score": 10},
                    {"label": "Single PPM 등 무결점 인증", "score": 10},
                ]
            },
        ],
        "evidences": [
            "불량률·클레임률 통계",
            "ISO 9001 인증서 (해당 시)",
            "KS·Single PPM 인증서 (해당 시)",
            "고객 클레임 처리 기록",
        ]
    },
}

PERFORMANCE_ITEMS_SVC = {
    "p1": {
        "category": "performance",
        "category_name": "성과관리",
        "name": "성과지표(KPI) 설정",
        "max": 60,
        "questions": [
            {
                "id": "p1_q1",
                "text": "전사 KPI가 설정·관리되고 있습니까?",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "매출만 관리", "score": 10},
                    {"label": "재무·고객·서비스품질 등 다차원 KPI", "score": 25},
                    {"label": "BSC 등 체계화된 KPI 시스템 운영", "score": 35},
                ]
            },
            {
                "id": "p1_q2",
                "text": "부서별·개인별 KPI가 연계되어 있습니까?",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "부서까지", "score": 10},
                    {"label": "개인 KPI까지 연계", "score": 25},
                ]
            },
        ],
        "evidences": [
            "전사·부서·개인 KPI 정의서",
            "KPI 모니터링 대시보드 화면",
        ]
    },
    "p2": {
        "category": "performance",
        "category_name": "성과관리",
        "name": "성과 측정 및 분석",
        "max": 60,
        "questions": [
            {
                "id": "p2_q1",
                "text": "성과 측정 주기는?",
                "type": "single",
                "options": [
                    {"label": "측정 안 함", "score": 0},
                    {"label": "연 1회", "score": 10},
                    {"label": "분기별", "score": 20},
                    {"label": "월별 이상", "score": 30},
                ]
            },
            {
                "id": "p2_q2",
                "text": "성과 분석 결과를 의사결정에 활용한 사례가 있습니까?",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "비정기 활용", "score": 10},
                    {"label": "정기적 분석·반영", "score": 30},
                ]
            },
        ],
        "evidences": [
            "성과 측정·분석 보고서 (월/분기)",
            "성과 기반 의사결정 사례 (회의록)",
        ]
    },
    "p3": {
        "category": "performance",
        "category_name": "성과관리",
        "name": "재무성과 — 매출액 영업이익률 (서비스업)",
        "max": 70,
        "questions": [
            {
                "id": "p3_q1",
                "text": "최근 3년 매출액 평균 증가율은? (서비스업 기준)",
                "type": "single",
                "options": [
                    {"label": "마이너스 또는 정체", "score": 0},
                    {"label": "0~10%", "score": 15},
                    {"label": "10~20%", "score": 30},
                    {"label": "20% 이상", "score": 40},
                ]
            },
            {
                "id": "p3_q2",
                "text": "최근 영업이익률은? (서비스업 평균 7% 기준)",
                "type": "single",
                "options": [
                    {"label": "영업적자", "score": 0},
                    {"label": "0~5%", "score": 10},
                    {"label": "5~10%", "score": 20},
                    {"label": "10% 이상", "score": 30},
                ]
            },
        ],
        "evidences": [
            "최근 3년 재무제표 (국세청 신고분 필수)",
            "손익계산서·재무상태표",
            "부가가치세 신고서",
        ]
    },
    "p4": {
        "category": "performance",
        "category_name": "성과관리",
        "name": "비재무성과 — 고객만족·서비스품질 (서비스업)",
        "max": 60,
        "questions": [
            {
                "id": "p4_q1",
                "text": "고객만족도(NPS, CSI 등) 점수는?",
                "type": "single",
                "options": [
                    {"label": "측정 안 함", "score": 0},
                    {"label": "측정만 하고 개선 없음", "score": 5},
                    {"label": "지속 향상 추세", "score": 20},
                    {"label": "업계 평균 대비 우수", "score": 30},
                ]
            },
            {
                "id": "p4_q2",
                "text": "서비스 품질 인증·평가 보유 여부 (중복 가능)",
                "type": "multi",
                "options": [
                    {"label": "ISO 9001", "score": 10},
                    {"label": "서비스품질 우수기업 지정", "score": 10},
                    {"label": "고객만족경영 인증", "score": 10},
                ]
            },
        ],
        "evidences": [
            "고객만족도(NPS/CSI) 조사 결과",
            "ISO 9001 인증서 (해당 시)",
            "서비스품질 인증서 (해당 시)",
            "VOC 처리 기록",
        ]
    },
}

PERFORMANCE_ITEMS_CON = {
    "p1": {
        "category": "performance",
        "category_name": "성과관리",
        "name": "성과지표(KPI) 설정",
        "max": 60,
        "questions": [
            {
                "id": "p1_q1",
                "text": "전사 KPI가 설정·관리되고 있습니까?",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "매출·수주만 관리", "score": 10},
                    {"label": "수주·공기·안전·품질 등 다차원 KPI", "score": 25},
                    {"label": "현장별 KPI까지 체계화", "score": 35},
                ]
            },
            {
                "id": "p1_q2",
                "text": "현장별·공정별 KPI가 연계되어 있습니까?",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "본사 KPI만", "score": 10},
                    {"label": "현장 KPI까지 연계", "score": 25},
                ]
            },
        ],
        "evidences": [
            "전사·현장 KPI 정의서",
            "현장별 KPI 모니터링 자료",
        ]
    },
    "p2": {
        "category": "performance",
        "category_name": "성과관리",
        "name": "성과 측정 및 분석",
        "max": 60,
        "questions": [
            {
                "id": "p2_q1",
                "text": "현장별 성과 측정 주기는?",
                "type": "single",
                "options": [
                    {"label": "측정 안 함", "score": 0},
                    {"label": "공사 완료 후만", "score": 10},
                    {"label": "공정별 단계 점검", "score": 20},
                    {"label": "월별 정기 측정", "score": 30},
                ]
            },
            {
                "id": "p2_q2",
                "text": "성과 분석 결과를 의사결정에 활용한 사례가 있습니까?",
                "type": "single",
                "options": [
                    {"label": "없음", "score": 0},
                    {"label": "비정기 활용", "score": 10},
                    {"label": "정기적 분석·반영", "score": 30},
                ]
            },
        ],
        "evidences": [
            "현장별 성과 측정·분석 보고서",
            "성과 기반 의사결정 사례 (회의록)",
        ]
    },
    "p3": {
        "category": "performance",
        "category_name": "성과관리",
        "name": "재무성과 — 매출액 영업이익률 (건설업)",
        "max": 70,
        "questions": [
            {
                "id": "p3_q1",
                "text": "최근 3년 매출액 평균 증가율은? (건설업 기준)",
                "type": "single",
                "options": [
                    {"label": "마이너스 또는 정체", "score": 0},
                    {"label": "0~5%", "score": 15},
                    {"label": "5~10%", "score": 30},
                    {"label": "10% 이상", "score": 40},
                ]
            },
            {
                "id": "p3_q2",
                "text": "최근 영업이익률은? (건설업 평균 4% 기준)",
                "type": "single",
                "options": [
                    {"label": "영업적자", "score": 0},
                    {"label": "0~2%", "score": 10},
                    {"label": "2~5%", "score": 20},
                    {"label": "5% 이상", "score": 30},
                ]
            },
        ],
        "evidences": [
            "최근 3년 재무제표 (국세청 신고분 필수)",
            "손익계산서·재무상태표",
            "시공능력평가서",
        ]
    },
    "p4": {
        "category": "performance",
        "category_name": "성과관리",
        "name": "비재무성과 — 안전·품질·공기 (건설업)",
        "max": 60,
        "questions": [
            {
                "id": "p4_q1",
                "text": "최근 3년 산업재해 발생 현황은?",
                "type": "single",
                "options": [
                    {"label": "중대재해 발생", "score": 0},
                    {"label": "경미사고 다수", "score": 5},
                    {"label": "재해율 업계 평균 이하", "score": 20},
                    {"label": "무재해 사업장", "score": 30},
                ]
            },
            {
                "id": "p4_q2",
                "text": "건설업 관련 인증·평가 보유 (중복 가능)",
                "type": "multi",
                "options": [
                    {"label": "ISO 9001", "score": 10},
                    {"label": "ISO 45001 (안전보건)", "score": 10},
                    {"label": "시공능력평가 상위 등급", "score": 10},
                ]
            },
        ],
        "evidences": [
            "산업재해 통계 (고용노동부 신고)",
            "ISO 9001/45001 인증서 (해당 시)",
            "시공능력평가서",
            "공기 준수율 자료",
        ]
    },
}

# =====================================================================
# 통합 평가지표 (업종별로 조합)
# =====================================================================

def get_mainbiz_criteria(industry: str) -> dict:
    """업종별 메인비즈 평가지표 반환

    industry: 'manufacturing' (제조업) | 'service' (서비스업) | 'construction' (건설업)
    """
    industry_perf = {
        "manufacturing": PERFORMANCE_ITEMS_MFG,
        "service": PERFORMANCE_ITEMS_SVC,
        "construction": PERFORMANCE_ITEMS_CON,
    }.get(industry, PERFORMANCE_ITEMS_MFG)

    # 16개 항목 통합
    items = {}
    items.update({k: v for k, v in COMMON_ITEMS.items() if v["category"] == "strategy"})  # s1~s4
    items.update(industry_perf)  # p1~p4
    items.update({k: v for k, v in COMMON_ITEMS.items() if v["category"] == "organization"})  # o1~o4
    items.update({k: v for k, v in COMMON_ITEMS.items() if v["category"] == "esg"})  # e1~e4

    return {
        "version": "2026.01",
        "industry": industry,
        "industry_name": {
            "manufacturing": "제조업",
            "service": "서비스업",
            "construction": "건설업"
        }[industry],
        "total_score": 1000,
        "self_pass": 600,
        "field_pass": 700,
        "items": items,
        "categories": [
            {"id": "strategy", "name": "전략기획 및 이행관리", "items": ["s1", "s2", "s3", "s4"]},
            {"id": "performance", "name": "성과관리", "items": ["p1", "p2", "p3", "p4"]},
            {"id": "organization", "name": "조직 및 인력관리", "items": ["o1", "o2", "o3", "o4"]},
            {"id": "esg", "name": "사회 신뢰 활동 (ESG경영)", "items": ["e1", "e2", "e3", "e4"]},
        ]
    }


def calculate_item_score(item: dict, answers: dict) -> int:
    """문항별 답변을 기반으로 점수 계산"""
    total = 0
    for question in item["questions"]:
        q_id = question["id"]
        if q_id not in answers:
            continue

        if question["type"] == "single":
            # 단일 선택: 선택된 옵션의 점수
            selected_idx = answers[q_id]
            if isinstance(selected_idx, int) and 0 <= selected_idx < len(question["options"]):
                total += question["options"][selected_idx]["score"]
        elif question["type"] == "multi":
            # 다중 선택: 선택된 옵션들의 점수 합산
            selected_indices = answers[q_id]
            if isinstance(selected_indices, list):
                for idx in selected_indices:
                    if 0 <= idx < len(question["options"]):
                        total += question["options"][idx]["score"]

    return min(total, item["max"])  # 항목 최대 점수 초과 방지
