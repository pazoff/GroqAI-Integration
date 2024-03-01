from typing import List, Optional, Type
from cat.mad_hatter.decorators import tool, hook, plugin
from pydantic import BaseModel, ConfigDict, SecretStr
from datetime import datetime, date
from cat.factory.llm import LLMSettings
from langchain_groq.chat_models import ChatGroq

class GroqAIConfig(LLMSettings):
    """The configuration for the GroqAI plugin."""

    groq_api_key: Optional[SecretStr]
    model: str = "mixtral-8x7b-32768"
    max_tokens: Optional[int] = 32768
    top_p: float = 1
    temperature: float = 0.7
    streaming: bool = False
    
    _pyclass: Type = ChatGroq

    model_config = ConfigDict(
        json_schema_extra={
            "humanReadableName": "GroqAI",
            "description": "Configuration for GroqAI",
            "link": "https://groq.com",
        }
    )
    

@hook
def factory_allowed_llms(allowed, cat) -> List:
    allowed.append(GroqAIConfig)
    return allowed
