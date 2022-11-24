from typing import Any, Dict
from uuid import uuid4

import sqlalchemy
from sqlalchemy import Column, DateTime, func, String, Float, Integer, inspect
from sqlalchemy.dialects.postgresql import UUID

from app.database.model import Base


class WeatherTable(Base):
    __tablename__ = "weather"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    city = Column(String)
    state = Column(String)
    country = Column(String)
    latitude = Column(String)
    longitude = Column(String)
    temperature = Column(Float)
    pressure = Column(Integer)
    humidity = Column(Integer)
    aqius = Column(Integer)
    aqicn = Column(Integer)

    __mapper_args__ = {"eager_defaults": True}

    def dict(self) -> Dict[str, Any]:
        d = {}
        for column in self.__table__.columns:
            d[column.name] = str(getattr(self, column.name))

        return d
