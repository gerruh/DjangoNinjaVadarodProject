from datetime import time, datetime

from ninja import Schema

from django_ninja_project.rest_api.procedure.schemas.output import ProcedureOutputSchema


class FacilityBaseOutputSchema(Schema):
    id: int
    name: str
    address: str
    start_work_time: time
    end_work_time: time
    procedures: list[ProcedureOutputSchema]
    created_at: datetime

class FacilityListOutputSchema(Schema):
    id: int
    name: str
    address: str

class FacilityDetailOutputSchema(Schema):
    name: str
    address: str
    start_work_time: time
    end_work_time: time
    procedures: list[ProcedureOutputSchema]
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None = None