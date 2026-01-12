# 🧠 LangGraph Streamlit Chatbot

A multi-conversation chatbot built with **Streamlit**, **LangGraph**, and **LangChain**, featuring persistent memory, smart conversation titles, and real-time streaming responses — similar to ChatGPT.

---

## 📦 Imports Overview

```python
import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage
import uuid
```

### Import Breakdown

- **streamlit (`st`)** – Builds the web UI  
- **langgraph_backend** – Custom backend with LangGraph + LLM  
- **HumanMessage** – LangChain message wrapper  
- **uuid** – Generates unique conversation IDs  

---

## 🔧 Helper Functions

### `generate_thread_id()`
Creates a unique ID for each conversation using UUID.

### `reset_chat()`
Starts a fresh conversation:
- Generates new thread ID  
- Clears chat history  
- Triggered by **New Chat** button  

### `add_thread(thread_id, title=None)`
Registers a conversation thread:
- Prevents duplicates  
- Stores thread ID  
- Sets default title if none provided  

### `update_thread_title(thread_id, first_message)`
Auto-generates a smart title:
- Runs only on first message  
- Uses AI to create short descriptive title  

### `load_conversation(thread_id)`
Loads chat history from LangGraph memory.

### `generate_conversation_title(first_message)`
Creates a concise AI-generated title:
- Max 5 words  
- Max 50 characters  
- Fallback-safe  

---

## 💾 Session State

Streamlit session state stores data across reruns.

### Stored Variables

- **chat_history** – Messages of active conversation  
- **thread_id** – Current conversation ID  
- **chat_threads** – List of all conversations  
- **thread_titles** – Mapping of thread IDs → titles  

---

## 🎨 Sidebar UI

- App title  
- **New Chat** button  
- List of conversations (newest first)  
- Clickable buttons with unique keys  

---

## 💬 Chat Interface

Messages are rendered using:

```python
st.chat_message(role)
```

- User and AI messages auto-styled  
- Clean ChatGPT-like UI  

---

## ⌨️ User Input Flow

1. User types message  
2. Message displayed immediately  
3. Title generated (first message only)  
4. Message sent to LangGraph  
5. AI response streams in real time  
6. Conversation saved to memory  

---

## 🔄 App Flow Summary

- App loads → first thread created  
- Messages persist per thread  
- Multiple conversations supported  
- Seamless switching between chats  

---

## 🎯 Key Features

✅ Persistent memory per conversation  
✅ Multiple chat threads  
✅ Smart AI-generated titles  
✅ Real-time streaming responses  
✅ Clean ChatGPT-style UI  

---

## 🛠 Tech Stack

- Streamlit  
- LangGraph  
- LangChain  
- Python  


## ▶️ How to Run the Project

Follow the steps below to run the LangGraph Streamlit Chatbot locally.

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/TahaDataAlchemy/LangGraph-Fundamentals.git
cd LanggraphChatbot
OPENAI_API_KEY=your_openai_api_key_here
streamlit run streamlit_frontend.py

---

## UI

<img width="1912" height="915" alt="image" src="https://github.com/user-attachments/assets/4363944f-31bb-4a85-8edb-4f0af551a418" />

