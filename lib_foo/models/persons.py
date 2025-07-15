from pydantic import BaseModel, Field
from typing import List, Optional
from decimal import Decimal


class Person(BaseModel):
    first_name: str
    last_name: str
    age: Decimal


class CreatePersonRequest(BaseModel):
    fname: str
    lname: str
    age: Decimal


class GetAllPersonsResponse(BaseModel):
    persons: List[Person]
