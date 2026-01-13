from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    GROQ_API_KEY: str = Field(default="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")
    DATABASE:str = Field(default="lang_chabot_db")

    class Config:
        env_file = "./.env" 
        extra = "ignore"

settings = Settings()
