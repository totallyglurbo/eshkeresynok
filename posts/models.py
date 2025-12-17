from django.contrib.auth.models import AbstractUser
from django.db import models

class ReallyUser(AbstractUser):

    class Meta(AbstractUser.Meta):
        pass

STATUS_CHOICES = (
    ('in', 'In stock'),
    ('out', 'Out of stock'),
)
class Post(models.Model):
    name = models.CharField(max_length=120, default='Имя')
    description = models.TextField(default='Описание')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='in')
    author = models.ForeignKey('ReallyUser', on_delete=models.CASCADE, verbose_name='Создатель интернета', null=True)
