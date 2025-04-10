from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

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

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def welcome():
    return """
    <!doctype html>
    <html lang="ru">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>FastAPI Приветствие</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
      </head>
      <body class="bg-dark text-white text-center d-flex flex-column justify-content-center align-items-center" style="height: 100vh;">
        <div>
          <h1 class="display-4">👋 Добро пожаловать!</h1>
          <p class="lead">Вы запустили FastAPI-приложение.</p>
          <a href="/docs" class="btn btn-outline-light mt-3">Открыть документацию</a>
        </div>
      </body>
    </html>
    """

app.include_router(ad_router)
