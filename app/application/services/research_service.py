from abc import ABC, abstractmethod

from app.domain.entities.research_query import ResearchQuery
from app.domain.entities.research_result import ResearchResult


class ResearchService(ABC):

    @abstractmethod
    def research(self, query: ResearchQuery) -> ResearchResult:
        pass

    
class DefaultResearchService(ResearchService):
     def research(self, query: ResearchQuery) -> ResearchResult:

        return ResearchResult(
            answer=f"Research requested for: {query.question}",
            sources=[]
        )