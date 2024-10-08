from pydantic import BaseModel, EmailStr, conint
from typing import Optional
from datetime import date
from decimal import Decimal
class UserCreate(BaseModel):
    name: str
    lastname: str
    identification: str
    second_name: Optional[str] 
    first_surname: str
    second_surname: Optional[str] 
    institutional_email: EmailStr #forma de validar un correo que tiene pydantic
    phone_number: str
    birth_date: str
    gender_id: int
    user_type_id: int
    institution_id: int
    date_registered: date
    rating: Decimal 
    total_ratings: int

class UserResponse(BaseModel):
    id: int
    name: str
    lastname: str
    identification: str
    second_name: Optional[str] 
    first_surname: str
    second_surname: Optional[str] 
    institutional_email: EmailStr
    phone_number: str
    birth_date: str
    gender_id: int
    user_type_id: int
    institution_id: int
    date_registered: date
    rating: Decimal 
    total_ratings: int

    class Config:
        orm_mode = True
