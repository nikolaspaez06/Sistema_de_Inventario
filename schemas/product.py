from pydantic import BaseModel, Field
from typing import Optional


class Product(BaseModel):
    id: Optional[int]=None
    name : str = Field(max_length=40, min_length=2,description="product name")
    brand : str = Field(max_length=30, min_length=2,description="name of product brand")
    description : str =Field(max_length=100, min_length=8,description="product description")
    price : float = Field(ge=100, le=None)
    entry_date : str = Field(max_length=50, min_length=5,description="product delivery date")
class Config:
        schema_extra = {
            "example":{
                'id':1,
                'name':'vive100',
                'brand':'vive100',
                'description':'exquisito producto para recargarte el dia',
                'price':2000,
                'entry_date':'29/05/2023',
            }
        }