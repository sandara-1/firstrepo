import streamlit as st

# MBTI 유형과 설명을 사전으로 정의
mbti_types = {
    "ISTJ": "성실하고, 실용적이며, 책임감이 강한 사람.",
    "ISFJ": "세심하고, 배려가 깊으며, 헌신적인 사람.",
    "INFJ": "통찰력이 있으며, 깊은 감정을 가진 사람.",
    "INTJ": "창의적이고, 문제 해결에 능숙한 전략가.",
    "ISTP": "실용적이고, 문제 해결을 즐기는 사람.",
    "ISFP": "감각적이고, 예술적인 재능이 많은 사람.",
    "INFP": "이상주의적이며, 깊은 감정을 가진 사람.",
    "INTP": "논리적이고, 독창적인 사고를 가진 사람.",
    "ESTP": "활동적이고, 모험을 즐기는 사람.",
    "ESFP": "사교적이며, 사람들과 함께하는 것을 좋아하는 사람.",
    "ENFP": "열정적이고, 창의성이 뛰어난 사람.",
    "ENTP": "호기심이 많고, 새로운 아이디어를 추구하는 사람.",
    "ESTJ": "조직적이고, 목표 지향적인 사람.",
    "ESFJ": "사람들과의 관계를 중시하는 헌신적인 사람.",
    "ENFJ": "사람들에게 영감을 주며, 지도력을 발휘하는 사람.",
    "ENTJ": "결단력 있고, 목표를 향해 나아가는 리더."
}

# Streamlit 앱 시작
st.title("MBTI 유형 선택기")

# MBTI 유형 선택
selected_mbti = st.selectbox("당신의 MBTI 유형을 선택하세요:", list(mbti_types.keys()))

# 선택된 유형에 대한 설명 표시
st.write(f"선택한 MBTI 유형: **{selected_mbti}**")
st.write(mbti_types[selected_mbti])

