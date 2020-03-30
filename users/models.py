from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_operator = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)


class Operator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    operator_id = models.CharField(max_length=20)


class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    manager_id = models.CharField(max_length=20)
