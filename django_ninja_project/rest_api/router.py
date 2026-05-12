from ninja import NinjaAPI

from django_ninja_project.rest_api.exception_handlers import register_exception_handlers
from django_ninja_project.rest_api.facility.router import facility_router
from django_ninja_project.rest_api.procedure.router import procedure_router

api = NinjaAPI(
    version='1.0.0',
    title='django_ninja_project API',
    docs_url='/docs',
)

api.add_router('/facility/', facility_router)
api.add_router('/procedure/', procedure_router)

register_exception_handlers(api)
