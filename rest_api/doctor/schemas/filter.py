from datetime import datetime, time
from typing import Annotated

from ninja import Field, FilterLookup, FilterSchema


class DoctorFilterSchema(FilterSchema):
    id: Annotated[
        int | None,
        FilterLookup(q="id"),
        Field(description="Doctor id"),
    ] = None
    name: Annotated[
        str | None,
        FilterLookup(q="name__icontains"),
        Field(description="Doctor name"),
    ] = None
    speciality: Annotated[
        str | None,
        FilterLookup(q="speciality__icontains"),
        Field(description="Doctor speciality"),
    ] = None
    is_active: Annotated[
        bool | None,
        FilterLookup(q="is_active"),
        Field(description="Doctor active status"),
    ] = None
    start_work_time_from: Annotated[
        time | None,
        FilterLookup(q="start_work_time__gte"),
        Field(description="Doctor start work time from"),
    ] = None
    start_work_time_to: Annotated[
        time | None,
        FilterLookup(q="start_work_time__lte"),
        Field(description="Doctor start work time to"),
    ] = None
    end_work_time_from: Annotated[
        time | None,
        FilterLookup(q="end_work_time__gte"),
        Field(description="Doctor end work time from"),
    ] = None
    end_work_time_to: Annotated[
        time | None,
        FilterLookup(q="end_work_time__lte"),
        Field(description="Doctor end work time to"),
    ] = None
    facility: Annotated[
        int | None,
        FilterLookup(q="facility"),
        Field(description="Doctor facility id"),
    ] = None
    created_at_from: Annotated[
        datetime | None,
        FilterLookup(q="created_at__gte"),
        Field(description="Doctor creation date from"),
    ] = None
    created_at_to: Annotated[
        datetime | None,
        FilterLookup(q="created_at__lte"),
        Field(description="Doctor creation date to"),
    ] = None
    updated_at_from: Annotated[
        datetime | None,
        FilterLookup(q="updated_at__gte"),
        Field(description="Doctor updated date from"),
    ] = None
    updated_at_to: Annotated[
        datetime | None,
        FilterLookup(q="updated_at__lte"),
        Field(description="Doctor updated date to"),
    ] = None
    deleted_at_from: Annotated[
        datetime | None,
        FilterLookup(q="deleted_at__gte"),
        Field(description="Doctor deletion date from"),
    ] = None
    deleted_at_to: Annotated[
        datetime | None,
        FilterLookup(q="deleted_at__lte"),
        Field(description="Doctor deletion date to"),
    ] = None
