from ninja import Schema
from pydantic import EmailStr


class RegisterInputSchema(Schema):
    email: EmailStr
    password: str

class LoginInputSchema(Schema):
    email: EmailStr
    password: str

class RefreshInputSchema(Schema):
    refresh_token: str