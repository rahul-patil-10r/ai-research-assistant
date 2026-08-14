from pydantic import BaseModel
from enum import Enum

class MessageRole(str,Enum):
    USER="user",
    ASSISTANT="assitant",
    SYSTEM="system"

class Message(BaseModel):
    role:MessageRole
    content:str

