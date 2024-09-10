from django.db import models
from django.core.exceptions import ValidationError


class BaseDesign(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")

    class Meta:
        abstract = True  # Эта модель не будет создавать таблицу в базе данных

    def __str__(self):
        return self.title


class GraphicDesign(BaseDesign):
    image = models.ImageField(upload_to='images/', verbose_name="Изображение")
    image2 = models.ImageField(upload_to='images/', verbose_name="Изображение 2", blank=True, null=True)
    image3 = models.ImageField(upload_to='images/', verbose_name="Изображение 3", blank=True, null=True)
    image4 = models.ImageField(upload_to='images/', verbose_name="Изображение 4", blank=True, null=True)

    def clean(self):
        max_images = 4  # Максимальное количество изображений
        if GraphicDesign.objects.filter(title=self.title).count() >= max_images:
            raise ValidationError(f"Нельзя загрузить больше {max_images} изображений.")

    class Meta:
        verbose_name = "Графический дизайн"
        verbose_name_plural = "Графический дизайн"
        ordering = ['-uploaded_at']


class MotionDesign(BaseDesign):
    cover = models.ImageField(upload_to='images/', verbose_name="Обложка")
    video1 = models.FileField(upload_to='videos/', verbose_name="Видео 1", blank=True, null=True)
    video2 = models.FileField(upload_to='videos/', verbose_name="Видео 2", blank=True, null=True)

    def clean(self):
        max_videos = 2  # Максимальное количество видео
        if GraphicDesign.objects.filter(title=self.title).count() >= max_videos:
            raise ValidationError(f"Нельзя загрузить больше {max_videos} изображений.")
        
    class Meta:
        verbose_name = "Моушн дизайн"
        verbose_name_plural = "Моушн дизайн"
        ordering = ['-uploaded_at']


class TreeD_Design(BaseDesign):
    image = models.ImageField(upload_to='images/', verbose_name="Изображение")
    image2 = models.ImageField(upload_to='images/', verbose_name="Изображение 2", blank=True, null=True)
    image3 = models.ImageField(upload_to='images/', verbose_name="Изображение 3", blank=True, null=True)
    image4 = models.ImageField(upload_to='images/', verbose_name="Изображение 4", blank=True, null=True)

    def clean(self):
        max_images = 4  # Максимальное количество изображений
        if GraphicDesign.objects.filter(title=self.title).count() >= max_images:
            raise ValidationError(f"Нельзя загрузить больше {max_images} изображений.")

    class Meta:
        verbose_name = "3D дизайн"
        verbose_name_plural = "3D дизайн"
        ordering = ['-uploaded_at'] 