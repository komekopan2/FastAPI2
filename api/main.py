from fastapi import FastAPI

from api.routers import recipe

app = FastAPI()
app.include_router(recipe.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
