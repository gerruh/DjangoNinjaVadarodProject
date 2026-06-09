from django.db import transaction, IntegrityError

from apps.procedure.models import Procedure
from common.api.exceptions import AlreadyExistsException
from rest_api.procedure.schemas.input import ProcedureInputSchema
from rest_api.procedure.schemas.output import ProcedureBaseOutputSchema


class CreateProcedureService:
    @transaction.atomic
    def execute(self, payload: ProcedureInputSchema) -> ProcedureBaseOutputSchema:
        try:
            procedure: Procedure = Procedure.objects.create(
                **payload.dict()
            )
        except IntegrityError:
            raise AlreadyExistsException(
                f"Procedure with such {payload.name} and {payload.type} combination already exists"
            )
        return ProcedureBaseOutputSchema.model_validate(procedure)
