from datetime import time

from ninja import FilterSchema
from pydantic import Field


class DoctorFilterSchema(FilterSchema):
    id: int = Field(
        None,
        description="Doctor id",
        json_schema_extra={"q": "id"},
    )
    name: str = Field(
        None,
        description="Doctor name",
        json_schema_extra={"q": "name__icontains"},
    )
    speciality: str = Field(
        None,
        description="Doctor speciality",
        json_schema_extra={"q": "type"},
    )

    is_active: bool = Field(
        None,
        description="Doctor active status",
        json_schema_extra={"q": "is_active"},
    )

    start_work_time_from: time = Field(
        None,
        description="Doctor start work time from",
        json_schema_extra={"q": "start_work_time__gte"},
    )

    start_work_time_to: time = Field(
        None,
        description="Doctor start work time to",
        json_schema_extra={"q": "start_work_time__lte"},
    )

    end_work_time_from: time = Field(
        None,
        description="Doctor end work time from",
        json_schema_extra={"q": "end_work_time__gte"},
    )

    end_work_time_to: time = Field(
        None,
        description="Doctor end work time to",
        json_schema_extra={"q": "end_work_time__lte"},
    )

    facility: str = Field(
        None,
        description="Doctor facility",
        json_schema_extra={"q": "start_work_time__lte"},
    )

    created_at: datetime = Field(
        None,
        description="Procedure creation date",
        json_schema_extra={"q": "created_at"},
    )
    updated_at: datetime = Field(
        None,
        description="Procedure creation date",
        json_schema_extra={"q": "updated_at"},
    )
    deleted_at: datetime = Field(
        None,
        description="Procedure deletion date",
        json_schema_extra={"q": "deleted_at"},
    )