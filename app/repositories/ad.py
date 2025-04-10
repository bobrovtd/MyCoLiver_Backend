from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import new_session
from app.models.ad import Ad
from app.schemas.ad import AdCreateSchema, AdSchema, AdUpdateSchema


class AdRepository:
    @classmethod
    async def create_ad(cls, ad: AdCreateSchema) -> int:
        """
        Создает новое объявление в базе данных.
        """
        async with new_session() as session:
            data = ad.model_dump()
            new_ad = Ad(**data)

            session.add(new_ad)
            try:
                await session.commit()
            except Exception:
                await session.rollback()
                raise
            return new_ad.id

    @classmethod
    async def get_ads(cls) -> list[AdSchema]:
        """
        Получает все объявления из базы данных.
        """
        async with new_session() as session:
            query = select(Ad)
            result = await session.execute(query)
            ad_models = result.scalars().all()
            return [AdSchema.model_validate(ad) for ad in ad_models]

    @classmethod
    async def get_ad(cls, ad_id: int) -> AdSchema:
        """
        Получает объявление из базы данных по его ID.
        """
        async with new_session() as session:
            ad_model = await cls._get_ad_or_404(session, ad_id)
            return AdSchema.model_validate(ad_model)

    @classmethod
    async def delete_ad(cls, ad_id: int) -> None:
        """
        Удаляет объявление из базы данных по его ID.
        """
        async with new_session() as session:
            ad_model = await cls._get_ad_or_404(session, ad_id)
            session.delete(ad_model)
            try:
                await session.commit()
            except Exception:
                await session.rollback()
                raise

    @classmethod
    async def update_ad(cls, ad_id: int, ad_update: AdUpdateSchema) -> AdSchema:
        """
        Обновляет данные объявления в базе данных по его ID.
        """
        async with new_session() as session:
            ad_model = await cls._get_ad_or_404(session, ad_id)

            for key, value in ad_update.model_dump(exclude_unset=True).items():
                setattr(ad_model, key, value)

            try:
                await session.commit()
            except Exception:
                await session.rollback()
                raise

            return AdSchema.model_validate(ad_model)

    @classmethod
    async def _get_ad_or_404(cls, session: AsyncSession, ad_id: int) -> Ad:
        """
        Вспомогательный метод для получения объявления или выбрасывания 404.
        """
        query = select(Ad).where(Ad.id == ad_id)
        result = await session.execute(query)
        ad_model = result.scalar_one_or_none()
        if ad_model is None:
            raise HTTPException(status_code=404, detail="Объявление не найдено")
        return ad_model
