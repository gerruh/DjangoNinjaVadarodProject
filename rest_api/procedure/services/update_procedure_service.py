from typing import Any

from django.db import IntegrityError, transaction

from apps.procedure.models import Procedure
from common.api.exceptions import NotFoundException, AlreadyExistsException
from rest_api.procedure.schemas.input import ProcedureInputSchema
from rest_api.procedure.schemas.output import ProcedureDetailOutputSchema


class UpdateProcedureService:
    @transaction.atomic
    def execute(self, procedure_id: int, payload: ProcedureInputSchema) -> ProcedureDetailOutputSchema:
        try:
            procedure: Procedure = Procedure.objects.get(id=procedure_id, deleted_at__isnull=True)
        except Procedure.DoesNotExist:
            raise NotFoundException(f"Procedure with id {procedure_id} does not exist")

        data: dict[str, Any] = payload.model_dump(exclude_unset=True)

        for attr, value in data.items():
            setattr(procedure, attr, value)

        try:
            procedure.save()
        except IntegrityError:
            raise AlreadyExistsException(
                f"Procedure with such name '{procedure.name}' and type '{procedure.type}' combination already exists"
            )

        return ProcedureDetailOutputSchema.model_validate(procedure)
