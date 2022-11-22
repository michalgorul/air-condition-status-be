from fastapi import APIRouter

from app.ninjas_geocoding import service
from app.ninjas_geocoding.models import GeolocationResponse

router = APIRouter(prefix="", tags=["Ninjas Geolocation"])


@router.get("/geolocation", response_model=GeolocationResponse)
async def get_geolocation(city: str, country: str | None = None) -> GeolocationResponse:
    return await service.get_geolocation(city, country)
