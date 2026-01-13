from app.data.chat_state import ChatState
from app.usecase.llm_client import llm
from typing import Dict

def chat_node(state:ChatState) -> Dict[list]:
    messages = state["messages"]
    response = llm.invoke(messages)
    return {"messages":[response]}

