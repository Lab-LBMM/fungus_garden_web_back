from fastapi import FastAPI
from app.database import engine, Base

app = FastAPI(
    title="Fungus Garden Web API",
    description="API para gerenciamento e consulta de dados do projeto Fungus Garden",
    version="1.0.0",
)

@app.get("/")
def read_root():
    return {"message": "Fungus Garden Web API is running!"}
