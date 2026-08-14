from pydantic import BaseModel
from app.domain.entities.source import Source,SourceType


class ResearchResult(BaseModel):
    answer: str
    sources: list[Source]

