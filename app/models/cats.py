"""Model for cat."""
from sqlalchemy import Column, Enum, Integer

from app.db.base_class import Base

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

    name = Column(Integer, primary_key=True)
    color = Column(cat_color)
    tail_length = Column(Integer)
    whiskers_length = Column(Integer)

    def __repr__(self) -> str:
        """Cat representation."""
        return f'{self.name}'
