from app.data.chat_state import ChatState
from app.usecase.chat_node import chat_node
from langgraph.graph import START,END,StateGraph
from langgraph.checkpoint.sqlite import SqliteSaver
from app.infra.config import settings
from app.infra.db_conn import conn

checkpointer = SqliteSaver(conn=conn)
graph = StateGraph(ChatState)
graph.add_node("chat_node",chat_node)
graph.add_edge(START,"chat_node")
graph.add_edge("chat_node",END)

chatbot = graph.compile(checkpointer=checkpointer)