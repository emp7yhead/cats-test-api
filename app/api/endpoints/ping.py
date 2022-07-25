from fastapi import APIRouter

router = APIRouter()


@router.get('/')
async def ping() -> str:
    """Ping endpoint."""
    return 'Cats Service. Version 0.1'
