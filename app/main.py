from fastapi import FastAPI

from app.api.api import api_router
from app.settings import settings

app = FastAPI(title=settings.APP_NAME)

app.include_router(api_router, prefix=settings.API_VERSION)
