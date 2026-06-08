from datetime import datetime, time

from ninja import Schema


class DoctorOutputSchema(Schema):
    id: int
    name: str
    speciality: str
    is_active: bool
    start_work_time: time
    end_work_time: time
    facility: int
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None