from fastapi import FastAPI
from sqlalchemy import text

from app.database import engine


app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "LBMM API funcionando!"
    }


@app.get("/test-database")
def test_database():

    with engine.connect() as connection:

        result = connection.execute(
            text("SELECT DATABASE()")
        )

        database_name = result.fetchone()

        return {
            "database": database_name[0]
        }