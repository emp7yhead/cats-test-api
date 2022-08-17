"""Model for cat."""
from sqlalchemy import Column, Enum, Integer, String

from app.db.base_class import Base

NAME_LENGTH = 20

cat_color = Enum(
    'black',
    'white',
    'black & white',
    'red',
    'red & black & white',
    'red & white',
    name='catcolor',
)


class Cats(Base):
    """Define cat model."""

    __tablename__ = 'cats'

    name = Column(String(NAME_LENGTH), primary_key=True)
    color = Column(cat_color)
    tail_length = Column(Integer)
    whiskers_length = Column(Integer)

    def __repr__(self) -> str:
        """Cat representation."""
        return f'{self.name}'
