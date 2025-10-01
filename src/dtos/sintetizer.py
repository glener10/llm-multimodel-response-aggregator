from pydantic import BaseModel
from enum import Enum


class ProviderEnum(str, Enum):
    OPENAI = "OPENAI"
    GEMINI = "GEMINI"


class Sintetizer(BaseModel):
    provider: ProviderEnum
    model: str
