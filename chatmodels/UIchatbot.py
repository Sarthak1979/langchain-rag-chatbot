import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

# Modes (UNCHANGED)
MODES = {
    "fast": {
        "system": "You are a fast AI assistant. Give short, direct answers.",
        "temperature": 0.3
    },
    "thinking": {
        "system": "You are a thoughtful AI. Explain step by step with reasoning.",
        "temperature": 0.7
    },
    "research": {
        "system": "You are a research AI. Provide detailed, structured, and in-depth answers.",
        "temperature": 0.9
    }
}

# UI Title
st.title("🤖 SUVIDHA AI ")

# Mode selection (replaces input())
mode = st.radio("Select Mode:", ["fast", "thinking", "research"])

config = MODES[mode]

# ✅ New Chat Button
if st.button("🆕 New Chat"):
    st.session_state.messages = [
        SystemMessage(content=config["system"])
    ]
    st.rerun()

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content=config["system"])
    ]

else:
    if isinstance(st.session_state.messages[0], SystemMessage):
        st.session_state.messages[0] = SystemMessage(content=config["system"])

# IMPORTANT: If mode changes → reset system message
if st.session_state.messages[0].content != config["system"]:
    st.session_state.messages = [
        SystemMessage(content=config["system"])
    ]

# Initialize model (same logic)
model = ChatMistralAI(
    model="mistral-small-latest",
    temperature=config["temperature"]
)

# Display chat history (skip system message)
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").write(msg.content)
    elif isinstance(msg, AIMessage):
        st.chat_message("assistant").write(msg.content)

# Input box (replaces input())
user_input = st.chat_input("Type your message...")

if user_input:
    # Exit condition
    if user_input == "0":
        st.stop()

    # Add user message
    st.session_state.messages.append(HumanMessage(content=user_input))
    st.chat_message("user").write(user_input)

    # Get response
    response = model.invoke(st.session_state.messages)

    # Add AI response
    st.session_state.messages.append(AIMessage(content=response.content))
    st.chat_message("assistant").write(response.content)