from pydantic import BaseModel
from enum import Enum

class MessageRole(str,Enum):
    USER="user",
    ASSISTANT="assitant",
    SYSTEM="system"

class Message(BaseModel):
    role:MessageRole
    content:str


message=Message(role=MessageRole.USER,content="what is rag" )
print(message)