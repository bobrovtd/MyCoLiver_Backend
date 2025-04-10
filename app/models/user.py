from sqlalchemy import Integer, String, Date
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Model


class User(Model):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    surname: Mapped[str] = mapped_column(String, nullable=False)
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    photo: Mapped[str] = mapped_column(String, nullable=True)
    gender: Mapped[str] = mapped_column(String, nullable=False)
    date_of_birth: Mapped[Date] = mapped_column(Date, nullable=False)
