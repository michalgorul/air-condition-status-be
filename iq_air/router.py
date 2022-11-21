from fastapi import APIRouter

from app.models import ResponseList, CitiesCategorized
from iq_air import service
from iq_air.models import WeatherDataResponse

router = APIRouter(prefix="", tags=["IQ Air"])


@router.get("/states", response_model=ResponseList)
async def get_available_states(country: str) -> ResponseList:
    return await service.get_available_states(country)


@router.get("/cities", response_model=ResponseList)
async def get_available_cities(country: str, state: str) -> ResponseList:
    return await service.get_available_cities(country, state)


@router.get("/{country}/cities/all", response_model=ResponseList)
async def get_all_polish_cities(country: str) -> ResponseList:
    return await service.get_all_cities(country)


@router.get("/{country}/cities/all/categorized", response_model=CitiesCategorized)
async def get_all_cities_categorized(country: str) -> CitiesCategorized:
    return await service.get_all_cities_categorized(country)


@router.get("/nearest_city", response_model=WeatherDataResponse)
async def get_nearest_city_data() -> WeatherDataResponse:
    return await service.get_nearest_city_data()


@router.get("/nearest_city", response_model=WeatherDataResponse)
async def get_nearest_city_coords_data(lat: str, lon: str) -> WeatherDataResponse:
    return await service.get_nearest_city_coords_data(lat, lon)


@router.get("/city", response_model=WeatherDataResponse)
async def get_city_data(country: str, state: str, city: str) -> WeatherDataResponse:
    return await service.get_city_data(country, state, city)
