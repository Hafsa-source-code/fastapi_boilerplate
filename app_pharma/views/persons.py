from fastapi import APIRouter
from jsql import sql
from lib_pharma.models.persons import GetAllPersonsResponse, Person
from lib_pharma import persons

router = APIRouter()


@router.post("/create/", response_model=Person)
def create_item(person: Person):
    created_person = persons.create_person(person)
    return created_person  # Assuming this returns a dict with the created person data


@router.get("/get_all", response_model=GetAllPersonsResponse)
def get_persons():
    persons_data = persons.get_persons()
    return persons_data

@router.get("/get_by_name/{full_name}", response_model=Person)
def get_person_by_name(full_name: str):
    person = persons.get_person_by_name(full_name)
    if person:
        return person
    return {"error": "Person not found"}