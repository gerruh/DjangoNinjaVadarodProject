from django.db import models

from common.mixins.model_mixins import TimeStampMixin
from config.validators import cyrillic_validator


class ProcedureTypeChoices(models.TextChoices):
    BLOOD = "blood", "Кровь"
    HEAD = "head", "Голова"


class Procedure(TimeStampMixin):
    name = models.CharField(
        max_length=100,
        validators=[cyrillic_validator],
        verbose_name="Имя процедуры",
    )

    type = models.CharField(
        max_length=100,
        choices=ProcedureTypeChoices,
        default=ProcedureTypeChoices.BLOOD,
        verbose_name="Тип услуги")

    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="Цена услуги"
    )

    class Meta:
        ordering = ["created_at"]
        verbose_name = "Процедура"
        verbose_name_plural = "Процедуры"
        db_table = "procedure"
        constraints = [
            models.UniqueConstraint(
                fields=["name", "type"],
                name="unique_procedure_type",
            )
        ]
