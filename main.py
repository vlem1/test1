import uvicorn
from fastapi import FastAPI
from db import engine, Base
from components.users.routers import user_router
from components.roles.routers import role_router


Base.metadata.create_all(bind=engine)
app = FastAPI()


app.include_router(user_router)
app.include_router(role_router)


if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)
