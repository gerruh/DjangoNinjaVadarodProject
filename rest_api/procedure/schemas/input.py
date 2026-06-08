from ninja import Schema


class ProcedureInputSchema(Schema):
    name: str
    type: str
    cost: int

class ProcedurePatchSchema(Schema):
    name: str | None
    type: str | None
    cost: int | None