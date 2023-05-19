from starlette.responses import JSONResponse
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from components.projects import schemas
from components.projects import crud
from db import get_db
from configparser import ConfigParser

configP = ConfigParser()
configP.read('messages.ini')

project_router = APIRouter(
    prefix='/project',
    tags=['project']
)


@project_router.get("/list")
def project_list(db: Session = Depends(get_db)):
    return crud.get_project_list(db=db)


@project_router.get("/{id}", response_model=schemas.Project)
def project_field_by_id(project_id: int, db: Session = Depends(get_db)):
    crud.get_project_by_id(project_id=project_id, db=db)
    return JSONResponse(status_code=200, content=configP.get('projects', 'project_found_success'))


@project_router.get("/user/{id}", response_model=list[schemas.UserFromProject])
def project_user_by_id(project_id: int, db: Session = Depends(get_db)):
    crud.get_user_by_id(project_id=project_id, db=db)
    return JSONResponse(status_code=200, content=configP.get('projects', 'user_id_found_success'))


@project_router.put("/create")
def project_create(project: schemas.Project, db: Session = Depends(get_db)):
    return crud.create_project(db=db, project=project)


@project_router.put("/update", response_model=schemas.ProjectUpdate)
def project_user_by_id_project(project_id: int, update_project: schemas.ProjectUpdate, db: Session = Depends(get_db)):
    db_update = crud.get_project_by_id(db=db, project_id=project_id)
    if not db_update:
        raise HTTPException(status_code=404, detail=configP.get('projects', 'project_not_found'))
    else:
        crud.get_update_project_blocks(db=db, project_id=project_id, update_project=update_project)
        return JSONResponse(status_code=200, content=configP.get('projects', 'project_updated'))


@project_router.delete("/delete")
def delete_project_via_id(project_id: int, db: Session = Depends(get_db)):
    crud.delete_project(db=db, project_id=project_id)
    return JSONResponse(status_code=200, content=configP.get('projects', 'projects_deleted'))

