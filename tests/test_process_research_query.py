from app.application.services.research_service import ResearchService
from app.domain.entities.research_query import ResearchQuery
from app.domain.entities.research_result import ResearchResult
from app.domain.entities.source import Source
from app.application.use_cases.process_research_query import ProcessResearchQuery
from app.application.services.research_service import DefaultResearchService
from app.application.orchestrators.research_orchestrator import ResearchOrchestrator
from app.application.services.source_retriever import FakeSourceRetriever
from app.application.services.answer_generator import AnswerGenerator
from app.application.services.source_retriever import WebSourceRetriever
from app.infrastruture.llm.llm_service import OllamaLLMService




def test_process_research_query():

    query = ResearchQuery(
        question="What is RAG?",
        depth="deep",
        research_type="technical"
    )

    llm_service=OllamaLLMService()
    
    source_retriever = WebSourceRetriever()

    answer_generator = AnswerGenerator(llm_service)
    
    research_service = DefaultResearchService(source_retriever,answer_generator)

    use_case = ProcessResearchQuery(research_service)

    result = use_case.execute(query)
    

    print("ANSWER IS : \n",result.answer)
    print("\n")
    print("SOURCES ARE : \n",result.sources)
    
    assert isinstance(result, ResearchResult)
    assert len(result.answer) > 0
    assert len(result.sources) > 0