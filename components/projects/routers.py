from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from components.projects import schemas
from components.projects import crud
from db import get_db

project_router = APIRouter(
    prefix='/project',
    tags=['project']
)


@project_router.get("/list")
def project_list(db: Session = Depends(get_db)):
    return crud.get_project_list(db=db)


@project_router.get("/field/{id}", response_model=schemas.Project)
def project_field_by_id(project_id: int, db: Session = Depends(get_db)):
    return crud.get_project_by_id(project_id=project_id, db=db)


@project_router.get("/project/user/{id}", response_model=list[schemas.UserFromProject])
def project_user_by_id(project_id: int, db: Session = Depends(get_db)):
    return crud.get_user_by_id(project_id=project_id, db=db)


@project_router.put("/project/create")
def project_create(project: schemas.Project, db: Session = Depends(get_db)):
    return crud.create_project(db=db, project=project)


@project_router.put("/project/update", response_model=schemas.ProjectUpdate)
def project_user_by_id_project(project_id: int, update_project: schemas.ProjectUpdate, db: Session = Depends(get_db)):
    db_update = crud.get_project_by_id(db=db, project_id=project_id)
    if not db_update:
        raise HTTPException(status_code=404, detail='project_not_found')
    else:
        return crud.get_update_project_blocks(db=db, project_id=project_id, update_project=update_project)
