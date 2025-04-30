import streamlit as st
from openai import OpenAI

# 페이지 설정
st.set_page_config(page_title="ChatGPT Mini", page_icon="💬", layout="wide")

st.markdown("""
    <style>
    .message {
        padding: 0.75rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        max-width: 80%;
    }
    .user {
        background-color: #DCF8C6;
        text-align: right;
        margin-left: auto;
    }
    .assistant {
        background-color: #F1F0F0;
        text-align: left;
        margin-right: auto;
    }
    </style>
""", unsafe_allow_html=True)

# 타이틀
st.title("💬 GPT-4.1-mini Chat")

# API Key
api_key = st.sidebar.text_input("🔑 OpenAI API Key", type="password")

# 채팅 기록 초기화
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

# 채팅 입력창 (하단 고정 스타일)
with st.container():
    user_input = st.chat_input("메시지를 입력하세요...")

# 메시지 전송 시
if user_input and api_key:
    # 메시지 추가
    st.session_state.messages.append({"role": "user", "content": user_input})

    # OpenAI 호출
    try:
        client = OpenAI(api_key=api_key)
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=st.session_state.messages
        )
        reply = response.output[0].content[0].text
        st.session_state.messages.append({"role": "assistant", "content": reply})

    except Exception as e:
        st.error(f"에러 발생: {e}")

# 대화 렌더링
for msg in st.session_state.messages[1:]:
    role_class = "user" if msg["role"] == "user" else "assistant"
    role_name = "You" if msg["role"] == "user" else "GPT"
    st.markdown(
        f'<div class="message {role_class}"><b>{role_name}</b><br>{msg["content"]}</div>',
        unsafe_allow_html=True
    )
