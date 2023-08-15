from datetime import date
from typing import Optional

from pydantic import BaseModel, Field, validator


class ContactsSchema(BaseModel):
    name: str = Field(max_length=50, min_length=3)
    surname: str = Field(max_length=100, min_length=3)
    email: str = Field(max_length=50, min_length=3)
    phone: str = Field(max_length=20, min_length=5)
    bd: str
    city: str = Field(max_length=50, min_length=3)
    notes: str = Field(max_length=300, min_length=3)

    # @validator('bd')
    # def string_to_date(cls, value):
    #     try:
    #         return date.fromisoformat(value)
    #     except ValueError:
    #         raise ValueError("Invalid date format. Use 'YYYY-MM-DD' format.")


class ContactsUpdateSchema(ContactsSchema):
    pass


class ContactsResponse(BaseModel):
    id: int = 1
    name: str
    surname: str
    email: str
    phone: str
    bd: str
    city: str
    notes: str


    class Config:
        from_attributes = True