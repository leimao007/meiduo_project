from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    inherit from abs so that django will provide user and password authentication
    """
    mobile = models.CharField(max_length=11, unique=True)

    class Meta:
        db_table = 'tb_users'
        verbose_name = 'user management'
        verbose_name_plural = verbose_name
