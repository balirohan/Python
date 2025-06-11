from fastapi import APIRouter, Depends, status, HTTPException, Response

import schemas, models
from database import get_db
from sqlalchemy.orm import Session
import helper.user

router = APIRouter(prefix='/user', tags=['Users'])

@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return helper.user.create(request, db)

@router.get('/', response_model=list[schemas.ShowUser])
def show_users(db: Session = Depends(get_db)):
    return helper.user.show_all(db)

@router.get('/{id}', response_model=schemas.ShowUser)
def show_user(id: int, db: Session = Depends(get_db)):
    return helper.user.show(id, db)