from fastapi import APIRouter
from jsql import sql
from web import engine
from sqlalchemy import text

router = APIRouter()


@router.get("/get_all")
def get_pharmacy():
    return {"message": "Pharmacy endpoint is under construction."}
