import streamlit as st


if 'chat_history' not in st.session_state:
    st.session_state["chat_history"] = []


chat_history = []
for message in st.session_state["chat_history"]:
    print(message)
    with st.chat_message(message["role"]):
        st.text(message["content"])

user_input = st.chat_input('Type here')

if user_input:
    with st.chat_message('user'):
        st.session_state["chat_history"].append({"role":"user","content":user_input})
        st.text(user_input)
    
    with st.chat_message('assistant'):
        st.session_state["chat_history"].append({"role":"assitant","content":user_input})
        st.text(user_input)
