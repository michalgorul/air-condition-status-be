from typing import List

from fastapi import APIRouter

from app.database.weather.schema import WeatherSchema
from app.weather_history import service

router = APIRouter(prefix="", tags=["Weather History"])


@router.get("/history", response_model=List[WeatherSchema])
async def get_all_weather_data() -> List[WeatherSchema]:
    return await service.get_all_weather_data()


@router.post("/history", response_model=WeatherSchema)
async def save_weather_data(data: WeatherSchema) -> WeatherSchema:
    return await service.save_weather_data(data)


@router.delete("/history/{data_id}", response_model=str)
async def delete_weather_data(data_id: str) -> str:
    return await service.delete_weather_data(data_id)
