from starlette.responses import JSONResponse
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from components.roles import schemas
from components.roles import crud
from db import get_db
from configparser import ConfigParser

configP = ConfigParser()
configP.read('messages.ini')


role_router = APIRouter(
    prefix='/role',
    tags=['role']
)


@role_router.get("/features/{id}", response_model=schemas.RoleFeatures)  # если правильное id - error500
def get_features(role_id: int, db: Session = Depends(get_db)):
    db_features = crud.get_role_by_id(db=db, role_id=role_id)
    if not db_features:
        raise HTTPException(status_code=404, detail=configP.get('roles', 'role_not_found'))
    else:
        return db_features


@role_router.get("/{id}", response_model=schemas.Role)
def current_role(role_id: int, db: Session = Depends(get_db)):
    crud.get_role_by_id(db=db, role_id=role_id)
    return JSONResponse(status_code=200, content=configP.get('roles', 'role_found_success'))


@role_router.put("/create", response_model=schemas.Role)
def current_role_add(role: schemas.Role, db: Session = Depends(get_db)):
    return crud.create_user_role(db=db, role=role)


@role_router.put("/update", response_model=schemas.RoleUpdate)
def update_description_role_via_id(update_role: schemas.RoleUpdate, role_id: int, db: Session = Depends(get_db)):
    crud.update_role(db=db, role_id=role_id, update_role=update_role)
    return JSONResponse(status_code=200, content=configP.get('roles', 'role_updated_success'))


@role_router.delete("/delete")
def delete_user_via_id(role_id: int, db: Session = Depends(get_db)):
    crud.delete_role(db=db, role_id=role_id)
    return JSONResponse(status_code=200, content=configP.get('roles', 'role_deleted'))



