from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

import schemas, models, hashing
from database import get_db

def create(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(name=request.name, email=request.email, password=hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show_all(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

def show(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} not found.')
    return user