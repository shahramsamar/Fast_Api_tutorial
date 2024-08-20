from typing import Optional
from fastapi import FastAPI, status, HTTPException, Query,Path
from fastapi.responses import JSONResponse
import random

app = FastAPI()

names_db = [
    {
        "id": 1,
        "name": "ali"
    },
    {
        "id": 2,
        "name": "maryam"
    },
    {
        "id": 3,
        "name": "arousha"
    },
]

# GET  /names List
# GET /names/<id> Detail
# POST /names Create
# PUT/PATCH  /names/<id> Update
# DELETE /names/<id> DELETE
# /names  GET POST
# /names/<id> GET PUT/PATCH DELETE



#search: Optional[str]=None 

@app.get("/names")
async def names_list(search: Optional[str]=Query(None, max_length=20,description="names")):
    result = names_db
    if search:
        result =[ item for item in names_db if search.lower() == item['name'].lower() ]
    return JSONResponse(result, status_code=status.HTTP_200_OK)


@app.get("/names/{item_id}")
async def names_detail(item_id:int = Path(description="detail")):
    for name in names_db:
        if  name["id"] == item_id: 
         return JSONResponse(name, status_code=status.HTTP_200_OK)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="item not fund")



@app.post('/names')
async def names_create(name:str):
    new_name = {'id':random.randint(4,10),"name":name}
    names_db.append(new_name)
    return JSONResponse(names_db, status_code=status.HTTP_201_CREATED)


@app.put("/names/{item_id}")
async def names_update(item_id:int, name:str):
    for item in names_db:
        if  item["id"] == item_id:
            item['name'] = name
            # return item
    raise HTTPException(item,status_code=status.HTTP_404_NOT_FOUND,detail="item not fund")   


@app.delete("/names/{item_id}")
async def names_delete(item_id:int):
    for index, item in enumerate(names_db):
        if  item["id"] == item_id:
            del names_db[index]
            return {"delete":"item removed successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="item not fund")   
