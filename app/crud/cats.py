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
