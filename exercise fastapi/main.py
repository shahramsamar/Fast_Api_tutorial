from fastapi import FastAPI, Query
from typing import Optional

apps = FastAPI()


post_list = [
    {
    "id": "id",
    "name":"name"
    }
]



@apps.get('/')
async def show_post():
    return post_list


@apps.post('post')
async def post_create(post_id: Optional['int']Query(None, max_length=2 ,title='Enter a number'),
                      post_name:Optional['in'] Query(str,title="Enter a name "))

    post_id.a