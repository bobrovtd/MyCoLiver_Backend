from fastapi import APIRouter, Depends
from app.schemas.user import UserCreateSchema, UserGetSchema, UserUpdateSchema
from app.repositories.user import UserRepository

router = APIRouter(
    prefix="/user",
    tags=["Пользователи"],
)


@router.post(
    "/",
    description="Создает нового пользователя в базе данных",
    response_description="Возвращает ID созданного пользователя",
)
async def create_user(data: UserCreateSchema = Depends()):
    new_user_id = await UserRepository.create_user(data)
    return {"id": new_user_id}


@router.get(
    "/{user_id}",
    description="Получает данные пользователя по ID из базы данных",
    response_description="Возвращает пользователя по ID",
)
async def get_user(user_id: int) -> UserGetSchema:
    user = await UserRepository.get_user(user_id)
    return user


@router.patch(
    "/{user_id}",
    description="Обновляет данные пользователя по ID в базе данных",
    response_description="Возвращает обновленные данные пользователя",
)
async def update_user(user_id: int, user_update: UserUpdateSchema) -> UserGetSchema:
    updated_user = await UserRepository.update_user(user_id, user_update)
    return updated_user


@router.delete(
    "/{user_id}",
    description="Удаляет пользователя по ID из базы данных",
    response_description="Возвращает сообщение об успешном удалении пользователя",
)
async def delete_user(user_id: int):
    await UserRepository.delete_user(user_id)
    return {"success": True}
