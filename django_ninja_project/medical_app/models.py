from django.core.validators import RegexValidator
from django.db import models

from django_ninja_project.common.models import TimeStampMixin


class ProcedureTypeChoices(models.TextChoices):
    BLOOD = "blood", "Кровь"
    HEAD = "head", "Голова"


class Procedure(TimeStampMixin):
    name = models.CharField(
        max_length=100,
        validators=[RegexValidator(regex=r"[а-яА-ЯёЁ]")],
        verbose_name="Имя процедуры",
    )

    type = models.CharField(
        max_length=100,
        choices=ProcedureTypeChoices,
        default=ProcedureTypeChoices.BLOOD,
        verbose_name="Тип услуги")

    cost = models.PositiveIntegerField(
        default=0,
        verbose_name="Цена услуги"
    )

    class Meta:
        ordering = ["-id"]
        verbose_name = "Процедура"
        verbose_name_plural = "Процедуры"
        db_table = "procedure"


class Facility(TimeStampMixin):
    name = models.CharField(
        max_length=100,
        validators=[RegexValidator(regex=r"[а-яА-ЯёЁ]")],
        verbose_name="Название мед. учреждения",
    )

    address = models.CharField(
        max_length=100,
        verbose_name="Адрес учреждения"
    )

    start_work_time = models.TimeField(
        default="08:00",
        verbose_name="Начало времени работы учреждения"

    )

    end_work_time = models.TimeField(
        default="17:00",
        verbose_name="Конец времени рабочего дня"
    )

    procedures = models.ManyToManyField(
        Procedure,
        related_name="procedures",
    )

    class Meta:
        ordering = ["-id"]
        verbose_name = "Учреждение"
        verbose_name_plural = "Учреждения"
        db_table = "facility"


class Doctor(TimeStampMixin):
    name = models.CharField(
        max_length=100,
        validators=[RegexValidator(regex=r"[а-яА-ЯёЁ]")],
        verbose_name="Имя врача",
    )

    speciality = models.CharField(
        max_length=100,
        validators=[RegexValidator(regex=r"[а-яА-ЯёЁ]")],
        verbose_name="Специальность",
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="Признак активности"
    )

    start_work_time = models.TimeField(
        default="08:00",
        verbose_name="Начало времени работы учреждения"

    )

    end_work_time = models.TimeField(
        default="17:00",
        verbose_name="Конец времени рабочего дня"
    )

    facility = models.ForeignKey(
        Facility,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Учреждение работы'
    )

    class Meta:
        ordering = ["-id"]
        verbose_name = "Доктор"
        verbose_name_plural = "Доктора"
        db_table = "doctor"
