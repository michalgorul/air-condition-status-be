from datetime import datetime

from app.database.model import SchemaModel


class WeatherSchema(SchemaModel):
    id: str | None
    timestamp: datetime | None
    city: str
    state: str
    country: str
    latitude: str
    longitude: str
    temperature: float
    pressure: int
    humidity: int
    aqius: int
    aqicn: int
