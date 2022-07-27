from pydantic import BaseModel


class CatSchema(BaseModel):
    """Schema for cat."""

    name: str
    color: str
    tail_length: int
    whiskers_length: int
