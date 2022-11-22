from fastapi import APIRouter

from app.open_meteo import service
from app.open_meteo.models import Forecast

router = APIRouter(prefix="", tags=["Open Meteo"])


@router.get("/forecast", response_model=Forecast)
async def get_forecast(lat: str, lon: str) -> Forecast:
    return await service.get_forecast_all_values(lat, lon)
