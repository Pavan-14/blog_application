from fastapi import FastAPI, status
from blog import models
from blog.database import engine
from blog.routers import blog,user,authentication


models.Base.metadata.create_all(engine)

app = FastAPI()

# registoring the routers
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)


# default route
@app.get('/', status_code=status.HTTP_200_OK)
def show_list():
    return {'details':'list of items'}
    
# the below functions are created for testing purpose. 
'''
@app.get('/blog')
def show_all_blogs(limit: int, published: bool = True, sort: Optional[str] = None):
    """
    show_all_blogs shows the blogs deatils
    Arguments:
        limit: requied argument type integer
        published: default argument type bool
        sort: optional argument as string
    they are called as Query parameters
    """
    if published:
        return {'details':f'{limit} published blog details'}
    else:
        return {'details':f'{limit} blog details'}

@app.get('/blog/unpublished')
def unpublished():
    return {'details':'unpublished blogs'}
'''