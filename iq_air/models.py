from typing import List

from pydantic import Field

from app.models import BaseModel


class State(BaseModel):
    state: str


class City(BaseModel):
    city: str


class AvailableStates(BaseModel):
    status: str
    data: List[State]


class AvailableCities(BaseModel):
    status: str
    data: List[City]


class Location(BaseModel):
    type: str
    coordinates: List[float]


class Pollution(BaseModel):
    ts: str = Field(..., alias="timestamp", description="Timestamp")
    aqius: int = Field(..., description="AQI value based on US EPA standard")
    mainus: str = Field(..., description="main pollutant for US AQI")
    aqicn: int = Field(..., description="AQI value based on China MEP standard")
    maincn: str = Field(..., description="main pollutant for Chinese AQI")


class Weather(BaseModel):
    ts: str = Field(..., alias="timestamp", description="Timestamp")
    tp: int = Field(..., alias="temperature", description="Temperature in Celsius")
    pr: int = Field(..., alias="pressure", description="Atmospheric pressure in hPa")
    hu: int = Field(..., alias="humidity", description="Humidity %")
    ws: float = Field(..., alias="windSpeed", description="Wind speed (m/s)")
    wd: int = Field(
        ...,
        alias="windDirection",
        description="Wind direction, as an angle of 360° (N=0, E=90, S=180, " "W=270)",
    )
    ic: str = Field(
        ..., alias="iconCode", description="Weather icon code, see below for icon index"
    )


class CurrentPollutionWeather(BaseModel):
    pollution: Pollution
    weather: Weather


class WeatherData(BaseModel):
    city: str
    state: str
    country: str
    location: Location
    current: CurrentPollutionWeather


class WeatherDataResponse(BaseModel):
    status: str
    data: WeatherData
