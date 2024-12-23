from django.db import models
from solo.models import SingletonModel


class Links(SingletonModel):
    yt_title = models.CharField(
        max_length=100,
        verbose_name="Youtube название"
    )
    yt_link = models.URLField(
        max_length=255,
        verbose_name="YouTube ссылка"
    )
    ig_title = models.CharField(
        max_length=100,
        verbose_name="Instagram название"
    )
    ig_link = models.URLField(
        max_length=255,
        verbose_name="Instagram ссылка"
    )
    wt_title = models.CharField(
        max_length=100,
        verbose_name="Whatsapp название"
    )
    wt_link = models.URLField(
        max_length=255,
        verbose_name="Watsapp ссылка"
    )
    email_link = models.EmailField(
        max_length=255,
        verbose_name="Почта"
    )

    def __str__(self):
        return f'{self.yt_link} {self.ig_link} {self.wt_link} {self.email_link}'

    class Meta:
        verbose_name = "Ссылки"
        verbose_name_plural = "Ссылки"


