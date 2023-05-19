import uvicorn
from fastapi import FastAPI
from db import engine, Base
from components.users.routers import user_router
from components.roles.routers import role_router
from components.clusters.routers import cluster_router
from components.projects.routers import project_router
from components.tasks.routers import task_router
from config import *


Base.metadata.create_all(bind=engine)
app = FastAPI()


app.include_router(user_router)
app.include_router(role_router)
app.include_router(cluster_router)
app.include_router(project_router)
app.include_router(task_router)

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)
