from typing import List, Any

from pydantic import BaseModel as Model, Field


class BaseModel(Model):
    class Config:
        allow_population_by_field_name = True
        orm_mode = True


class ResponseList(BaseModel):
    total_elements: int = Field(..., alias="totalElements")
    data: List[Any]
