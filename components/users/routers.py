from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from components.users import schemas
from components.users import crud
from db import get_db

user_router = APIRouter(
    prefix='/user',
    tags=['user']
)


@user_router.get("/user/{id}/idRole", response_model=schemas.ValuesFromIdRole)
def current_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user_role_by_id(db=db, user_id=user_id)


@user_router.get("/user/{id}/idCLuster", response_model=schemas.ValuesFromIdCluster)
def current_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user_cluster_by_id(db=db, user_id=user_id)


@user_router.get("/user/{id}/projects", response_model=list[schemas.ValuesFromProjects])
def current_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user_projects_by_id(db=db, user_id=user_id)


@user_router.get("/features/{id}", response_model=schemas.UserFeatures)
def get_features(user_id: int, db: Session = Depends(get_db)):
    db_features = crud.get_user_by_id(db=db, user_id=user_id)
    if not db_features:
        raise HTTPException(status_code=404, detail='user_not_found')
    else:
        return db_features


@user_router.get("/user/{id}", response_model=schemas.User)
def current_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user_by_id(db=db, user_id=user_id)


@user_router.put("/user/create")
def current_user_add(user: schemas.AddNewUser, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


@user_router.put("/user/update", response_model=schemas.UserUpdate)
def update_description_user_via_id(update_user: schemas.UserUpdate, user_id: int, db: Session = Depends(get_db)):
    return crud.update_user(db=db, user_id=user_id, updated_user=update_user)


@user_router.delete("/user/delete")
def delete_user_via_id(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_user(db=db, user_id=user_id)

