from django.db import models

class CarModel(models.Model):
    link = models.CharField(max_length=256, primary_key=True)
    name = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    year = models.IntegerField()
    mileage = models.IntegerField()
    fuel = models.CharField(max_length=64)
    drive_type = models.CharField(max_length=128)