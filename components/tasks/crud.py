from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from components.tasks import models
from components.tasks import schemas


def create_task(db: Session, task: schemas.Task):
    db_task = models.Task(
        name=task.name,
        description=task.description,
        idProject=task.idProject
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_task_list(db: Session):
    db_task = db.query(models.Task).all()
    return db_task


def get_task_by_id(task_id: int, db: Session):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    return db_task


def get_update_task(db: Session, task_id: int, update_task: schemas.TaskUpdate):
    db_task = get_task_by_id(task_id, db=db)
    db_task.name = update_task.name
    db_task.description = update_task.description
    db.commit()
    db.refresh(db_task)
    return db_task


def delete_task(task_id: int, db: Session):
    db_task = get_task_by_id(task_id, db=db)
    db.delete(db_task)
    db.commit()
    return db_task


