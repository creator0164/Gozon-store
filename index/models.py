from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
