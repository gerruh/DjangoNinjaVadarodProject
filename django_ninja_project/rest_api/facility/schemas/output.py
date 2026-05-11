from datetime import time, datetime

from ninja import Schema


class FacilityOutputSchema(Schema):
    id: int
    name: str
    address: str
    start_work_time: time
    end_work_time: time
    procedures: list[int]
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None
