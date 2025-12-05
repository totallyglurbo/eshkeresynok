from django.contrib.auth.models import AbstractUser
from django.db import models

class ReallyUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True,
                               verbose_name='Аватар', default='avatars/image.png')


    class Meta(AbstractUser.Meta):
        pass
#