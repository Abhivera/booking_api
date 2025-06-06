from pydantic import BaseModel, EmailStr
from datetime import datetime

class FitnessClassBase(BaseModel):
    name: str
    datetime: datetime
    instructor: str
    available_slots: int

class FitnessClassResponse(FitnessClassBase):
    id: int

    class Config:
        orm_mode = True

class BookingRequest(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr

class BookingResponse(BaseModel):
    id: int
    class_id: int
    client_name: str
    client_email: EmailStr

    class Config:
        orm_mode = True
