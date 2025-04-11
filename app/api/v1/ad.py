from fastapi import APIRouter, Depends
from app.schemas.ad import AdCreateSchema, AdSchema, AdUpdateSchema
from app.repositories.ad import AdRepository

router = APIRouter(
    prefix="/ads",
    tags=["Объявления"],
)


@router.post(
    "/",
    description="Добавляет объявление в базу данных",
    response_description="Возвращает ID созданного объявления",
)
async def create_ad(data: AdCreateSchema = Depends()):
    new_ad_id = await AdRepository.create_ad(data)
    return {"id": new_ad_id}


@router.get(
    "/",
    description="Получает все объявления из базы данных",
    response_description="Возвращает список всех объявлений",
)
async def get_ads() -> list[AdSchema]:
    ads = await AdRepository.get_ads()
    return ads


@router.get(
    "/{ad_id}",
    description="Получает объявление по ID из базы данных",
    response_description="Возвращает объявление по ID",
)
async def get_ad(ad_id: int) -> AdSchema:
    ad = await AdRepository.get_ad(ad_id)
    return ad


@router.delete(
    "/{ad_id}",
    description="Удаляет объявление по ID из базы данных",
    response_description="Возвращает сообщение об успешном удалении объявления",
)
async def delete_ad(ad_id: int):
    await AdRepository.delete_ad(ad_id)
    return {"success": True}


@router.patch(
    "/{ad_id}",
    description="Обновляет данные объявления по ID в базе данных",
    response_description="Возвращает обновленное объявление",
)
async def update_ad(ad_id: int, ad_update: AdUpdateSchema) -> AdSchema:
    updated_ad = await AdRepository.update_ad(ad_id, ad_update)
    return updated_ad
