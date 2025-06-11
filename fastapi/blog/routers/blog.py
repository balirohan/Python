from fastapi import APIRouter, Depends, status, HTTPException, Response

import schemas, models
from database import get_db
from sqlalchemy.orm import Session
import helper.blog
from oauth2 import get_current_user

router = APIRouter(prefix='/blog', tags=['Blogs'])

@router.get('/', response_model=list[schemas.ShowBlog])
def get_all_blogs(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return helper.blog.get_all(db)
    

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return helper.blog.create(request, db)

@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def get_blog(id: int, response: Response, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return helper.blog.get(id, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return helper.blog.destroy(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return helper.blog.update(id, request, db)