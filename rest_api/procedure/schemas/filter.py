from datetime import datetime

from ninja import FilterSchema
from pydantic import Field

class ProcedureFilterSchema(FilterSchema):
    id: int = Field(
        None,
        description="Procedure id",
        json_schema_extra={"q": "id"},
    )
    name: str = Field(
        None,
        description="Procedure name",
        json_schema_extra={"q": "name__icontains"},
    )
    type: str = Field(
        None,
        description="Procedure type",
        json_schema_extra={"q": "type"},
    )

    cost_from: int = Field(
        None,
        description="Procedure cost",
        json_schema_extra={"q": "start_work_time__gte"},
    )

    cost_to: int = Field(
        None,
        description="Procedure cost",
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
