from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.database import engine
from app.database.model import Base
from app.database.weather.model import WeatherTable
from app.iq_air.router import router as iq_air_router
from app.open_meteo.router import router as open_meteo_router
from app.ninjas_geocoding.router import router as ninjas_router
from app.weather_history.router import router as weather_history_router

app = FastAPI(
    title="Air condition status API",
    description="REST API for retrieving information about current air conditions",
    version="0.1.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
)

app.include_router(iq_air_router)
app.include_router(open_meteo_router)
app.include_router(ninjas_router)
app.include_router(weather_history_router)


origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(engine)
