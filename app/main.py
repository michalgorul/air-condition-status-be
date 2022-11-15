from typing import Any, Dict

from fastapi import FastAPI

from app.models import ResponseList
from iq_air import service
from iq_air.client import client
from iq_air.models import WeatherData, WeatherDataResponse

app = FastAPI()


@app.get("/")
async def root() -> Dict[str, Any]:
    return {"message": "Hello World"}


@app.get("/states/{country}")
async def get_available_states(country: str) -> ResponseList:
    return await service.get_available_states(country)


@app.get("/cities/{country}/{state}")
async def get_available_cities(country: str, state: str) -> ResponseList:
    return await service.get_available_cities(country, state)


@app.get("/nearest_city")
async def get_nearest_city_data() -> WeatherDataResponse:
    return await service.get_nearest_city_data()


@app.get("/nearest_city/{lat}/{lon}")
async def get_nearest_city_coords_data(lat: str, lon: str) -> WeatherDataResponse:
    return await service.get_nearest_city_coords_data(lat, lon)


@app.get("/city/{country}/{state}/{city}")
async def get_city_data(country: str, state: str, city: str) -> WeatherDataResponse:
    return await service.get_city_data(country, state, city)
