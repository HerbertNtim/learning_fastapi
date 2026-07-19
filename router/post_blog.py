from fastapi import APIRouter

router = APIRouter(
  prefix='/blog',
  tags=['blog']
)

@router.post('/new')
def post_blog():
  pass
