from pydantic import BaseModel

class QuoteBase(BaseModel):
    text: str
    author: str

class QuoteCreate(QuoteBase):
    pass

class Quote(QuoteBase):
    id: int

    class Config:
        from_attributes = True

