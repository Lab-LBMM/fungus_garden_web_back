from fastapi import FastAPI
from sqlalchemy import text

from app.database import engine
from app.Controller.organismDetail_Controller import router as organism_detail_router
from app.Controller.bacterium_Controller import router as bacterium_router
from app.Controller.ant_Controller import router as ant_router
from app.Controller.fungi_Controller import router as fungi_router




app = FastAPI()

app.include_router(organism_detail_router)
app.include_router(bacterium_router)
app.include_router(ant_router)
app.include_router(fungi_router)

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