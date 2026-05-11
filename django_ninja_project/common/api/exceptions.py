class AppException(Exception):
    status_code = 400
    code = "BAD_REQUEST"
