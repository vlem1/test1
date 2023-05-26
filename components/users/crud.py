from select import select

from sqlalchemy.orm import Session
from sqlalchemy import or_
from components.users import models
from components.users import schemas
from components.roles import models as roles_models
from components.clusters import models as cluster_models
from components.projects import models as project_models
from components.tasks import models as task_models


def get_user_role_by_id(user_id: int, db: Session):
    role_db = db.query(
        models.User.idRole,
        roles_models.Role.name,
        roles_models.Role.description
    ). \
        filter(models.User.id == user_id). \
        join(roles_models.Role, roles_models.Role.id == models.User.idRole).first()
    return role_db


def get_user_cluster_by_id(user_id: int, db: Session):
    cluster_db = db.query(
        models.User.idRole,
        cluster_models.Cluster.name,
    ). \
        filter(models.User.id == user_id). \
        join(cluster_models.Cluster, cluster_models.Cluster.id == models.User.idCluster).first()
    return cluster_db


def get_user_projects_by_id(db: Session, user_id: int):
    projects_db = db.query(
        models.User.idRole,
        project_models.Project.name,
        project_models.Project.description,
        project_models.Project.idAutor,
    ). \
        filter(models.User.id == user_id). \
        join(project_models.Project, project_models.Project.idAutor == models.User.id).all()
    return projects_db


def get_user_tasks_by_id(db: Session, user_id: int):
    task_db = db.query(
        task_models.Task
    ).filter(project_models.Project.idAutor == user_id) \
        .filter(task_models.Task.idProject == project_models.Project.id).all()
    return task_db


def get_user_by_id(user_id: int, db: Session):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    return db_user


def update_user(user_id: int, db: Session, updated_user: schemas.UserUpdate):
    db_user = get_user_by_id(user_id, db=db)
    db_user.name = updated_user.name
    db_user.surname = updated_user.surname
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(user_id: int, db: Session):
    db_user = get_user_by_id(user_id, db=db)
    db.delete(db_user)
    db.commit()
    return db_user


def create_user(user: schemas.AddNewUser, db: Session):
    db_user = models.User(
        name=user.name,
        surname=user.surname,
        idRole=user.idRole,
        position=user.position,
        login=user.login,
        passwordHash=user.passwordHash,
        idCluster=user.idCluster,
        markingDeletion=user.markingDeletion
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_letter(user_let: str, db: Session):
    db_user = db.query(models.User)\
        .filter(or_(models.User.name.contains(user_let), models.User.surname.contains(user_let))).all()
    return db_user

