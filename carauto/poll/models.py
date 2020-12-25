from django.db import models

class SearchModel(models.Model):
    brand = models.CharField(max_length=128)
    min_price = models.DecimalField(max_digits=8, decimal_places=2)
    max_price = models.DecimalField(max_digits=8, decimal_places=2)
    min_year = models.IntegerField()
    max_year = models.IntegerField()
    min_mileage = models.IntegerField()
    max_mileage = models.IntegerField()
    fuel = models.CharField(max_length=64)
    drive_type = models.CharField(max_length=128)

class AutoRiaBrandModel(models.Model):
    brand_id = models.CharField(max_length=8)
    brand_name = models.CharField(max_length=128)