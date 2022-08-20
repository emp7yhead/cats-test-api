from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.cats import Cats
from app.schemas.cats import CatSchema


async def get_cats(
    session: AsyncSession,
    offset: int,
    limit: int,
) -> List[CatSchema]:
    """Get cats with/or offset and limit."""
    all_cats = await session.execute(
        select(Cats).limit(limit).offset(offset),
    )
    return all_cats.scalars().all()


def post_cat(
    session: AsyncSession,
    name: str,
    color: str,
    tail_length: int,
    whiskers_length: int,
) -> CatSchema:
    """Post cat to database."""
    new_cat = Cats(
        name=name,
        color=color,
        tail_length=tail_length,
        whiskers_length=whiskers_length,
    )
    session.add(new_cat)
    return new_cat
