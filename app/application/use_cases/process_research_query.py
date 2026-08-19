from app.domain.entities.research_query import ResearchQuery
from app.application.services.research_service import ResearchService
from app.application.orchestrators.research_orchestrator import ResearchOrchestrator


class ProcessResearchQuery:

    def __init__(self, orchestration: ResearchOrchestrator):
        self.orchestration = orchestration

    def execute(self, query: ResearchQuery):
        return self.orchestration.research(query)