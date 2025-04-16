import streamlit as st

# MBTI 유형과 설명 및 관련 정보
mbti_data = {
    "ISTJ": {
        "description": "성실하고, 실용적이며, 책임감이 강한 사람입니다. 질서와 규칙을 중시하며, 세부적인 사항에 주의 깊습니다. 비판적 사고와 신뢰성을 바탕으로 일을 처리합니다.",
        "jobs": ["회계사", "변호사", "교사"],
        "compatibility": "ESTP, ISFP",
        "emoji": "📚"
    },
    "ISFJ": {
        "description": "세심하고, 배려가 깊으며, 헌신적인 사람입니다. 다른 사람들을 도와주고 그들의 필요를 돌보는 것을 좋아합니다. 조용하고 차분한 성격을 가지고 있습니다.",
        "jobs": ["간호사", "사회복지사", "교사"],
        "compatibility": "ESTP, ENFP",
        "emoji": "💖"
    },
    "INFJ": {
        "description": "통찰력이 있으며, 깊은 감정을 가진 사람입니다. 이상주의적이고, 다른 사람들의 감정을 이해하려고 노력합니다. 항상 의미 있는 관계를 추구합니다.",
        "jobs": ["작가", "상담사", "예술가"],
        "compatibility": "ENFP, INFP",
        "emoji": "🌈"
    },
    "INTJ": {
        "description": "창의적이고, 문제 해결에 능숙한 전략가입니다. 독창적이고 분석적이며, 목표를 달성하기 위한 장기적인 계획을 세우는 것을 좋아합니다.",
        "jobs": ["과학자", "플래너", "IT 전문가"],
        "compatibility": "ENTP, ENFJ",
        "emoji": "🧠"
    },
    "ISTP": {
        "description": "실용적이고, 문제 해결을 즐기는 사람입니다. 기술적이고 논리적이며, 손재주가 뛰어나고 즉각적인 대처 능력이 뛰어납니다.",
        "jobs": ["기술자", "조종사", "경비원"],
        "compatibility": "ESTJ, ISFJ",
        "emoji": "⚙️"
    },
    "ISFP": {
        "description": "감각적이고, 예술적인 재능이 많은 사람입니다. 자연과 사람들에 대한 애정이 깊고, 자신의 감정을 표현하는 것을 선호합니다.",
        "jobs": ["예술가", "디자이너", "작가"],
        "compatibility": "ENFJ, ESTP",
        "emoji": "🎨"
    },
    "INFP": {
        "description": "이상주의적이며, 깊은 감정을 가진 사람입니다. 자신의 가치를 중요시하며, 공감 능력이 뛰어나고 자신의 내면을 탐구하는 것을 좋아합니다.",
        "jobs": ["작가", "상담사", "사회운동가"],
        "compatibility": "ENFJ, INFJ",
        "emoji": "🌸"
    },
    "INTP": {
        "description": "논리적이고, 독창적인 사고를 가진 사람입니다. 새로운 아이디어와 개념을 탐구하는 것을 좋아하며, 논쟁이나 사고 실험에 흥미를 가집니다.",
        "jobs": ["과학자", "철학자", "프로그래머"],
        "compatibility": "ENTJ, INFJ",
        "emoji": "🤔"
    },
    "ESTP": {
        "description": "활동적이고, 모험을 즐기는 사람입니다. 즉각적인 행동을 취하고, 위기 상황에서 침착하게 대처할 수 있는 능력을 지니고 있습니다.",
        "jobs": ["영업직", "운전사", "스포츠 코치"],
        "compatibility": "ISTJ, ISFJ",
        "emoji": "🚀"
    },
    "ESFP": {
        "description": "사교적이며, 사람들과 함께하는 것을 좋아하는 사람입니다. 즐거운 경험을 선호하고, 다른 사람들에게 긍정적인 에너지를 전파합니다.",
        "jobs": ["연예인", "이벤트 플래너", "여행 가이드"],
        "compatibility": "ISTJ, ISFJ",
        "emoji": "🎉"
    },
    "ENFP": {
        "description": "열정적이고, 창의성이 뛰어난 사람입니다. 사람들과의 관계를 중시하고, 다양한 가능성을 탐구하는 것을 즐깁니다.",
        "jobs": ["마케팅 전문가", "작가", "상담사"],
        "compatibility": "INFJ, INFP",
        "emoji": "🌟"
    },
    "ENTP": {
        "description": "호기심이 많고, 새로운 아이디어를 추구하는 사람입니다. 논쟁을 통해 자신의 사고를 발전시키고, 변화를 즐깁니다.",
        "jobs": ["기업가", "상담가", "변호사"],
        "compatibility": "INTJ, INFP",
        "emoji": "💡"
    },
    "ESTJ": {
        "description": "조직적이고, 목표 지향적인 사람입니다. 실질적이고 합리적으로 문제를 해결하며, 전통적인 가치관을 존중합니다.",
        "jobs": ["관리자", "경영 컨설턴트", "교사"],
        "compatibility": "ISTP, ESFP",
        "emoji": "📊"
    },
    "ESFJ": {
        "description": "사람들과의 관계를 중시하는 헌신적인 사람입니다. 타인의 감정을 이해하고, 그들을 돕는 것을 즐깁니다.",
        "jobs": ["간호사", "교사", "인사관리자"],
        "compatibility": "ISTP, INTJ",
        "emoji": "🤗"
    },
    "ENFJ": {
        "description": "사람들에게 영감을 주며, 지도력을 발휘하는 사람입니다. 타인의 성장을 도와주고, 공동체를 위해 헌신하려고 합니다.",
        "jobs": ["상담사", "교사", "리더"],
        "compatibility": "INFP, ENFP",
        "emoji": "👑"
    },
    "ENTJ": {
        "description": "결단력 있고, 목표를 향해 나아가는 리더입니다. 전략적 사고와 효율성을 중시하며, 팀을 이끄는 데 능숙합니다.",
        "jobs": ["CEO", "경영자", "전략 기획자"],
        "compatibility": "INTP, INFJ",
        "emoji": "🚀"
    },
}

# Streamlit 앱 시작
st.title("MBTI 유형 선택기")

# MBTI 유형 선택
selected_mbti = st.selectbox("당신의 MBTI 유형을 선택하세요:", list(mbti_data.keys()))

# 선택된 유형에 대한 상세 정보 표시
mbti_info = mbti_data[selected_mbti]

st.markdown(f"### 선택한 MBTI 유형: **{selected_mbti}** {mbti_info['emoji']}")
st.write(mbti_info['description'])

st.markdown("#### 추천 직업:")
for job in mbti_info['jobs']:
    st.write(f"- {job}")

st.markdown(f"#### 어울리는 짝꿍 MBTI: {mbti_info['compatibility']}")

