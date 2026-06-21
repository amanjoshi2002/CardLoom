from fastapi import FastAPI
from database import Base, engine
from routes.provider import router as provider_router
from routes.health import router as health_router
app = FastAPI()


#database sqlite 
Base.metadata.create_all(bind=engine)




# routes
app.include_router(provider_router)
app.include_router(health_router)