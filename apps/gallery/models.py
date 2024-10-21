from django.db import models
from apps.common.utils import compress_image

class Gallery(models.Model):
    image = models.ImageField(
        verbose_name="Галерея",
        upload_to='gallery/'
    )

    description = models.CharField(
        max_length=100,
        verbose_name="Описание"
    )

    def save(self, *args, **kwargs):
        if self.image:
            compressed_image = compress_image(self.image)
            self.image.save(self.image.name, compressed_image, save=False)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"

class Stages(models.Model):
    image = models.ImageField(
        verbose_name="Этапы строительства",
        upload_to='Stages/'
    )

    def save(self, *args, **kwargs):
        if self.image:
            compressed_image = compress_image(self.image)
            self.image.save(self.image.name, compressed_image, save=False)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Этап строительства"
        verbose_name_plural = "Этапы строительства"
