from fastapi import HTTPException

from app.ninjas_geocoding.client import client
from app.ninjas_geocoding.models import GeolocationResponse


async def get_geolocation(city: str, country: str | None) -> GeolocationResponse:
    response = await client.get_geolocation(city, country)
    try:
        return GeolocationResponse.parse_obj(response[0])
    except Exception as ke:
        print(f"Failed to get geocoding info, error={ke}")
        raise HTTPException(status_code=422, detail="Failed to get geocoding info")
