from datetime import datetime
from typing import Annotated

from ninja import Field, FilterLookup, FilterSchema


class ProcedureFilterSchema(FilterSchema):
    name: Annotated[
        str | None,
        FilterLookup(q="name__icontains"),
        Field(description="Procedure name"),
    ] = None
    type: Annotated[
        str | None,
        FilterLookup(q="type"),
        Field(description="Procedure type"),
    ] = None
    cost_from: Annotated[
        int | None,
        FilterLookup(q="cost__gte"),
        Field(description="Procedure cost"),
    ] = None
    cost_to: Annotated[
        int | None,
        FilterLookup(q="cost__lte"),
        Field(description="Procedure cost"),
    ] = None
    created_at_from: Annotated[
        datetime | None,
        FilterLookup(q="created_at__gte"),
        Field(description="Procedure creation date from"),
    ] = None
    created_at_to: Annotated[
        datetime | None,
        FilterLookup(q="created_at__lte"),
        Field(description="Procedure creation date to"),
    ] = None
    updated_at_from: Annotated[
        datetime | None,
        FilterLookup(q="updated_at__gte"),
        Field(description="Procedure updated date from"),
    ] = None
    updated_at_to: Annotated[
        datetime | None,
        FilterLookup(q="updated_at__lte"),
        Field(description="Procedure updated date to"),
    ] = None
    deleted_at_from: Annotated[
        datetime | None,
        FilterLookup(q="deleted_at__gte"),
        Field(description="Procedure deletion date from"),
    ] = None
    deleted_at_to: Annotated[
        datetime | None,
        FilterLookup(q="deleted_at__lte"),
        Field(description="Procedure deletion date to"),
    ] = None
