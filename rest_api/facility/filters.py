from datetime import datetime, time
from typing import Annotated

from ninja import Field, FilterLookup, FilterSchema


class FacilityFilterSchema(FilterSchema):
    name: Annotated[
        str | None,
        FilterLookup(q="name__icontains"),
        Field(description="Facility name"),
    ] = None
    address: Annotated[
        str | None,
        FilterLookup(q="address__icontains"),
        Field(description="Facility address"),
    ] = None
    start_work_time_from: Annotated[
        time | None,
        FilterLookup(q="start_work_time__gte"),
        Field(description="Facility start work time"),
    ] = None
    start_work_time_to: Annotated[
        time | None,
        FilterLookup(q="start_work_time__lte"),
        Field(description="Facility start work time"),
    ] = None
    end_work_time_from: Annotated[
        time | None,
        FilterLookup(q="end_work_time__gte"),
        Field(description="Facility end work time"),
    ] = None
    end_work_time_to: Annotated[
        time | None,
        FilterLookup(q="end_work_time__lte"),
        Field(description="Facility end work time"),
    ] = None
    procedures: Annotated[
        list[int] | None,
        FilterLookup(q="procedures__id__in"),
        Field(description="Facility procedures"),
    ] = None
    created_at_from: Annotated[
        datetime | None,
        FilterLookup(q="created_at__gte"),
        Field(description="Facility creation date from"),
    ] = None
    created_at_to: Annotated[
        datetime | None,
        FilterLookup(q="created_at__lte"),
        Field(description="Facility creation date to"),
    ] = None
    updated_at_from: Annotated[
        datetime | None,
        FilterLookup(q="updated_at__gte"),
        Field(description="Facility updated date from"),
    ] = None
    updated_at_to: Annotated[
        datetime | None,
        FilterLookup(q="updated_at__lte"),
        Field(description="Facility updated date to"),
    ] = None
    deleted_at_from: Annotated[
        datetime | None,
        FilterLookup(q="deleted_at__gte"),
        Field(description="Facility deletion date from"),
    ] = None
    deleted_at_to: Annotated[
        datetime | None,
        FilterLookup(q="deleted_at__lte"),
        Field(description="Facility deletion date to"),
    ] = None
