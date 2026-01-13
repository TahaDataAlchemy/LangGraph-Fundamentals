from app.data.chat_state import ChatState
from app.usecase.llm_client import llm
from typing import Dict,List,Any

def chat_node(state:ChatState) -> Dict[str,List[Any]]:
    messages = state["messages"]
    response = llm.invoke(messages)
    return {"messages":[response]}

