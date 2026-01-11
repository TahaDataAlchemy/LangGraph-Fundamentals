import streamlit as st
from langgraph_backend import chatbot,llm
from langchain_core.messages import HumanMessage
import uuid


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


if 'chat_history' not in st.session_state:
    st.session_state["chat_history"] = []


if "thread_id" not in st.session_state:
    st.session_state["thread_id"] = generate_thread_id()

if "chat_threads" not in st.session_state:
    st.session_state["chat_threads"] = []

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
