from fastapi import FastAPI, Query, status, Path, HTTPException
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



@apps.get('/posts')
async def show_post():
    return JSONResponse(post_list)

@apps.get("/posts/{post_id}")
async def search_post(post_id: int = Path(description='This is a id of the post to search')):
    for post in post_list:
        if post["id"] == post_id:
            return JSONResponse(post,
                                status_code=status.HTTP_200_OK)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"We don't have any id={id}")                
    
        


@apps.post('/posts')
async def post_create(title: Optional[str] = Query(None,max_length=50, 
                                                   description='this is a create post to title'),
                      description: Optional[str] = Query(None, max_length=150,
                                                         description='this is a create post to description')):
       if title and description: 
            post = {
                    "id":random.randint(4,10),
                    "title":title,
                    "description":description,
                    "is_published":False
                }
            post_list.append(post)              
            return JSONResponse(post, status_code=status.HTTP_201_CREATED)
       raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                           detail="We don't create  any post")                


@apps.put("/posts/{post_id}") 
async def post_update(post_id: int = Path(description="type your post id to update"),
                      title: Optional[str] = Query(description="type your post title to update", max_length=50),
                      description: Optional[str] = Query(max_length=150, description='type your post description to update'),
                      is_published: Optional[bool] = Query(description='type your post is published to update')):
    for item in post_list:
        if item["id"] == post_id:
            item["title"] = title
            item["description"] = description
            item["is_published"] = is_published
        return JSONResponse(item, 
                            status_code=status.HTTP_200_OK)       
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Post not found")   


@apps.delete("/posts/{post_id}")
async def post_delete(post_id: int = Path(description="type your id to delete")):
    for index, item in enumerate(post_list):
        if item["id"] == post_id:
            del post_list[index]
            return JSONResponse(status_code=status.HTTP_200_OK,detail="Post removed successfully")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Post not found')