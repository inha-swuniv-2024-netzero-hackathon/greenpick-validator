from pydantic import BaseModel


class Product(BaseModel):
    name: str


class ProductScore(BaseModel):
    score: int
