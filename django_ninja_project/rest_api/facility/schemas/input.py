from datetime import time
from ninja import Schema
from pydantic import Field


class FacilityInputSchema(Schema):
    name: str
    address: str
    start_work_time: time = time(8, 0)
    end_work_time: time = time(17, 0)
    procedures: list[int] = Field(default_factory=list)


class FacilityPatchSchema(FacilityInputSchema):
    name: str | None = None
    address: str | None = None
    start_work_time: time | None = None
    end_work_time: time | None = None
    procedures: list[int] | None = None
