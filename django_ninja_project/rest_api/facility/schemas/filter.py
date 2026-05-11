from datetime import datetime, time

from ninja import FilterSchema
from pydantic import Field


class FacilityFilterSchema(FilterSchema):
    id: int = Field(
        None,
        description="Facility id",
        json_schema_extra={"q": "id"},
    )
    name: str = Field(
        None,
        description="Facility name",
        json_schema_extra={"q": "name__icontains"},
    )
    address: str = Field(
        None,
        description="Facility address",
        json_schema_extra={"q": "address__icontains"},
    )

    start_work_time_from: time = Field(
        None,
        description="Facility start work time",
        json_schema_extra={"q": "start_work_time__gte"},
    )

    start_work_time_to: time = Field(
        None,
        description="Facility start work time",
        json_schema_extra={"q": "start_work_time__lte"},
    )

    end_work_time_from: time = Field(
        None,
        description="Facility end work time",
        json_schema_extra={"q": "end_work_time__gte"},
    )

    end_work_time_from_to: time = Field(
        None,
        description="Facility end work time",
        json_schema_extra={"q": "end_work_time__lte"},
    )

    procedures: list[int] = Field(
        None,
        description="Facility procedures",
        json_schema_extra={"q": "procedures__id__in"},
    )

    created_at: datetime = Field(
        None,
        description="Facility creation date",
        json_schema_extra={"q": "created_at"},
    )
    updated_at: datetime = Field(
        None,
        description="Facility creation date",
        json_schema_extra={"q": "updated_at"},
    )
    deleted_at: datetime = Field(
        None,
        description="Facility deletion date",
        json_schema_extra={"q": "deleted_at"},
    )
