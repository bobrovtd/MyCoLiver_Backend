from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Model


class Conversation(Model):
    __tablename__ = "conversations"

    conversation_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    participant_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.user_id"))
    ad_id: Mapped[int] = mapped_column(Integer, ForeignKey("ad.ad_id"))
