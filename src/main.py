from fastapi import FastAPI
from api.routes import router as battery_router

app = FastAPI()
app.include_router(
    battery_router,
    prefix="/battery",
    tags=['Battery']
)