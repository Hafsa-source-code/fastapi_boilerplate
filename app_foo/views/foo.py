from fastapi import APIRouter

router = APIRouter()


@router.get("/get_all")
def get_foo():
    return {"message": "foo endpoint is under construction."}
