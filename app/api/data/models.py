#from sqlalchemy import Column, Integer, String
#from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, Field
from typing import Optional

#Base = declarative_base()

class Cocktail(BaseModel):
    #__tablename__ = "cocktails"

    id: Optional[int] = None
    #id = Column(Integer, primary_key=True, index=True)
    name: str = Field(min_length=5, max_length=30)
    #name = Column(String, index=True)
    ingredients: list[str]
    #ingredients = Column(String)
    recipet: list[str]
    #recipe = Column(String)
    #history = Column(String)
    history: str = Field(max_length=500)
    tags: list[str]
    image: str = Field(max_length=500)
    
    class Config:
        schema_extra = {
            "examples" : [
                {
                    "id" : 1,
                    "name": "Peach Bellini",
                    "ingredients": ["peach puree", "Prosecco"],
                    "recipet": ["Add peach puree to a chilled champagne flute.", "Top up with Prosecco and stir gently."],
                    "history" : "a little background of your new cocktail",
                    "tags": ["champagne flute", "Prosecco", "brunch"],
                    "image": "https://firebasestorage.googleapis.com/v0/b/mixology-af57f.appspot.com/o/christmas_champagne_cocktail.jpg?alt=media&token=9b7da4d4-cd8d-4a48-97c2-da2836e0d339"
                }
            ]
        }
    

#class CocktailAsIngredient(Base):
    #__tablename__ = "cocktails"
