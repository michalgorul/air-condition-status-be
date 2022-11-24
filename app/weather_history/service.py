from typing import List

from fastapi import HTTPException

from app.database.weather import crud
from app.database.weather.schema import WeatherSchema


async def get_all_weather_data() -> List[WeatherSchema]:
    return crud.get_all_weather_data()


async def save_weather_data(data: WeatherSchema) -> WeatherSchema:
    try:
        return await crud.save_weather_data(data)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))


async def delete_weather_data(data_id: str) -> str:
    try:
        return await crud.delete_weather_data(data_id)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
