from datetime import datetime

from ninja import Schema


class ProcedureOutputSchema(Schema):
    id: int
    name: str
    type: str
    cost: int
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None