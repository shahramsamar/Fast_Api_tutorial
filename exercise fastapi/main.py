from fastapi import FastAPI, Query, status, Path
from typing import Optional
from fastapi.responses import JSONResponse
import random



apps = FastAPI()

post_list = [
    {
        "id": 1,
        "title": "post1",
        "description": "post1 description",
        "is_published": False,
    },
    {
        "id": 2,
        "title": "post2",
        "description": "post2 description",
        "is_published": True,
    },
    {
        "id": 3,
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
        result = [item for item in post_list if post_id == item['id']]
    if title :
        result = [item for item in result if title.lower() == item['title'].lower()]
    if description :
        result = [item for item in result if description.lower() == item['description'].lower()]
    if is_published :
        result = [item for item in result if item['is_published'] == is_published]            
    
    if result:                       
        return JSONResponse(result,status_code=status.HTTP_200_OK)
    else:
         return JSONResponse({"message":f"We don't have any id={id}, title={title}, description={description}, is_published={is_published}"},status_code=status.HTTP_404_NOT_FOUND)                



@apps.post('/create/')
async def post_create(post_name: Optional[str] = Query(None,max_length=50,  description='this is a create post to post_name'),
                      description: Optional[str] = Query(None, max_length=150,  description='this is a create post to description')):
       if post_name and description: 
            post = {"id":random.randint(4,10),"name":post_name,"description":description,"is_published":False}
            post_list.append(post)              
            return JSONResponse(post, status_code=status.HTTP_201_CREATED)
            
       return JSONResponse({"message":"We don't create  any post"},status_code=status.HTTP_400_BAD_REQUEST)                


@apps.put("/update/{post_id}") 
async def post_update(post_id: int,
                      title: str,
                      description: str,
                      is_published: bool):
    for item in post_list:
        if item['id'] == post_id:
            item['title'] = title
            item['description'] = description
            item['is_published'] = is_published
        return JSONResponse(item, status_code=status.HTTP_301_MOVED_PERMANENTLY)       
    return JSONResponse({"message": "Post not found"}, status_code=status.HTTP_404_NOT_FOUND)   