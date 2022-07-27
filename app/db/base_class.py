from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    """Generate declarative base."""

    id: Any
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        """Generate tablename."""
        return cls.__name__.lower()
