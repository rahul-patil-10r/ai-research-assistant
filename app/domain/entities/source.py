from pydantic import BaseModel
from enum import Enum


class SourceType(str, Enum):
    WEB = "web"
    PAPER = "paper"
    PDF = "pdf"
    BOOK = "book"


class Source(BaseModel):
    title: str
    url: str
    content: str
    source_type: SourceType

