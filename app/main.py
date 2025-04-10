from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.core.database import create_tables, delete_tables

from app.api.v1.ad import router as ad_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    print("База готова")
    yield
    await delete_tables()
    print("База очищена")


app = FastAPI(lifespan=lifespan)

app.include_router(ad_router)
