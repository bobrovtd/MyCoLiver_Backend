from sqlalchemy import Integer, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Model


class Message(Model):
    __tablename__ = "messages"

    message_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    conversation_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("conversations.conversation_id"), nullable=False
    )
    sender_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.user_id"), nullable=False
    )
    text: Mapped[str] = mapped_column(Text, nullable=False)
    sending_time: Mapped[DateTime] = mapped_column(DateTime)
    sended: Mapped[bool] = mapped_column(Boolean)
    received: Mapped[bool] = mapped_column(Boolean)
    viewed: Mapped[bool] = mapped_column(Boolean)
