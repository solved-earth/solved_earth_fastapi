from typing import Optional
from sqlmodel import Field, SQLModel

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True)

class Photo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(
        default=None, foreign_key="user.id"
    )
    challenge_id: Optional[int] = Field(
        default=None, foreign_key="challenge.id"
    )
    photo_url: str

class Challenge(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    challenge_name: str = Field(index=True)
    answer: str