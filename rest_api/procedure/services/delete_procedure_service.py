import datetime

from django.db import transaction

from common.api.exceptions import NotFoundException
from apps.procedure.models import Procedure
from rest_api.procedure.schemas.output import ProcedureDetailOutputSchema


class DeleteProcedureService:
    @transaction.atomic
    def execute(self, procedure_id: int) -> ProcedureDetailOutputSchema:
        try:
            procedure: Procedure = Procedure.objects.get(id=procedure_id, deleted_at__isnull=True)
        except Procedure.DoesNotExist:
            raise NotFoundException(f"Procedure with id {procedure_id} not found")

        procedure.deleted_at = datetime.datetime.now(datetime.timezone.utc)
        procedure.save()

        return ProcedureDetailOutputSchema.model_validate(procedure)