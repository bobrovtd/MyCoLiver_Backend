from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class MessageBaseSchema(BaseModel):
    conversation_id: int
    sender_id: int
    text: str


class MessageCreateSchema(MessageBaseSchema):
    pass


class MessageUpdateSchema(BaseModel):
    text: Optional[str] = None
    viewed: Optional[bool] = None


class MessageResponseSchema(MessageBaseSchema):
    message_id: int
    sending_time: datetime
    sended: bool
    received: bool
    viewed: bool

    class Config:
        from_attributes = True
