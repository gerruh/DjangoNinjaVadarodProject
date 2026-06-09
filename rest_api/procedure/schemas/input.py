from ninja import Schema


class ProcedureInputSchema(Schema):
    name: str
    type: str
    cost: int

class ProcedurePatchSchema(ProcedureInputSchema):
    name: str | None = None
    type: str | None = None
    cost: int | None = None