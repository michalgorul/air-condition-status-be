import json

from app.database.weather.schema import WeatherSchema
from app.models import ResponseList, Responses, CountryData, City, CitiesCategorized
from app.iq_air.client import client
from app.iq_air.models import AvailableStates, AvailableCities, WeatherDataResponse, WeatherData
from app.weather_history.service import save_weather_data


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


async def save_data_to_db(weather_response: WeatherDataResponse) -> None:
    weather: WeatherData = weather_response.data
    weather_schema = WeatherSchema(
        city=weather.city,
        state=weather.state,
        country=weather.country,
        latitude=weather.location.coordinates[0],
        longitude=weather.location.coordinates[1],
        temperature=weather.current.weather.tp,
        pressure=weather.current.weather.pr,
        humidity=weather.current.weather.hu,
        aqius=weather.current.pollution.aqius,
        aqicn=weather.current.pollution.aqicn,
    )
    await save_weather_data(weather_schema)


async def get_nearest_city_coords_data(lat: str, lon: str) -> WeatherDataResponse:
    response = await client.get_nearest_city_coords_data(lat, lon)
    weather_response = WeatherDataResponse.parse_obj(response)
    await save_data_to_db(weather_response)
    return weather_response


async def get_city_data(country: str, state: str, city: str) -> WeatherDataResponse:
    response = await client.get_city_data(country, state, city)
    weather_response = WeatherDataResponse.parse_obj(response)
    await save_data_to_db(weather_response)
    return weather_response


async def get_all_cities(country: str) -> ResponseList:
    with open("app/data/responses.json", "r") as file:
        data = json.loads(file.read())

    response = Responses.parse_obj(data)
    if response is None:
        raise ValueError

    try:
        country_data: CountryData = response.countries[country]
        cities = [value.data for key, value in country_data.cities.items()]
        flat_list = [item for sublist in cities for item in sublist]
        return ResponseList(total_elements=len(flat_list), data=sorted(flat_list))
    except KeyError as e:
        raise NotImplemented from e


async def get_all_cities_categorized(country: str) -> CitiesCategorized:
    with open("app/data/responses.json", "r") as file:
        data = json.loads(file.read())

    response = Responses.parse_obj(data)
    if response is None:
        raise ValueError
    try:
        country_data: CountryData = response.countries[country]
        cities = [
            [City(state=state, city=city) for city in value.data]
            for state, value in country_data.cities.items()
        ]
        flat_list = [item for sublist in cities for item in sublist]
        return CitiesCategorized(cities=flat_list, country=country)
    except KeyError as e:
        raise NotImplemented from e
