from starlette.responses import JSONResponse
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from components.tasks import schemas
from components.tasks import crud
from db import get_db
from configparser import ConfigParser

configP = ConfigParser()
configP.read('messages.ini')

task_router = APIRouter(
    prefix='/task',
    tags=['task']
)


@task_router.get("/list")
def task_list(db: Session = Depends(get_db)):
    return crud.get_task_list(db=db)


@task_router.get("/{id}", response_model=schemas.Task)
def task_by_id(task_id: int, db: Session = Depends(get_db)):
    crud.get_task_by_id(task_id=task_id, db=db)
    return JSONResponse(status_code=200, content=configP.get('tasks', 'task_found_success'))


@task_router.put("/create")
def task_create(task: schemas.Task, db: Session = Depends(get_db)):
    return crud.create_task(db=db, task=task)


@task_router.put("/update", response_model=schemas.TaskUpdate)
def task_id_update(update_task: schemas.TaskUpdate, task_id: int, db: Session = Depends(get_db)):
    db_update = crud.get_task_by_id(db=db, task_id=task_id)
    if not db_update:
        raise HTTPException(status_code=404, detail=configP.get('tasks', 'task_not_found'))
    else:
        crud.get_update_task(db=db, task_id=task_id, update_task=update_task)
        return JSONResponse(status_code=200, content=configP.get('tasks', 'task_updated'))


@task_router.delete("/delete")
def delete_project_via_id(task_id: int, db: Session = Depends(get_db)):
    crud.delete_task(db=db, task_id=task_id)
    return JSONResponse(status_code=200, content=configP.get('tasks', 'task_deleted'))