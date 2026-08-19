from abc import ABC, abstractmethod

from app.domain.entities.research_query import ResearchQuery
from app.domain.entities.research_result import ResearchResult
from app.application.services.research_service import ResearchService


class ResearchOrchestrator(ABC):

    @abstractmethod
    def research(self, query: ResearchQuery) -> ResearchResult:
        pass


class DefaultResearchOrchestrator(ResearchOrchestrator):

    def __init__(self, research_service: ResearchService):
        self.research_service = research_service

    def research(self, query: ResearchQuery) -> ResearchResult:
        return self.research_service.research(query)