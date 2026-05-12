from datetime import time

from ninja import Schema



class DoctorInputSchema(Schema):
    name: str
    speciality: str
    is_active: bool
    start_work_time: time
    end_work_time: time
    facility: int

class DoctoPatchSchema(Schema):
    name: str | None = None
    speciality: str | None = None
    is_active: bool | None = None
    start_work_time: time | None = None
    end_work_time: time | None = None
    facility: int | None = None