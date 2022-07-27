from typing import List

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.cats import get_cats
from app.db.session import get_session
from app.schemas.cats import CatSchema

router = APIRouter()


@router.get('/', response_model=List[CatSchema])
async def get_all_cats(
    session: AsyncSession = Depends(get_session),
    offset: int | None = Query(default=None),
    limit: int | None = Query(default=None),
):
    """Get list of all cats."""
    cats = await get_cats(session, offset, limit)
    return [
        CatSchema(
            name=cat.name,
            color=cat.color,
            tail_length=cat.tail_length,
            whiskers_length=cat.whiskers_length,
        ) for cat in cats
    ]
