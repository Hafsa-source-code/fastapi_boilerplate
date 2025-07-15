from web import engine
from sqlalchemy import text
from lib_pharma.models.persons import GetAllPersonsResponse, Person
from libsql.sql import sql


def create_person(person: Person):
    with engine.begin() as conn:
        sql(conn).insert_one('persons', {
            "fname": person.first_name,
            "lname": person.last_name,
            "age": person.age
        })
    return {
        "first_name": person.first_name,
        "last_name": person.last_name,
        "age": person.age,
    }


def get_persons():
    with engine.begin() as conn:
        rows = sql(conn, "SELECT fname, lname, age FROM persons").dicts()
    persons = []
    for row in rows:
        person = Person(first_name=row["fname"], last_name=row["lname"], age=row["age"])
        persons.append(person)

    return GetAllPersonsResponse(persons=persons)

def get_person_by_name(full_name: str):
    first_name, last_name = full_name.split(" ", 1)
    with engine.begin() as conn:
        row = sql(
            conn,
            "SELECT fname, lname, age FROM persons WHERE fname = :fname AND lname = :lname",
            {"fname": first_name, "lname": last_name}
        ).dict()
    if row:
        return Person(first_name=row["fname"], last_name=row["lname"], age=row["age"])
    return None
