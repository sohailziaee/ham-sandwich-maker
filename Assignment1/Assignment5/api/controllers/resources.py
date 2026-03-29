from sqlalchemy.orm import Session
from api.models import models
from fastapi import Response

def create(db: Session, obj):
    db_obj = models.Resource(**obj.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def read_all(db: Session):
    return db.query(models.Resource).all()

def read_one(db: Session, obj_id):
    return db.query(models.Resource).filter(models.Resource.id == obj_id).first()

def update(db: Session, obj_id, obj):
    db_obj = db.query(models.Resource).filter(models.Resource.id == obj_id)
    db_obj.update(obj.dict(exclude_unset=True))
    db.commit()
    return db_obj.first()

def delete(db: Session, obj_id):
    db.query(models.Resource).filter(models.Resource.id == obj_id).delete()
    db.commit()
    return Response(status_code=204)