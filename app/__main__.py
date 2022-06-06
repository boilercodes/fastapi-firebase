import uvicorn

from app.api.v1 import api_router
from app.core import settings
from fastapi import FastAPI

app = FastAPI(title=settings.api.name)
app.include_router(api_router, prefix=settings.api.endpoint)

if __name__ == "__main__":
    uvicorn.run("app.__main__:app", host=settings.api.host, port=settings.api.port)
