from fastapi import FastAPI
app = FastAPI()

@app.get('/')
async def root():
    return {"message":'Hello World!'}


# two way run
# import uvicorn

# two way run
# if __name__ == "__main__":
#     uvicorn.run ('main.py',port=8000, log_level='info')   


# sample structure code 
# @app.<method_name>('<url_path')
# async_or_not def function_name(<request>,<args>):
#     return <request>

# structure map
# path
# method
# response
# body
