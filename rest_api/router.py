from ninja import NinjaAPI

from rest_api.doctor.router import doctor_router
from rest_api.exception_handlers import register_exception_handlers
from rest_api.facility.router import facility_router
from rest_api.procedure.router import procedure_router

api = NinjaAPI(
    version='1.0.0',
    title='DNP API',
    docs_url='/docs',
)

api.add_router('/facility/', facility_router)
api.add_router('/procedure/', procedure_router)
api.add_router('/doctor/', doctor_router)

register_exception_handlers(api)
