from app.domain.entities.research_query import ResearchQuery
from app.domain.entities.research_result import ResearchResult


class ResearchService:
    def research(self, query: ResearchQuery) -> ResearchResult:
        raise NotImplementedError