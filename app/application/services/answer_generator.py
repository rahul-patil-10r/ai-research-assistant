from abc import ABC, abstractmethod
from app.application.services.llm_service import LLMService
from app.domain.entities.research_query import ResearchQuery
from app.domain.entities.source import Source


class AnswerGenerator():
    def __init__(self,llm_service:LLMService):
        self.llm_service=llm_service
        
    def generate(self,query: ResearchQuery,sources: list[Source]) -> str:
        
        context = "\n\n".join(

            f"Title: {source.title}\n"

            f"Content: {source.content}"

            for source in sources

        )
        prompt = f"""

    Answer the question using the provided sources.

    Question:

    {query.question}

    Sources:

    {context}

    Give a clear and accurate answer.

    """

        return self.llm_service.generate(prompt)
        
        
      
