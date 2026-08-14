from app.domain.entities.research_query import ResearchQuery
from app.application.use_cases.process_research_query import ProcessResearchQuery


class FakeResearchService:
    def research(self, query):
        return query


def test_process_research_query():
    query = ResearchQuery(
        question="What is RAG?",
        depth="deep",
        research_type="technical"
    )

    research_service = FakeResearchService()

    use_case = ProcessResearchQuery(research_service)

    result = use_case.execute(query)

    assert result == query