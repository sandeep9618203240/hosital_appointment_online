from django.db import models

class enter(models.Model):
    name=models.CharField(max_length=15)
    phone=models.CharField(max_length=10)

