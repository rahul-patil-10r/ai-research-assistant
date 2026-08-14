from pydantic import BaseModel
from enum import Enum

class Depth(str,Enum):
    BASIC="basic"
    STANDARD="standard"
    DEEP="deep"
    
class ResearchType(str,Enum):
    TECHNICAL="technical"
    GENERAL="general"
    COMPARATIVE="comparative"

class ResearchQuery(BaseModel):
    question:str
    depth:Depth
    research_type:ResearchType

