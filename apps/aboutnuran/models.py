from django.db import models
from solo.models import SingletonModel


class AboutCompany(SingletonModel):
    aboutCompany = models.TextField(
        max_length=255,
        verbose_name="О компании"
    )

    aboutProject = models.TextField(
        verbose_name="О проекте"
    )

    video_link = models.URLField(
        max_length=255,
        verbose_name='Ссылка на видео'
    )

    def __str__(self):
        return f'О компании'

    class Meta:
        verbose_name = "О компании"
        verbose_name_plural = "О компании"


