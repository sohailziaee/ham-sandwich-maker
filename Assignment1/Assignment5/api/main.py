from fastapi import FastAPI
from api.dependencies.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Sandwich Maker API Running"}