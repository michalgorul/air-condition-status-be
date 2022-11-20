from enum import Enum
from typing import List

from pydantic import Field

from app.models import BaseModel


class DailyWeatherVariables(Enum):
    WEATHERCODE = "weathercode"
    TEMPERATURE_2M_MAX = "temperature_2m_max"
    TEMPERATURE_2M_MIN = "temperature_2m_min"
    APPARENT_TEMPERATURE_MAX = "apparent_temperature_max"
    APPARENT_TEMPERATURE_MIN = "apparent_temperature_min"
    SUNRISE = "sunrise"
    SUNSET = "sunset"
    PRECIPITATION_SUM = "precipitation_sum"
    RAIN_SUM = "rain_sum"
    SHOWERS_SUM = "showers_sum"
    SNOWFALL_SUM = "snowfall_sum"
    PRECIPITATION_HOURS = "precipitation_hours"
    WINDSPEED_10M_MAX = "windspeed_10m_max"
    WINDGUSTS_10M_MAX = "windgusts_10m_max"
    WINDDIRECTION_10M_DOMINANT = "winddirection_10m_dominant"
    SHORTWAVE_RADIATION_SUM = "shortwave_radiation_sum"
    ET_0_FAO_EVAPOTRANSPIRATION = "et0_fao_evapotranspiration"


class ForecastDailyUnits(BaseModel):
    time: str | None = Field(...)
    weathercode: str | None = Field(...)
    temperature_2m_max: str | None = Field(..., alias="temperature2mMax")
    temperature_2m_min: str | None = Field(..., alias="temperature2mMin")
    apparent_temperature_max: str | None = Field(..., alias="apparentTemperatureMax")
    apparent_temperature_min: str | None = Field(..., alias="apparentTemperatureMin")
    sunrise: str | None = Field(...)
    sunset: str | None = Field(...)
    precipitation_sum: str | None = Field(..., alias="precipitationSum")
    rain_sum: str | None = Field(..., alias="rainSum")
    showers_sum: str | None = Field(..., alias="showersSum")
    snowfall_sum: str | None = Field(..., alias="snowfallSum")
    precipitation_hours: str | None = Field(..., alias="precipitationHours")
    windspeed_10m_max: str | None = Field(..., alias="windspeed10mMax")
    windgusts_10m_max: str | None = Field(..., alias="windgusts10mMax")
    winddirection_10m_dominant: str | None = Field(..., alias="winddirection10mDominant")
    shortwave_radiation_sum: str | None = Field(..., alias="shortwaveRadiationSum")
    et0_fao_evapotranspiration: str | None = Field(..., alias="et0FaoEvapotranspiration")


class ForecastDailyValues(BaseModel):
    time: List[str] | None = Field(...)
    weathercode: List[int] | None = Field(...)
    temperature_2m_max: List[float] | None = Field(..., alias="temperature2mMax")
    temperature_2m_min: List[float] | None = Field(..., alias="temperature2mMin")
    apparent_temperature_max: List[float] | None = Field(..., alias="apparentTemperatureMax")
    apparent_temperature_min: List[float] | None = Field(..., alias="apparentTemperatureMin")
    sunrise: List[str] | None = Field(...)
    sunset: List[str] | None = Field(...)
    precipitation_sum: List[float] | None = Field(..., alias="precipitationSum")
    rain_sum: List[float] | None = Field(..., alias="rainSum")
    showers_sum: List[float] | None = Field(..., alias="showersSum")
    snowfall_sum: List[float] | None = Field(..., alias="snowfallSum")
    precipitation_hours: List[int] | None = Field(..., alias="precipitationHours")
    windspeed_10m_max: List[float] | None = Field(..., alias="windspeed10mMax")
    windgusts_10m_max: List[float] | None = Field(..., alias="windgusts10mMax")
    winddirection_10m_dominant: List[int] | None = Field(..., alias="winddirection10mDominant")
    shortwave_radiation_sum: List[float] | None = Field(..., alias="shortwaveRadiationSum")
    et0_fao_evapotranspiration: List[float] | None = Field(..., alias="et0FaoEvapotranspiration")


class Forecast(BaseModel):
    latitude: float = Field(...)
    longitude: float = Field(...)
    generationtime_ms: float = Field(..., alias="generationtimeMs")
    utc_offset_seconds: int = Field(..., alias="utcOffsetSeconds")
    timezone: str = Field(...)
    timezone_abbreviation: str = Field(..., alias="timezoneAbbreviation")
    elevation: int = Field(...)
    daily_units: ForecastDailyUnits = Field(..., alias="dailyUnits")
    daily: ForecastDailyValues = Field(...)
