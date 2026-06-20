from ninja import Schema


class AuthInputSchema(Schema):
    login: str
    password: str