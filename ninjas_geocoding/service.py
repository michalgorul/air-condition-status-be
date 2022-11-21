from ninjas_geocoding.client import client
from ninjas_geocoding.models import GeolocationResponse


async def get_geolocation(city: str, country: str | None) -> GeolocationResponse:
    response = await client.get_geolocation(city, country)
    try:
        return GeolocationResponse.parse_obj(response[0])
    except IndexError as e:
        print(f"Failed to get first element from response, error={e}")
