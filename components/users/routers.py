from starlette.responses import JSONResponse
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from components.users import schemas
from components.users import crud
from db import get_db
from configparser import ConfigParser

configP = ConfigParser()
configP.read('messages.ini')

user_router = APIRouter(
    prefix='/user',
    tags=['user']
)


@user_router.get("/{id}/idRole", response_model=schemas.ValuesFromIdRole)
def current_user(user_id: int, db: Session = Depends(get_db)):
    crud.get_user_role_by_id(db=db, user_id=user_id)
    return JSONResponse(status_code=200, content=configP.get('users', 'user_found_success'))


@user_router.get("/{id}/idCLuster", response_model=schemas.ValuesFromIdCluster)
def current_user(user_id: int, db: Session = Depends(get_db)):
    crud.get_user_cluster_by_id(db=db, user_id=user_id)
    return JSONResponse(status_code=200, content=configP.get('users', 'user_found_success'))


@user_router.get("/{id}/projects", response_model=list[schemas.ValuesFromProjects])
def current_user(user_id: int, db: Session = Depends(get_db)):
    crud.get_user_tasks_by_id(db=db, user_id=user_id)
    return JSONResponse(status_code=200, content=configP.get('users', 'user_found_success'))


@user_router.get("/{id}/tasks", response_model=list[schemas.ValuesFromTasks])
def current_user(user_id: int, db: Session = Depends(get_db)):
    crud.get_user_tasks_by_id(db=db, user_id=user_id)
    return JSONResponse(status_code=200, content=configP.get('users', 'user_found_success'))


@user_router.get("/features/{id}", response_model=schemas.UserFeatures)
def get_features(user_id: int, db: Session = Depends(get_db)):
    db_features = crud.get_user_by_id(db=db, user_id=user_id)
    if not db_features:
        raise HTTPException(status_code=404, detail=configP.get('users', 'user_not_found'))
    else:
        return db_features


@user_router.get("/{id}", response_model=schemas.User)
def current_user(user_id: int, db: Session = Depends(get_db)):
    crud.get_user_by_id(db=db, user_id=user_id)
    return JSONResponse(status_code=200, content=configP.get('users', 'user_found_success'))


@user_router.get("/letters/search/user", response_model=list[schemas.User])
def current_user(user_let: str, db: Session = Depends(get_db)):
    return crud.get_user_by_letter(db=db, user_let=user_let)
    # return JSONResponse(status_code=200, content=configP.get('users', 'user_found_success'))


@user_router.put("/create")
def current_user_add(user: schemas.AddNewUser, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


@user_router.put("/update", response_model=schemas.UserUpdate)
def update_description_user_via_id(update_user: schemas.UserUpdate, user_id: int, db: Session = Depends(get_db)):
    crud.update_user(db=db, user_id=user_id, updated_user=update_user)
    return JSONResponse(status_code=200, content=configP.get('users', 'user_update_success'))


@user_router.delete("/delete")
def delete_user_via_id(user_id: int, db: Session = Depends(get_db)):
    crud.delete_user(db=db, user_id=user_id)
    return JSONResponse(status_code=200, content=configP.get('users', 'user_deleted'))

