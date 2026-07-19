from fastapi import APIRouter, status, Response
from enum import Enum
from typing import Optional


router = APIRouter(
  prefix='/blog',
  tags=['blog']
)

@router.get('/all', summary='This API gets all blogs', description='Getting all blogs from the data base')
def get_blogs(page=1, page_size=10):
  return {"message": f'All {page_size} blogs can be found on {page}'}


@router.get('/{id}/comments/{comment_id}', tags=['comment'])
def get_comments(comment_id: int, valid: bool=True, username: Optional[str]=None):
  """
  Getting comments based on 

  - **blog id** Mandatory parameter for getting the id
  - **comment id** Mandatory parameter for getting the comment 
  - **valid** Optional parameter for getting the comment 
  - **username** Optional parameter for getting the comment 
  """
  return {"message": f"Blog ID {id}, Comment ID {comment_id}, valid {valid}, username {username}"}


class BlogType(str, Enum):
  short = 'short'
  story = 'story'
  howto = 'howto'


@router.get('/type/{blog_type}')
def get_blog_type(blog_type: BlogType):
  return {'message': f'This is a Blog type of {blog_type}'}


@router.get("/{id}", status_code=status.HTTP_200_OK, response_description='Found blog based on id')
def get_blog(blog_id: int, response:Response):
  if blog_id > 5:
    response.status_code = status.HTTP_404_NOT_FOUND
    return {'error': f"Blog with {blog_id} not found"}
  else:
    response.status_code = status.HTTP_200_OK
    return {"message": f"Blog with the id {blog_id} found"}


