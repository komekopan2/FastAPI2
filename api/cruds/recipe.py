from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import select
from sqlalchemy.engine.result import Result
import api.models.recipe as recipe_model
import api.schemas.recipe as recipe_schema


def init_db_data(db: Session, data_init: recipe_schema.Initialize_post_request):
    original = recipe_model.Recipe(**data_init.dict())
    db.add(original)
    db.commit()
    db.refresh(original)
    return original


def create_recipe(db: Session, recipe_create: recipe_schema.Post_request):
    original = recipe_model.Recipe(**recipe_create.dict())
    db.add(original)
    db.commit()
    db.refresh(original)
    return original


def getall_recipe(db: Session):
    return db.query(recipe_model.Recipe).all()


def getid_recipe(db: Session, id: int):
    return db.query(recipe_model.Recipe).filter(recipe_model.Recipe.id == id).first()


def search_recipe(db: Session, id: int):
    result: Result = db.execute(
        select(recipe_model.Recipe).filter(recipe_model.Recipe.id == id))
    return result.scalars().first()


def update_recipe(db: Session, recipe_update: recipe_schema.Patch_request, original: recipe_model.Recipe):
    original.title = recipe_update.title
    original.making_time = recipe_update.making_time
    original.serves = recipe_update.serves
    original.ingredients = recipe_update.ingredients
    original.cost = recipe_update.cost
    db.add(original)
    db.commit()
    db.refresh(original)
    return original


def delete_recipe(db: Session, original: recipe_model.Recipe):
    db.delete(original)
    db.commit()
