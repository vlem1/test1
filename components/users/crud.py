from sqlalchemy.orm import Session
from components.users import models
from components.users import schemas


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
    db.refresh(db_user)
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
