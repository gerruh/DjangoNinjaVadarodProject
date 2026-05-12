from django.http import HttpRequest
from ninja import Query
from ninja.pagination import paginate

from django_ninja_project.medical_app.models import Procedure
from django_ninja_project.rest_api.procedure.schemas.filter import ProcedureFilterSchema
from django_ninja_project.rest_api.procedure.schemas.output import ProcedureOutputSchema


@paginate
def get_procedure_list(request: HttpRequest, filters: ProcedureFilterSchema = Query()) -> list[ProcedureOutputSchema]:
    return [ProcedureOutputSchema.model_validate(obj) for obj in filters.filter(Procedure.objects.all())]