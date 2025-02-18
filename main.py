from fastapi import FastAPI # type: ignore
from typing import Optional
from pydantic import BaseModel # type: ignore
app = FastAPI()

@app.get('/')                      # this is a decorator (@app.get('/')  ('/')- this is known as path , get in (@app.get('/')) is known as operation, the @app in (@app.get('/')) is known path operation decorator and under this decorator (@app.get('/') the fucntion def index() is known as path operation function)
def index():
    return {'data': {'name': 'ammar'}}


@app.get('/blogs')
def getblobs():
    return {'data': 'list of blobs'}

@app.get('/blogs/unpublished')
def getunpublished():
    return {'data': 'list of unpublished blobs'}

@app.get('/blogs/{id}')    ## this {id} is a path parameter
def getblobsid(id: int):  ## this will convert it into string. this happends throufh pyndit
    return {'data': id}

# @app.get('/blogs/unpublished')   ## this function at this position will throw an error because fast api will check the the line one by one from above for executing which apis based on then entered query. In this request requste was '/blogs/unpublished' so it will start from above it will see first / then /blogs then blogs/{id} at this stage /blogs/unpublished would exexute blogs/{id} cuz it would thing unpublished is a paramter for {id} so handling for such cases always placed your apis according so this could be prevented
# def getunpublished():
#     return {'data': 'list of unpublished blobs'}

@app.get('/blogs/{id}/comments')    ## this {id} is a path parameter
def getblobsidcomments(id: int):
    return {'data': { id: ['1','2','3','4']}}


@app.get('/items')  ## for query parameter we cant hardocde it it will not change our query like (@app.get('/items?limit=10')) - we will add query paramter in functon
def getblobs(limit =10,published: bool =True, sort: Optional[str] = None): ## here limit=10 means if no query paramter is provided then defaultwill be 10 and published: bool means the value will converted to bool for if statements as string could not be used for comparision
    if published:
        return {'data': f'{limit} of published items'}      ## in the above the sort will be an optional paramter. by default it will be none but user could use it in query 
    else:
        return {'data': f'{limit} of unpublished items'}
    

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def createblog(request: Blog):
    return {'data': f'new item created with title as {request.title}'}


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1",port=9000)

