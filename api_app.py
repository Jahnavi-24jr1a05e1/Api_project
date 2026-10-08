import streamlit as st
import google.generativeai as genai

st.set_page_config(
    page_title="Google AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

GOOGLE_API_KEY = "AQ.Ab8RN6Ic1q1Pa4a203qpa1WWou3OjnH7BRJogStaYa9paxTmOQ"

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-3.8-flash")

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🤖 Google AI Chatbot")
st.write("Ask me anything!")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    try:
        response = st.session_state.chat.send_message(user_input)

        with st.chat_message("assistant"):
            st.markdown(response.text)

        st.session_state.messages.append({
            "role": "assistant",
            "content": response.text
        })

    except Exception as e:
        st.error(f"Error: {e}")