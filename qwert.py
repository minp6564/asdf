import streamlit as st
from openai import OpenAI

# 제목
st.title("🧠 GPT-4.1-mini 채팅")

# API Key 입력 받기
api_key = st.text_input("🔐 OpenAI API Key", type="password")

# 세션 상태에 대화 메시지 리스트 초기화
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

# 사용자 입력 받기
user_input = st.text_input("✍️ 질문을 입력하세요", key="input")

# GPT 응답 처리
if st.button("보내기"):
    if not api_key:
        st.warning("API 키를 입력해주세요.")
    elif not user_input:
        st.warning("질문을 입력해주세요.")
    else:
        try:
            # OpenAI 클라이언트 설정
            client = OpenAI(api_key=api_key)

            # 사용자 메시지 추가
            st.session_state.messages.append({"role": "user", "content": user_input})

            # Responses API 호출
            response = client.responses.create(
                model="gpt-4.1-mini",
                input=st.session_state.messages
            )

            assistant_reply = response.output[0].content[0].text
            st.session_state.messages.append({"role": "assistant", "content": assistant_reply})

        except Exception as e:
            st.error(f"에러 발생: {e}")

# 대화 이력 출력
st.subheader("💬 대화")
for msg in st.session_state.messages[1:]:
    speaker = "👤 사용자" if msg["role"] == "user" else "🤖 GPT"
    st.markdown(f"**{speaker}:** {msg['content']}")
