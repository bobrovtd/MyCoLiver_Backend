from fastapi import HTTPException
from sqlalchemy import select
from app.core.database import new_session
from app.models.ad import Ad
from app.schemas.ad import AdCreateSchema, AdSchema


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
            await session.flush()
            await session.commit()
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
            query = select(Ad).where(Ad.id == ad_id)
            result = await session.execute(query)
            ad_model = result.scalar_one_or_none()
            if ad_model is None:
                raise HTTPException(status_code=404, detail="Объявление не найдено")

            return AdSchema.model_validate(ad_model)
