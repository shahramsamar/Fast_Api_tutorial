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

#@app.<method name>("<url_path>")
#async_or_not def function_name(<request>,<args>):
#    return <response>



# query parameter with ? mark in end of parameter
# path  parameter with slug in inti in address

# structure
# request: path, query
# body: urlencode, paintext
# method 
# response


# example to use 
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


@app.post('/names')
async def names_create(name:str):
    new_name = {'id':random.randint(4,10),"name":name}
    names_db.append(new_name)
    return new_name


@app.put("/names/{item_id}")
async def names_update(item_id:int, name:str):
    for item in names_db:
        if  item["id"] == item_id:
            item['name'] = name
            return item
    return {"detail":"item not fund"}    


@app.delete("/names/{item_id}")
async def names_delete(item_id:int):
    for index, item in enumerate(names_db):
        if  item["id"] == item_id:
            del names_db[index]
            return {"delete":"item removed successfully"}
    return {"detail":"item not fund"}    
