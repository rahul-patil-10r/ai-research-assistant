import ollama 
import requests
from app.application.services.llm_service import LLMService
# from app.application.services.answer_generator import AnswerGenerator
# from app.domain.entities.source import Source,SourceType
# from app.domain.entities.research_query import ResearchQuery



class OllamaLLMService(LLMService):
    def generate(self,prompt:str)->str:
        response=ollama.chat(
            model="llama3:latest",
            messages=[
                    {
                        "role":"user",
                        "content":prompt
                    }
                ]
            )
        return response["message"]["content"]