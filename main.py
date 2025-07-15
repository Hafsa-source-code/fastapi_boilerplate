from fastapi import FastAPI
from app_pharma.views.persons import router as persons_router
from app_pharma.views.pharmacy import router as pharmacy_router

app = FastAPI()
app.include_router(persons_router, prefix="/persons", tags=["persons"])
app.include_router(pharmacy_router, prefix="/pharmacy", tags=["pharmacy"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}
