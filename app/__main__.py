import uvicorn
from fastapi import FastAPI

from app.api.v1 import api_router
from app.core import settings

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(api_router, prefix=settings.API_ENDPOINT)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=settings.API_PORT)
