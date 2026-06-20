from ninja import Schema


class UserInputSchema(Schema):
    email: str
    password: str