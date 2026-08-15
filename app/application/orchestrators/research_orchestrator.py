from app.domain.entities.research_query import ResearchQuery
from app.domain.entities.research_result import ResearchResult

class ResearchOrchestrator:

    def research(self, query: ResearchQuery) -> ResearchResult:
        raise NotImplementedError