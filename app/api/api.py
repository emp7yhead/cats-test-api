from fastapi import APIRouter

from app.api.endpoints import cats, ping

api_router = APIRouter()
api_router.include_router(ping.router, prefix='/ping', tags=['ping'])
api_router.include_router(cats.router, prefix='/cats', tags=['cats'])
