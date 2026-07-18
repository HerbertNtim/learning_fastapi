from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index() :
  return "Hello World!!!!"

@app.get('/blog/all')
def get_all_blog():
  return "Getting all blogs"

@app.get("/blog/{id}")
def get_blog(id: int):
  return {"message": f"Blog with the id {id}"}

