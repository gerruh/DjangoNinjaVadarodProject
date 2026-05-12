from django.core.validators import RegexValidator


cyrillic_validator = RegexValidator(
    regex=r"^[а-яА-ЯёЁ\s-]+$",
    message="Поле должно содержать только кириллицу"
)

address_validator = RegexValidator(
    regex=r"^[а-яА-ЯёЁ0-9\s.,\-]+$",
    message="Некорректный адрес"
)