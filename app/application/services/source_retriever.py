from abc import ABC, abstractmethod
from app.domain.entities.source import Source

class SourceRetriever(ABC):
    @abstractmethod
    def retrieve(self,query)->list[Source]:
        pass

class FakeSourceRetriever(SourceRetriever):
    def retrieve(self,query)->list[Source]:
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