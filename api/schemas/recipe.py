from pydantic import BaseModel
from datetime import datetime


class Recipe_simple(BaseModel):
    title: str
    making_time: str
    serves: str
    ingredients: str
    cost: int


class Recipe_id(Recipe_simple):
    id: int


class Recipe_id_create_update(Recipe_id):
    created_at: datetime
    updated_at: datetime


class Initialize_post_request((Recipe_id_create_update)):
    pass


class Post_request(Recipe_simple):
    pass


class Post_responce(BaseModel):
    message: str
    recipe: list[Recipe_id_create_update]

    class Config:
        orm_mode = True


class Getall_responce(BaseModel):
    recipes: list[Recipe_id]

    class Config:
        orm_mode = True


class Getid_responce(BaseModel):
    message: str
    recipe: list[Recipe_id]

    class Config:
        orm_mode = True


class Patch_request(Recipe_simple):
    pass


class Patch_responce(BaseModel):
    message: str
    recipe: list[Recipe_simple]

    class Config:
        orm_mode = True


class Delete_responce(BaseModel):
    message: str

    class Config:
        orm_mode = True
