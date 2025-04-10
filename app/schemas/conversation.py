from pydantic import BaseModel
from typing import Optional


class ConversationCreateSchema(BaseModel):
    participant_id: int
    ad_id: int


class ConversationReadSchema(ConversationCreateSchema):
    conversation_id: int

    class Config:
        from_attributes = True


class ConversationUpdateSchema(BaseModel):
    participant_id: Optional[int] = None
    ad_id: Optional[int] = None
