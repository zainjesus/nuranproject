from django.db import models
from solo.models import SingletonModel


class Order(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="ФИО"
    )
    number = models.CharField(
        max_length=255,
        verbose_name="Номер"
    )

    def __str__(self):
        return f'{self.full_name} {self.number}'

    class Meta:
        verbose_name = 'Заказ на звонок'
        verbose_name_plural = 'Заказы на звонок'


class Email(SingletonModel):
    email = models.EmailField(verbose_name="Почта для получения заказов")

    class Meta:
        verbose_name = "Почта"
        verbose_name_plural = "Почта"
