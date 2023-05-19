from starlette.responses import JSONResponse
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from components.clusters import schemas
from components.clusters import crud
from db import get_db
from configparser import ConfigParser

configP = ConfigParser()
configP.read('messages.ini')

cluster_router = APIRouter(
    prefix='/cluster',
    tags=['cluster']
)


@cluster_router.get("/{id}", response_model=schemas.Cluster)
def current_cluster(cluster_id: int, db: Session = Depends(get_db)):
    crud.get_cluster_by_id(db=db, cluster_id=cluster_id)
    return JSONResponse(status_code=200, content=configP.get('clusters', 'cluster_found_success'))


@cluster_router.get("/list")
def current_cluster(db: Session = Depends(get_db)):
    return crud.get_cluster_list(db=db)


@cluster_router.put("/create")
def cluster_add(cluster: schemas.Cluster, db: Session = Depends(get_db)):
    return crud.create_cluster(db=db, cluster=cluster)


@cluster_router.delete("/delete")
def delete_cluster_via_id(cluster_id: int, db: Session = Depends(get_db)):
    crud.delete_cluster(db=db, cluster_id=cluster_id)
    return JSONResponse(status_code=200, content=configP.get('clusters', 'cluster_deleted'))








