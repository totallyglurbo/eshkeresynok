from django.contrib.auth.models import AbstractUser
from django.db import models

class ReallyUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True,
                               verbose_name='Аватар', default='avatars/image.png')
    email = models.EmailField(unique=True, verbose_name='Адрес электронной почты')


    class Meta(AbstractUser.Meta):
        pass

class Post(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    post_image = models.ImageField(upload_to='posts/', blank=True, null=True,)