import streamlit as st
from openai import OpenAI

# 1. 제목 출력
st.title("GPT-4.1-mini 응답 웹앱")

# 2. API 키 입력 받기 (비밀번호 타입으로 숨김)
api_key = st.text_input("🔑 OpenAI API Key를 입력하세요", type="password")

# 3. 질문 입력 받기
user_prompt = st.text_input("💬 질문을 입력하세요")

# 4. 응답 버튼
if st.button("응답 요청"):

    # 5. 입력값 유효성 검사
    if not api_key:
        st.error("API Key를 입력하세요.")
    elif not user_prompt:
        st.error("질문을 입력하세요.")
    else:
        try:
            # 6. OpenAI API 클라이언트 생성
            client = OpenAI(api_key=api_key)

            # 7. Responses API 호출
            response = client.responses.create(
                model="gpt-4.1-mini",
                input=[{"role": "user", "content": user_prompt}]
            )

            # 8. 응답 텍스트 추출 및 출력
            output = response.output[0].content[0].text
            st.success("🧠 GPT 응답:")
            st.write(output)

        except Exception as e:
            st.error(f"에러 발생: {e}")
