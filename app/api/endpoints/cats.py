from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.cats import get_cats, post_cat
from app.db.session import get_session
from app.schemas.cats import CatSchema

router = APIRouter()


@router.get('/', response_model=List[CatSchema])
async def get_all_cats(
    session: AsyncSession = Depends(get_session),
    offset: int | None = Query(default=None),
    limit: int | None = Query(default=None),
) -> List[CatSchema]:
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


@router.post('/')
async def create_cat(
    cat: CatSchema,
    session: AsyncSession = Depends(get_session),
) -> CatSchema:
    """Post a cat."""
    new_cat = post_cat(
        session=session,
        name=cat.name,
        color=cat.color,
        tail_length=cat.tail_length,
        whiskers_length=cat.whiskers_length,
    )
    try:  # noqa: WPS229
        await session.commit()
        return new_cat
    except IntegrityError:
        await session.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Cat already exists!',
        )
