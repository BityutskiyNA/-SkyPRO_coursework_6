from django.conf import settings
from django.db import models

from users.models import User


class Ad(models.Model):
    # TODO добавьте поля модели здесь
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField()
    image = models.ImageField(upload_to='images/',default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Обьявление'
        verbose_name_plural = 'Обьявления'


class Comment(models.Model):
    # TODO добавьте поля модели здесь
    text = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    ad = models.ForeignKey(Ad, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

