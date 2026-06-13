from datetime import datetime, time

from ninja import Schema

from rest_api.facility.schemas.output import FacilityDetailOutputSchema


class DoctorBaseOutputSchema(Schema):
    id: int
    name: str
    speciality: str
    is_active: bool
    start_work_time: time
    end_work_time: time
    facility: FacilityDetailOutputSchema
    created_at: datetime


class DoctorListOutputSchema(Schema):
    id: int
    name: str
    speciality: str
    is_active: bool


class DoctorDetailOutputSchema(Schema):
    id: int
    name: str
    speciality: str
    is_active: bool
    start_work_time: time
    end_work_time: time
    facility: FacilityDetailOutputSchema | None
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None
