from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine) # create tables in the database

app = FastAPI()


@app.get("/quotes/")
def read_quotes(db: Session = Depends(get_db)):
    quotes = crud.get_quotes(db=db)
    return quotes


@app.post("/quotes/")
def create_quote(quote: schemas.QuoteCreate, db: Session = Depends(get_db)):
    crud.create_quote(db=db, quote=quote)
    return HTMLResponse(
        status_code=201,
        content="Quote created successfully"
    )
