from pydantic import BaseModel
from source import Source, SourceType


class ResearchResult(BaseModel):
    answer: str
    sources: list[Source]


source1 = Source(
    title="RAG Paper",
    url="example.com/rag",
    content="RAG combines retrieval and generation.",
    source_type=SourceType.PAPER
)

source2 = Source(
    title="RAG Documentation",
    url="example.com/docs",
    content="RAG retrieves relevant information before generating an answer.",
    source_type=SourceType.WEB
)


research = ResearchResult(
    answer="RAG is a technique that combines retrieval and generation.",
    sources=[source1, source2]
)

print(research)