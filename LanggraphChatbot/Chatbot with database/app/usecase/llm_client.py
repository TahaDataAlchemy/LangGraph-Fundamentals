from langchain_openai import ChatOpenAI
from app.data.chat_state import ChatState
from app.infra.config import settings

llm = ChatOpenAI(
    model='openai/gpt-oss-120b',
    temperature=0,
    max_tokens = 8192,
    api_key=settings.GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)