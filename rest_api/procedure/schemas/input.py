from ninja import Schema

from apps.procedure.models import ProcedureTypeChoices


class ProcedureInputSchema(Schema):
    name: str
    type: ProcedureTypeChoices
    cost: int


class ProcedurePatchSchema(ProcedureInputSchema):
    name: str | None = None
    type: ProcedureTypeChoices | None = None
    cost: int | None = None
