from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import new_session
from app.models.user import User
from app.schemas.user import UserCreateSchema, UserGetSchema, UserUpdateSchema


class UserRepository:
    @classmethod
    async def create_user(cls, user: UserCreateSchema) -> int:
        """
        Создает нового пользователя в базе данных.
        """
        async with new_session() as session:
            new_user = User(**user.model_dump())

            session.add(new_user)
            try:
                await session.commit()
                await session.refresh(new_user)
            except Exception:
                await session.rollback()
                raise

            return new_user.user_id

    @classmethod
    async def get_user(cls, user_id: int) -> UserGetSchema:
        """
        Получает пользователя по ID.
        """
        async with new_session() as session:
            user_model = await cls._get_user_or_404(session, user_id)
            return UserGetSchema.model_validate(user_model)

    @classmethod
    async def update_user(cls, user_id: int, user_update: UserUpdateSchema) -> UserGetSchema:
        """
        Обновляет данные пользователя по ID.
        """
        async with new_session() as session:
            user_model = await cls._get_user_or_404(session, user_id)

            for key, value in user_update.model_dump(exclude_unset=True).items():
                setattr(user_model, key, value)

            try:
                await session.commit()
            except Exception:
                await session.rollback()
                raise

            return UserGetSchema.model_validate(user_model)

    @classmethod
    async def delete_user(cls, user_id: int) -> None:
        """
        Удаляет пользователя по ID.
        """
        async with new_session() as session:
            user_model = await cls._get_user_or_404(session, user_id)
            session.delete(user_model)

            try:
                await session.commit()
            except Exception:
                await session.rollback()
                raise

    @classmethod
    async def _get_user_or_404(cls, session: AsyncSession, user_id: int) -> User:
        """
        Вспомогательный метод для получения пользователя или выбрасывания 404.
        """
        query = select(User).where(User.user_id == user_id)
        result = await session.execute(query)
        user_model = result.scalar_one_or_none()
        if user_model is None:
            raise HTTPException(status_code=404, detail="Пользователь не найден")
        return user_model
