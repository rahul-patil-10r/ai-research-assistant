from app.application.services.research_service import ResearchService
from app.domain.entities.research_query import ResearchQuery
from app.domain.entities.research_result import ResearchResult
from app.domain.entities.source import Source
from app.application.use_cases.process_research_query import ProcessResearchQuery
from app.application.services.research_service import DefaultResearchService
from app.application.orchestrators.research_orchestrator import ResearchOrchestrator


class FakeResearchOrchestrator(ResearchOrchestrator):
    
    def research(self, query: ResearchQuery) -> ResearchResult:
        source = Source(
            title="RAG Paper",
            url="https://example.com/rag",
            content="RAG combines retrieval with generation.",
            source_type="paper"
        )

        return ResearchResult(
            answer="RAG stands for Retrieval-Augmented Generation.",
            sources=[source]
        )


def test_process_research_query():

    query = ResearchQuery(
        question="What is RAG?",
        depth="deep",
        research_type="technical"
    )

    research_service = FakeResearchOrchestrator()

    use_case = ProcessResearchQuery(research_service)

    result = use_case.execute(query)

    assert isinstance(result, ResearchResult)
    assert result.answer == "RAG stands for Retrieval-Augmented Generation."
    assert len(result.sources) == 1