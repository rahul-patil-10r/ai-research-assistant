from abc import ABC, abstractmethod

from app.domain.entities.research_query import ResearchQuery
from app.domain.entities.source import Source


class AnswerGenerator(ABC):
    @abstractmethod
    def generate(self,query: ResearchQuery,sources: list[Source]) -> str:
        pass


class FakeAnswerGenerator(AnswerGenerator):

    def generate(self,query:ResearchQuery,source:Source)->str:
        return f"fake answer for :{query.question} is "