import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="GPT Chat UI", page_icon="💬", layout="wide")

# API Key
api_key = st.sidebar.text_input("🔑 OpenAI API Key", type="password")

# 채팅 기록 초기화
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

# 📌 메시지 출력 (위쪽 영역)
st.title("💬 GPT-4.1-mini Chat")
for msg in st.session_state.messages[1:]:
    with st.chat_message("user" if msg["role"] == "user" else "assistant"):
        st.markdown(msg["content"])

# 📌 하단 입력창 (항상 화면 하단에 위치)
if prompt := st.chat_input("메시지를 입력하세요..."):
    # 사용자 입력 추가
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    if api_key:
        try:
            client = OpenAI(api_key=api_key)
            response = client.responses.create(
                model="gpt-4.1-mini",
                input=st.session_state.messages
            )
            reply = response.output[0].content[0].text
            st.session_state.messages.append({"role": "assistant", "content": reply})
            with st.chat_message("assistant"):
                st.markdown(reply)
        except Exception as e:
            st.error(f"에러 발생: {e}")
    else:
        st.warning("🔐 OpenAI API Key를 먼저 입력하세요.")
