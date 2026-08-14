from app.domain.entities.research_query import ResearchQuery
from app.application.services.research_service import ResearchService


class ProcessResearchQuery:

    def __init__(self, research_service: ResearchService):
        self.research_service = research_service

    def execute(self, query: ResearchQuery):
        return self.research_service.research(query)