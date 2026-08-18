import os
from tavily import TavilyClient
from abc import ABC, abstractmethod
from app.domain.entities.source import Source,SourceType
from app.domain.entities.research_query import ResearchQuery

from dotenv import load_dotenv
load_dotenv()

class SourceRetriever(ABC):
    @abstractmethod
    def retrieve(self,query)->list[Source]:
        pass

class FakeSourceRetriever(SourceRetriever):
    def retrieve(self,query:ResearchQuery)->list[Source]:
        source1=Source(
            title="rag",
            url="www.example1.com",
            content="rag is good",
            source_type="pdf"
            )
        source2=Source(
            title="vector database",
            url="www.example2.com",
            content="vector is good",
            source_type="book"
            )
        
        return [source1,source2]

class WebSourceRetriever(SourceRetriever):
    def __init__(self):
        self.client = TavilyClient(
            api_key=os.getenv("TAVILY_API_KEY")
        )
        
    def retrieve(self, query: ResearchQuery) -> list[Source]:
        response = self.client.search(
            query.question,
            max_results=5
        )
        sources=[]
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