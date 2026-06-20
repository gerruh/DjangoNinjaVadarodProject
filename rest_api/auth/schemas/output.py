from ninja import Schema


class AuthOutputSchema(Schema):
    access_token: str
    refresh_token: str