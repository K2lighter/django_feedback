from django.db import models
from django.core.validators import MinLengthValidator


class Feedback(models.Model):
    """
    Не забываем делать миграции
    """
    name = models.CharField(max_length=10, validators=[MinLengthValidator(3)])  # max_length - обязательный параметр
    surname = models.CharField(max_length=21)
    feedback = models.TextField()
    rating = models.PositiveIntegerField()  # только положительные числа могут быть

