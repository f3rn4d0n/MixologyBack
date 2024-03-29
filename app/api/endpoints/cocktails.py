from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import JSONResponse
#from sqlalchemy.ext.asyncio import AsyncSession
from app.api.data import models, crud
from app.api.data.models import Cocktail
#from app.api.data.database import database, metadata
import json
import math

router = APIRouter()

# Specify the path to your JSON file

listRecipes = []

@router.get("/resume")
async def get_resume():
  return {
    "data": [
      {
        "name": "For you",
        "section": "foryou",
        "data": listRecipes[0:10] 
      },
      {
        "name": "Favorites",
        "section": "favorites",
        "data": listRecipes[0:10]
      },
      {
        "name": "Season",
        "section": "season",
        "data": listRecipes[0:10]
      }
    ]
  }

@router.get("/cocktail")
async def get_cocktail(
  limit: int = Query(20, ge= 0),
  page: int = Query(0, ge= 0),
): 
  origin = limit * (page - 1)
  offset = origin
  if offset < 0:
    offset = 0
  end = origin + limit
  total_pages = (float(len(listRecipes)) / float(limit))
  return {
    "pagination": {
      "total": len(listRecipes),
      "limit": limit,
      "offset": offset,
      "total_pages": math.ceil(total_pages),
      "current_page": page
    },
    "data": listRecipes[origin:end] 
  }
  
@router.post("/cocktail")
async def create_cocktail(cocktail: Cocktail): 
  if not listRecipes:
    new_id = 1
  else:
    last_cocktail = listRecipes[-1]
    new_id = last_cocktail.id + 1
  cocktail.id = new_id
  listRecipes.append(cocktail)
  return cocktail
  
@router.put("/cocktail/{item_id}")
async def update_cocktail(item_id: int, cocktail: Cocktail): 
  resultados = list(filter(lambda x: x.id == item_id, listRecipes))
  if resultados:
    item_founded = listRecipes.index(resultados[0])
    cocktail.id = listRecipes[item_founded].id
    listRecipes[item_founded] = cocktail
    return cocktail
  raise HTTPException(status_code=404, detail="cocktail not found")
  
@router.delete("/cocktail/{item_id}")
async def delete_cocktail(item_id: int): 
  resultados = list(filter(lambda x: x.id == item_id, listRecipes))
  if resultados:
    item_founded = listRecipes.index(resultados[0])
    del listRecipes[item_founded]
    return {"message": "Item deleted"}
  raise HTTPException(status_code=404, detail="cocktail not found")