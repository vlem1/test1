from sqlalchemy.orm import Session
from components.roles import models
from components.roles import schemas


def get_role_by_id(role_id: int, db: Session):
    db_role = db.query(models.Role).filter(models.Role.id == role_id).first()
    return db_role


def update_role(role_id: int, db: Session, update_role: schemas.RoleUpdate):
    db_role = get_role_by_id(role_id, db=db)
    db_role.name = update_role.name
    db_role.description = update_role.description
    db.commit()
    db.refresh(db_role)
    return db_role


def delete_role(role_id: int, db: Session):
    db_role = get_role_by_id(role_id, db=db)
    db.delete(db_role)
    db.commit()
    return db_role


def create_user_role(role: schemas.Role, db: Session):
    db_role = models.Role(
        name=role.name,
        description=role.description
    )
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

