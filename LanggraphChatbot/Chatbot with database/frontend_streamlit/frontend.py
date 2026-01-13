import sys
from pathlib import Path

# Get the absolute path to project root
current_file = Path(__file__).resolve()
project_root = current_file.parent.parent

print(f"Current file: {current_file}")
print(f"Project root: {project_root}")
print(f"App folder exists: {(project_root / 'app').exists()}")
print(f"Python path: {sys.path[:3]}")

# Add project root to Python path if not already there
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

print(f"Updated Python path: {sys.path[:3]}")

import streamlit as st
from app.usecase.chatbot_invoke import chatbot
from app.usecase.thread_retriever import retrieve_all_threads
from langchain_core.messages import HumanMessage
from frontend_streamlit.utility_func import (
    generate_thread_id,reset_chat,add_thread,update_thread_title,load_conversation,generate_conversation_title
)

if 'chat_history' not in st.session_state:
    st.session_state["chat_history"] = []


if "thread_id" not in st.session_state:
    st.session_state["thread_id"] = generate_thread_id()

if "chat_threads" not in st.session_state:
    st.session_state["chat_threads"] = retrieve_all_threads()

if "thread_titles" not in st.session_state:
    st.session_state["thread_titles"] = {}


add_thread(st.session_state["thread_id"])


st.sidebar.title("LangGraph Chatbot")

if st.sidebar.button("New Chat"):
    reset_chat()

st.sidebar.header("My conversations")

for thread_id in st.session_state["chat_threads"][::-1]:
    title = st.session_state["thread_titles"].get(thread_id,"Untitled")
    if st.sidebar.button(title,key=f"btn_{thread_id}"):
        st.session_state["thread_id"] = thread_id
        messages =load_conversation(thread_id)

        temp_messages = []
        for msg in messages:
            if isinstance(msg,HumanMessage):
                role='user'
            else:
                role='assistant'
            temp_messages.append({"role":role,"content":msg.content})
        st.session_state["chat_history"] = temp_messages
       
       

for message in st.session_state["chat_history"]:
    with st.chat_message(message["role"]):
        st.text(message["content"])

user_input = st.chat_input('Type here')

if user_input:
    with st.chat_message('user'):
        st.session_state["chat_history"].append({"role":"user","content":user_input})
        st.text(user_input)

    if len(st.session_state["chat_history"]) == 1:
        update_thread_title(st.session_state["thread_id"],user_input)
    CONFIG = {'configurable': {'thread_id': st.session_state["thread_id"]}}

    with st.chat_message("assistant"):
        ai_message = st.write_stream(
            message_chunk.content for message_chunk,metadata in chatbot.stream(
                {"messages":[HumanMessage(content=user_input)]},
                config=CONFIG,
                stream_mode="messages"
            )
        )
        st.session_state["chat_history"].append({"role":"assistant","content":ai_message})
