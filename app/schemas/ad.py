from typing import Optional
from pydantic import BaseModel


class AdCreateSchema(BaseModel):
    owner_id: int
    title: str
    description: str
    age_requirements: Optional[int] = None
    nationality: Optional[str] = None
    budget: float
    number_of_roommates: int
    gender: str
    bad_habits: Optional[str] = None
    cleanliness: Optional[str] = None
    character: Optional[str] = None
    lifestyle: Optional[str] = None


class AdSchema(AdCreateSchema):
    id: int

    class Config:
        from_attributes = True


class AdUpdateSchema(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    age_requirements: Optional[int] = None
    nationality: Optional[str] = None
    budget: Optional[float] = None
    number_of_roommates: Optional[int] = None
    gender: Optional[str] = None
    bad_habits: Optional[str] = None
    cleanliness: Optional[str] = None
    character: Optional[str] = None
    lifestyle: Optional[str] = None
