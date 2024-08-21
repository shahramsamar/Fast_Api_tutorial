from fastapi import FastAPI, Query, status, Path
from typing import Optional
from fastapi.responses import JSONResponse
import random



apps = FastAPI()

post_list = [
    {
        "item_id": 1,
        "title": "post1",
        "description": "post1 description",
        "is_published": False,
    },
    {
        "item_id": 2,
        "title": "post2",
        "description": "post2 description",
        "is_published": True,
    },
    {
        "item_id": 3,
        "title": "post3",
        "description": "post3 description",
        "is_published": False,
    }
]



@apps.get('/')
async def show_post():
    # return post_list
    return JSONResponse(post_list)


@apps.get("/search/")
async def search_post(post_id: Optional[int] = Query(None,description='This is a id of the post to search'),
                      title: Optional[str] = Query(None, max_length=50, description='this is a title of the post to search'),
                      description: Optional[str] = Query(None, max_length=150,  description='this is a description of the post to search'),
                      is_published: Optional[bool] = Query(None, description='this is a is_published of the post to search')):
    result = post_list
    if post_id == 0:
                 return JSONResponse({"message":f"we don't have any post"},status_code=status.HTTP_404_NOT_FOUND)                
    if post_id :
        result = [item for item in post_list if post_id == item['item_id']]
    if title :
        result = [item for item in result if title.lower() == item['title'].lower()]
    if description :
        result = [item for item in result if description.lower() == item['description'].lower()]
    if is_published :
        result = [item for item in result if item['is_published'] == is_published]            
    
    if result:                       
        return JSONResponse(result,status_code=status.HTTP_200_OK)
    else:
         return JSONResponse({"message":f"we don't have any post_id={post_id}, title={title}, description={description}, is_published={is_published}"},status_code=status.HTTP_404_NOT_FOUND)                



@apps.post('/name/')
async def post_create(post_name: Optional[str] = Query(None,max_length=50,  description='this is a create post to post_name'),
                      description: Optional[str] = Query(None, max_length=150,  description='this is a create post to description')):
       post = {"id":random.randint(4,10),"name":post_name,"description":description,"is_published":False}
       post_list.append(post)              
       return JSONResponse(post, status_code=status.HTTP_201_CREATED)
    # else:
    #     return JSONResponse({"message":"we don't create  any post"},status_code=status.HTTP_404_NOT_FOUND)                


# @apps.put("/names/{id}") 
# async def post_update(id:int, name:str):
#     for item in post_list:
#         if item['id']==id:
#             item['name'] = name 
#         return JSONResponse(item, status_code=status.HTTP_301_MOVED_PERMANENTLY)       
       