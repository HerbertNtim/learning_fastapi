from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get("/")
def index() :
  return "Hello World!!!!"

# @app.get('/blog/all')
# def get_all_blog():
#   return "Getting all blogs"

@app.get('/blog/all')
def get_blogs(page=1, page_size=10):
  return {"message": f'All {page_size} blogs can be found on {page}'}

class BlogType(str, Enum):
  short = 'short'
  story = 'story'
  howto = 'howto'
  
@app.get('/blog/type/{type}')
def get_blog_type(type: BlogType):
  return {'message': f'This is a Blog type of {type}'}

@app.get("/blog/{id}")
def get_blog(id: int):
  return {"message": f"Blog with the id {id}"}

