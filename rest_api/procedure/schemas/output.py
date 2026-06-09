from datetime import datetime

from ninja import Schema


class ProcedureBaseOutputSchema(Schema):
    id: int
    name: str
    type: str
    cost: int
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None


class ProcedureListOutputSchema(Schema):
    id: int
    name: str
    type: str
    cost: int


class ProcedureDetailOutputSchema(Schema):
    id: int
    name: str
    type: str
    cost: int
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None
