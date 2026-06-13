from datetime import time, datetime


from ninja import Schema

from rest_api.procedure.schemas.output import ProcedureDetailOutputSchema


class FacilityBaseOutputSchema(Schema):
    id: int
    name: str
    address: str
    start_work_time: time
    end_work_time: time
    procedures: list[ProcedureDetailOutputSchema]
    created_at: datetime


class FacilityListOutputSchema(Schema):
    id: int
    name: str
    address: str


class FacilityDetailOutputSchema(Schema):
    id: int
    name: str
    address: str
    start_work_time: time
    end_work_time: time
    procedures: list[ProcedureDetailOutputSchema]
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None = None