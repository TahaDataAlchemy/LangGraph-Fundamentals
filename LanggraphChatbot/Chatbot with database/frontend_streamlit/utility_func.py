from langchain_core.messages import HumanMessage
from app.usecase.chatbot_invoke import chatbot
import uuid
import streamlit as st
from app.usecase.llm_client import llm

def generate_thread_id():
    thread_id = uuid.uuid4()
    return thread_id

def reset_chat():
    thread_id = generate_thread_id()
    st.session_state["thread_id"] = thread_id
    add_thread(st.session_state['thread_id'])
    st.session_state['chat_history'] = []

def add_thread(thread_id,title = None):
    if thread_id not in st.session_state["chat_threads"]:
        st.session_state['chat_threads'].append(thread_id)
        if title:
            st.session_state["thread_titles"][thread_id] = title
        else:
            st.session_state["thread_titles"][thread_id] = "New Conversation"

def update_thread_title(thread_id,first_message):
    if st.session_state['thread_titles'][thread_id] == "New Conversation":
        title = generate_conversation_title(first_message)
        st.session_state["thread_titles"][thread_id] = title

def load_conversation(thread_id):
    state = chatbot.get_state(config={"configurable":{"thread_id":thread_id}})
    return state.values.get("messages", [])

def generate_conversation_title(first_message:str) -> str:
    try:
        title_prompt = f"""Generate a short, concise title (maximum 5 words) for a conversation that starts with: "{first_message[:100]}"
            Only respond with the title, nothing else."""
        response = llm.invoke({"message":[HumanMessage(content=title_prompt)]})
        title = response["message"][-1].content.strip().replace('"','').replace("'","")
        return title[:50]
    except:
        return first_message[:30] + "..."