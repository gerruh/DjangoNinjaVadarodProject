from ninja import Schema


class RegisterOutputSchema(Schema):
    access_token: str
    refresh_token: str

class LoginOutputSchema(Schema):
    access_token: str
    refresh_token: str

class RefreshOutputSchema(Schema):
    access_token: str
    refresh_token: str