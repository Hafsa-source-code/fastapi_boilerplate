from fastapi import FastAPI
from app_foo.views.persons import router as persons_router
from app_foo.views.foo import router as foo_router

app = FastAPI()
app.include_router(persons_router, prefix="/persons", tags=["persons"])
app.include_router(foo_router, prefix="/foo", tags=["foo"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}
