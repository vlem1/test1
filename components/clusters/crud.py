from sqlalchemy.orm import Session
from components.clusters import models
from components.clusters import schemas
from components.clusters import models as cluster_models


def create_cluster(cluster: schemas.Cluster, db: Session):
    db_cluster = models.Cluster(
        name=cluster.name
    )
    db.add(db_cluster)
    db.commit()
    db.refresh(db_cluster)
    return db_cluster


def get_cluster_by_id(cluster_id: int, db: Session):
    db_cluster = db.query(models.Cluster).filter(models.Cluster.id == cluster_id).first()
    return db_cluster


def get_cluster_list(db: Session):
    db_user = db.query(models.Cluster).all()
    return db_user


def delete_cluster(cluster_id: int, db: Session):
    db_cluster = get_cluster_by_id(cluster_id, db=db)
    db.delete(db_cluster)
    db.commit()
    return db_cluster





