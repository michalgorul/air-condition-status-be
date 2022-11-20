from typing import List, Any, Dict

from pydantic import BaseModel as Model, Field


class BaseModel(Model):
    class Config:
        allow_population_by_field_name = True
        orm_mode = True


class ResponseList(BaseModel):
    total_elements: int = Field(..., alias="totalElements")
    data: List[Any]


class CountryData(BaseModel):
    states: ResponseList = Field(...)
    cities: Dict[str, ResponseList] = Field(...)


class Responses(BaseModel):
    countries: Dict[str, CountryData] = Field(...)


class City(BaseModel):
    city: str = Field(...)
    state: str = Field(...)


class CitiesCategorized(BaseModel):
    cities: List[City] = Field(...)
    country: str = Field(...)


class Coordinates(BaseModel):
    latitude: str
    longitude: str
