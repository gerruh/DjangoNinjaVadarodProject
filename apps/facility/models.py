from django.db import models
import datetime

from apps.procedure.models import Procedure
from common.mixins.model_mixins import TimeStampMixin
from config.validators import cyrillic_validator, address_validator


class Facility(TimeStampMixin):
    name = models.CharField(
        max_length=100,
        validators=[cyrillic_validator],
        verbose_name="Название мед. учреждения",
    )

    address = models.CharField(
        max_length=100,
        validators=[address_validator],
        verbose_name="Адрес учреждения"
    )

    start_work_time = models.TimeField(
        default=datetime.time(0, 0),
        verbose_name="Начало времени работы учреждения"

    )

    end_work_time = models.TimeField(
        default=datetime.time(23, 59),
        verbose_name="Конец времени рабочего дня"
    )

    procedures = models.ManyToManyField(
        Procedure,
        related_name="facilities",
    )

    class Meta:
        ordering = ["created_at"]
        verbose_name = "Учреждение"
        verbose_name_plural = "Учреждения"
        db_table = "facility"
        constraints = [
            models.UniqueConstraint(
                fields=["name", "address"],
                name="unique_facility_name_address",
            )
        ]
