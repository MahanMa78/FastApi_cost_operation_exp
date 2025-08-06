from fastapi import FastAPI , Path , status , HTTPException , Body
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


@app.get("/items/{item_id}")
def read_item(item_id: int ):
    for item in custom_list:
        if item["id"] == item_id: 
            return item
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="object not found")


@app.post("/items/" , status_code=status.HTTP_201_CREATED)
def create_item(description:str = Body(embed=True)  , amount:int = Body(embed=True)):
    item_obj = {"id" : len(custom_list) + 1 , "description" : description, "amount" : amount}
    custom_list.append(item_obj)
    
    return item_obj


@app.put("/items/{item_id}" , status_code=status.HTTP_200_OK)
def update_item(item_id:int = Path() , description:str = Body(embed=True) , amount:int = Body(embed=True)):
    for item in custom_list:
        if item["id"] == item_id:
            item['description'] = description
            item['amount'] = amount
            return item
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="object not found")



