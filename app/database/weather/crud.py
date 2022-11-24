from typing import List

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.database import engine
from app.database.weather.model import WeatherTable
from app.database.weather.schema import WeatherSchema


def get_all_weather_data() -> List[WeatherSchema]:
    with Session(engine) as session:
        return [WeatherSchema(**row.dict()) for row in session.query(WeatherTable).all()]


async def save_weather_data(data: WeatherSchema) -> WeatherSchema:
    with Session(engine) as session:
        try:
            row = WeatherTable(**data.dict())
            session.add(row)
            session.commit()
            return WeatherSchema(**row.dict())
        except Exception as e:
            error_str = f"Failed to add row to table, data={data.dict()}, error={e}"
            print(error_str)
            raise ValueError(error_str)
