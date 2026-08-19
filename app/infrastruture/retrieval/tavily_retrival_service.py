import os

from dotenv import load_dotenv
from tavily import TavilyClient

from app.application.services.source_retriever import SourceRetriever
from app.domain.entities.research_query import ResearchQuery
from app.domain.entities.source import Source, SourceType


load_dotenv()


class TavilySourceRetriever(SourceRetriever):

    def __init__(self):
        self.client = TavilyClient(
            api_key=os.getenv("TAVILY_API_KEY")
        )

    def retrieve(self, query: ResearchQuery) -> list[Source]:

        response = self.client.search(
            query.question,
            max_results=5
        )

        sources = []

        for result in response["results"]:

            sources.append(
                Source(
                    title=result["title"],
                    url=result["url"],
                    content=result["content"],
                    source_type=SourceType.WEB
                )
            )

        return sources