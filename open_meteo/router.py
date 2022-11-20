from fastapi import APIRouter

from open_meteo import service
from open_meteo.models import Forecast

router = APIRouter(prefix="", tags=["Open Meteo"])


@router.get("/forecast/{lat}/{lon}", response_model=Forecast)
async def get_forecast(lat: str, lon: str) -> Forecast:
    return await service.get_forecast_all_values(lat, lon)
