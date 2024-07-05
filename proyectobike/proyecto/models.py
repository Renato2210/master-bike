# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Arriendo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bike_model = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} - {self.bike_model}"
