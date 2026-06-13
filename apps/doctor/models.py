from django.db import models
import datetime

from apps.facility.models import Facility
from common.mixins.model_mixins import TimeStampMixin
from config.validators import cyrillic_validator


class Doctor(TimeStampMixin):
    name = models.CharField(
        max_length=100,
        validators=[cyrillic_validator],
        verbose_name="Имя врача",
    )

    speciality = models.CharField(
        max_length=100,
        validators=[cyrillic_validator],
        verbose_name="Специальность",
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="Признак активности"
    )

    start_work_time = models.TimeField(
        default=datetime.time(0,0),
        verbose_name="Начало времени работы учреждения"

    )

    end_work_time = models.TimeField(
        default=datetime.time(23,59),
        verbose_name="Конец времени рабочего дня"
    )

    facility = models.ForeignKey(
        Facility,
        on_delete=models.CASCADE,
        related_name="doctors",
        verbose_name='Учреждение работы'
    )

    class Meta:
        ordering = ["created_at"]
        verbose_name = "Доктор"
        verbose_name_plural = "Доктора"
        db_table = "doctor"