"""Configure database."""
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.settings import settings

engine = create_async_engine(settings.SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False,
)


async def get_session() -> AsyncSession:
    """Dependency to create future sessions."""
    async with async_session() as session:
        yield session
