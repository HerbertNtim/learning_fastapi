from fastapi import FastAPI, status, Response
from enum import Enum
from typing import Optional

app = FastAPI()

@app.get("/")
def index() :
  return "Hello World!!!!"

# @app.get('/blog/all')
# def get_all_blog():
#   return "Getting all blogs"

@app.get('/blog/all', tags=['blog'])
def get_blogs(page=1, page_size=10):
  return {"message": f'All {page_size} blogs can be found on {page}'}

@app.get('/blog/comments/{comment_id}', tags=['blog', 'comment'])
def get_comments(comment_id: int, valid: bool = True, username: Optional[str] = None):
  return {"message": f"Blog ID {comment_id}, valid {valid}, username {username}"}

class BlogType(str, Enum):
  short = 'short'
  story = 'story'
  howto = 'howto'
  
@app.get('/blog/type/{type}', tags=['blog'])
def get_blog_type(type: BlogType):
  return {'message': f'This is a Blog type of {type}'}

@app.get("/blog/{id}",  status_code=status.HTTP_200_OK, tags=['blog'])
def get_blog(id: int, response:Response):
  if id > 5:
    response.status_code = status.HTTP_404_NOT_FOUND
    return {'error': f"Blog with {id} not found"}
  else:    
    response.status_code = status.HTTP_200_OK
    return {"message": f"Blog with the id {id} found"}

