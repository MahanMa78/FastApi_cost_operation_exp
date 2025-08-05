from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.responses import JSONResponse


@asynccontextmanager
async def lifespan(app:FastAPI):
    print("Application startup")
    yield
    print("Application shutdown")


app = FastAPI(lifespan=lifespan)

custom_list = [
    {"id" : 1 , "amount" : 100 , "description" : "for sport"},
    {"id" : 2 , "amount" : 150 , "description" : "for lunch"},
    
]




@app.get("/items/")
async def read_items():
    return JSONResponse(content=custom_list)


