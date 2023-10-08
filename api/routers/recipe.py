from fastapi import APIRouter, Depends
import api.schemas.recipe as recipe_schema
from sqlalchemy.orm import Session
from api.db import get_db
import api.cruds.recipe as recipe_crud
router = APIRouter()


@router.post("/recipes/init/", response_model=recipe_schema.Post_responce)
async def init_db_data(request_body: recipe_schema.Initialize_post_request, db: Session = Depends(get_db)):
    if not request_body:
        return {"message": "Recipe creation failed!", "required": "id, title, making_time, serves, ingredients, cost, created_at, updated_at"}
    db_recipe = recipe_crud.init_db_data(db, request_body)
    return {"message": "Recipe successfully created!", "recipe": [db_recipe]}


@router.post("/recipes/", response_model=recipe_schema.Post_responce)
async def create_recipe(request_body: recipe_schema.Post_request, db: Session = Depends(get_db)):
    if not request_body:
        return {"message": "Recipe creation failed!", "required": "title, making_time, serves, ingredients, cost"}
    db_recipe = recipe_crud.create_recipe(db, request_body)
    return {"message": "Recipe successfully created!", "recipe": [db_recipe]}
    return recipe_schema.Post_responce(message="Recipe successfully created!", recipe=[recipe_schema.Recipe_id_create_update(**request_body.dict(), id=1, created_at="2016-01-10 12:10:12", updated_at="2016-01-10 12:10:12")])


@router.get("/recipes/", response_model=recipe_schema.Getall_responce)
async def get_recipes(db: Session = Depends(get_db)):
    db_recipe = recipe_crud.getall_recipe(db)
    return {"recipes": db_recipe}
    return recipe_schema.Getall_responce(recipes=[recipe_schema.Recipe_id(id=1, title="title", making_time="making_time", serves="serves", ingredients="ingredients", cost=100)])


@router.get("/recipes/{id}", response_model=recipe_schema.Getid_responce)
async def get_recipe(id: int, db: Session = Depends(get_db)):
    db_recipe = recipe_crud.getid_recipe(db, id)
    return {"message": "Recipe details by id", "recipe": [db_recipe]}
    return recipe_schema.Getid_responce(message="Recipe details by id", recipe=[recipe_schema.Recipe_id(id=id, title="title", making_time="making_time", serves="serves", ingredients="ingredients", cost=100)])


@router.patch("/recipes/{id}", response_model=recipe_schema.Patch_responce)
async def update_recipes(id: int, request_body: recipe_schema.Patch_request, db: Session = Depends(get_db)):
    original = recipe_crud.search_recipe(db, id)
    db_recipe = recipe_crud.update_recipe(db, request_body, original)
    return {"message": "Recipe successfully updated!", "recipe": [db_recipe]}
    return recipe_schema.Patch_responce(message="Recipe successfully updated!", recipe=[recipe_schema.Recipe_simple(**request_body.dict())])


@router.delete("/recipes/{id}", response_model=recipe_schema.Delete_responce)
async def delete_recipes(id: int, db: Session = Depends(get_db)):
    original = recipe_crud.search_recipe(db, id)
    if original is None:
        return {"message": "No Recipe found"}
    recipe_crud.delete_recipe(db, original)
    return {"message": "Recipe successfully removed!"}
    return recipe_schema.Delete_responce(message="Recipe successfully removed!")
