import logging

from app.models import ResponseList
from iq_air.client import client
from iq_air.models import AvailableStates, AvailableCities, WeatherData, WeatherDataResponse


async def get_available_states(country: str) -> ResponseList:
    response = await client.get_available_states(country)
    available_states = [
        state.state for state in AvailableStates.parse_obj(response).data if response
    ]
    return ResponseList(total_elements=len(available_states), data=available_states)


async def get_available_cities(country: str, state: str) -> ResponseList:
    response = await client.get_available_cities(country, state)
    available_cities = [city.city for city in AvailableCities.parse_obj(response).data if response]
    print(available_cities)

    return ResponseList(total_elements=len(available_cities), data=available_cities)


async def get_nearest_city_data() -> WeatherDataResponse:
    response = await client.get_nearest_city_data()
    return WeatherDataResponse.parse_obj(response)


async def get_nearest_city_coords_data(lat: str, lon: str) -> WeatherDataResponse:
    response = await client.get_nearest_city_coords_data(lat, lon)
    return WeatherDataResponse.parse_obj(response)


async def get_city_data(country: str, state: str, city: str) -> WeatherDataResponse:
    response = await client.get_city_data(country, state, city)
    return WeatherDataResponse.parse_obj(response)
