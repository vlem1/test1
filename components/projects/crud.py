from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from components.projects import models
from components.projects import schemas
from components.users import models as users_models


def create_project(db: Session, project: schemas.Project):
    db_project = models.Project(
        name=project.name,
        description=project.description,
        idAutor=project.idAutor
    )
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


def get_project_list(db: Session):
    db_project = db.query(models.Project).all()
    return db_project


def get_project_by_id(project_id: int, db: Session):
    db_project = db.query(models.Project).filter(models.Project.id == project_id).first()
    return db_project


def get_user_by_id(project_id: int, db: Session):
    project_db = db.query(
        models.Project.idAutor,
        users_models.User.name,
        users_models.User.surname,
        users_models.User.idRole,
        users_models.User.position,
        users_models.User.login,
        users_models.User.passwordHash,
        users_models.User.idCluster,
        users_models.User.markingDeletion,
                        ). \
        filter(models.Project.id == project_id). \
        join(users_models.User, users_models.User.id == models.Project.idAutor).first()
    return project_db


def get_update_project_blocks(db: Session, project_id: int, update_project: schemas.ProjectUpdate):
    db_project = get_project_by_id(project_id, db=db)
    db_user_exist = get_user_by_id(db=db, project_id=update_project.idAutor)
    if not db_user_exist:
        raise HTTPException(status_code=404, detail='user_with_correct_id_not_exist')
    else:
        db_project.name = update_project.name
        db_project.idAutor = update_project.idAutor
        db.commit()
        db.refresh(db_project)
        return db_project


