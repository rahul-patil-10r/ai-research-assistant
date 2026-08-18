from abc import ABC, abstractmethod
from app.domain.entities.research_query import ResearchQuery
from app.domain.entities.research_result import ResearchResult
from app.application.services.source_retriever import SourceRetriever
from app.application.services.answer_generator import AnswerGenerator


class ResearchService(ABC):

    @abstractmethod
    def research(self, query: ResearchQuery) -> ResearchResult:
        pass

class DefaultResearchService(ResearchService):

    def __init__(
        self,
        source_retriever: SourceRetriever,
        answer_generator: AnswerGenerator
    ):
        self.source_retriever = source_retriever
        self.answer_generator = answer_generator

    def research(self, query: ResearchQuery) -> ResearchResult:
        sources = self.source_retriever.retrieve(query)

        answer = self.answer_generator.generate(query, sources)

        return ResearchResult(
            answer=answer,
            sources=sources
        )