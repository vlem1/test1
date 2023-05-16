from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from components.clusters import schemas
from components.clusters import crud
from db import get_db
from fastapi import Query


cluster_router = APIRouter(
    prefix='/cluster',
    tags=['cluster']
)


@cluster_router.get("/cluster/{id}", response_model=schemas.Cluster)
def current_cluster(cluster_id: int, db: Session = Depends(get_db)):
    return crud.get_cluster_by_id(db=db, cluster_id=cluster_id)


@cluster_router.get("/list")
def current_cluster(db: Session = Depends(get_db)):
    return crud.get_cluster_list(db=db)


@cluster_router.put("/cluster/create")
def cluster_add(cluster: schemas.Cluster, db: Session = Depends(get_db)):
    return crud.create_cluster(db=db, cluster=cluster)








