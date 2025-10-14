import streamlit as st
import requests
from streamlit_chat import message
import json
import os

OLLAMA_API_URL = "http://localhost:11434/api/chat"
HISTORY_FILE = "chat_history.json"  

if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        saved_history = json.load(f)
else:
    saved_history = []

if 'user_input' not in st.session_state:
    st.session_state['user_input'] = [item['user'] for item in saved_history]

if 'ollama_response' not in st.session_state:
    st.session_state['ollama_response'] = [item['bot'] for item in saved_history]

def ollama_chat(messages):
    payload = {
        "model": "llama2:latest",
        "messages": messages,
        "stream": False
    }
    response = requests.post(OLLAMA_API_URL, json=payload)
    if response.status_code == 200:
        return response.json()['message']['content']
    else:
        return f"Error: {response.text}"

st.title("💻 ByteBuddy: AI for Coders")

st.sidebar.title("Conversation History")


if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state['user_input'] = []
    st.session_state['ollama_response'] = []

if st.sidebar.button("🧹 Clear History"):
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)
    st.session_state['user_input'] = []
    st.session_state['ollama_response'] = []

for i, (u, b) in enumerate(zip(st.session_state['user_input'], st.session_state['ollama_response'])):
    one_liner = u if len(u) <= 40 else u[:37] + "..."
    with st.sidebar.expander(f"{i+1}. {one_liner}", expanded=False):
        st.markdown(f"**You:** {u}")
        st.markdown(f"**Bot:** {b}")

user_input = st.text_input("Write your message here:", key="input")

if user_input:
    conversation = [{"role": "system", "content": "You are a helpful assistant."}]
    for u, b in zip(st.session_state['user_input'], st.session_state['ollama_response']):
        conversation.append({"role": "user", "content": u})
        conversation.append({"role": "assistant", "content": b})
    conversation.append({"role": "user", "content": user_input})

    bot_response = ollama_chat(conversation).lstrip("\n")

    st.session_state['user_input'].append(user_input)
    st.session_state['ollama_response'].append(bot_response)

    chat_data = [{"user": u, "bot": b} for u, b in zip(st.session_state['user_input'], st.session_state['ollama_response'])]
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(chat_data, f, ensure_ascii=False, indent=4)

if st.session_state['user_input']:
    for i in range(len(st.session_state['user_input'])):
        message(st.session_state["user_input"][i],
                key=str(i) + "_user", avatar_style="icons", is_user=True)
        message(st.session_state["ollama_response"][i],
                key=str(i) + "_bot", avatar_style="miniavs")
