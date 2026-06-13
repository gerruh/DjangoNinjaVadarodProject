from datetime import time

from ninja import Schema


class DoctorInputSchema(Schema):
    name: str
    speciality: str
    is_active: bool
    start_work_time: time = time(8, 0)
    end_work_time: time = time(17, 0)
    facility: int


class DoctorPatchSchema(Schema):
    name: str | None = None
    speciality: str | None = None
    is_active: bool | None = None
    start_work_time: time | None = None
    end_work_time: time | None = None
    facility: int | None = None
