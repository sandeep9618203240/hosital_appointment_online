from django.db import models
class first(models.Model):
    name=models.CharField(max_length=20)
    phonenumber=models.CharField(max_length=10)

    def __str__(self):
        return self.name
    