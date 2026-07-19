from fastapi import FastAPI
from router import get_blog

app = FastAPI()
app.include_router(get_blog.router)

@app.get("/")
def index():
  return "Hello World!!!!"
