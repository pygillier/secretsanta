from typing import Optional
from sqlmodel import SQLModel, Field


class Participant(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    dm_channel: str
