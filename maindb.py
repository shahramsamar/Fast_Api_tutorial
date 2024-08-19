from fastapi import FastAPI
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




@app.get("/names")
async def names_list():
    return names_db


@app.get("/names/{item_id}")
async def names_detail(item_id:int):
    for name in names_db:
        if  name["id"] == item_id:
            return name
    return {"detail":"item not fund"}    

# @app.get("/names")
# async def names_list():
#     return names_db


# @app.post("/names")
# async def names_create(name: str):
#     new_name = {"id": random.randint(100, 1000), "name": name}
#     names_db.append(new_name)
#     return new_name


# @app.get("/names/{item_id}")
# async def names_detail(item_id: int):
#     for name in names_db:
#         if name["id"] == item_id:
#             return name

#     return {"detail": "item not found"}


# @app.put("/names/{item_id}")
# async def names_update(item_id: int, name: str):
#     for item in names_db:
#         if item["id"] == item_id:
#             item["name"] = name
#             return item

#     return {"detail": "item not found"}


# @app.delete("/names/{item_id}")
# async def names_delete(item_id: int):
#     for index, item in enumerate(names_db):
#         if item["id"] == item_id:
#             del names_db[index]
#             return {"detail": "item removed successfully"}

#     return {"detail": "item not found"}

