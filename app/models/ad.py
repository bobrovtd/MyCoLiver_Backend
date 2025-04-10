from sqlalchemy import Integer, String, Text, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Model


class Ad(Model):
    __tablename__ = "ads"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    owner_id: Mapped[int] = mapped_column(Integer, nullable=False)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    age_requirements: Mapped[int] = mapped_column(Integer, nullable=True)
    nationality: Mapped[str] = mapped_column(String, nullable=True)
    budget: Mapped[DECIMAL] = mapped_column(DECIMAL, nullable=False)
    number_of_roommates: Mapped[int] = mapped_column(Integer, nullable=False)
    gender: Mapped[str] = mapped_column(String, nullable=False)
    bad_habits: Mapped[str] = mapped_column(String, nullable=True)
    cleanliness: Mapped[str] = mapped_column(String, nullable=True)
    character: Mapped[str] = mapped_column(String, nullable=True)
    lifestyle: Mapped[str] = mapped_column(String, nullable=True)
