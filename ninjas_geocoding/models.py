from pydantic import Field

from app.models import BaseModel


class GeolocationResponse(BaseModel):
    name: str = Field(...)
    latitude: str = Field(...)
    longitude: str = Field(...)
    country: str = Field(...)
    state: str = Field(...)
