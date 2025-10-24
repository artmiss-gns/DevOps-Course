from sqlalchemy.orm import Session

from . import models, schemas


def get_quotes(db: Session):
    return db.query(models.Quote).all()


def create_quote(db: Session, quote: schemas.QuoteCreate):
    db_quote = models.Quote(text=quote.text, author=quote.author)
    db.add(db_quote)
    db.commit()
    db.refresh(db_quote)

