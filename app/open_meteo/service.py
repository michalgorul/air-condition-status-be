from app.models import Coordinates
from app.open_meteo.client import client
from app.open_meteo.models import Forecast, DailyWeatherVariables


async def get_forecast_all_values(lat: str, lon: str) -> Forecast:
    coordinates = Coordinates(latitude=lat, longitude=lon)
    values_to_get_list = [member.value for member in DailyWeatherVariables]
    values_to_get_param = {"daily": ",".join(map(str, values_to_get_list))}
    timezone = {"timezone": "auto"}

    params = coordinates.dict() | values_to_get_param | timezone
    return await client.get_forecast_all_values(params=params)
