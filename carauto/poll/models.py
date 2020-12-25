from django.db import models

class AutoRiaBrandModel(models.Model):
    brand_id = models.CharField(max_length=8)
    brand_name = models.CharField(max_length=128)

class SearchModel(models.Model):

    def brands_choices():
        res = []
        all_brands = AutoRiaBrandModel.objects.all()
        for brand in all_brands:
            res.append((brand.brand_id, brand.brand_name))
        return res

    brand = models.CharField(
        max_length=128,
        choices=brands_choices()
        )
    min_price = models.DecimalField(max_digits=8, decimal_places=2)
    max_price = models.DecimalField(max_digits=8, decimal_places=2)
    min_year = models.IntegerField()
    max_year = models.IntegerField()
    min_mileage = models.IntegerField()
    max_mileage = models.IntegerField()
    fuel = models.CharField(max_length=64)
    drive_type = models.CharField(max_length=128)

    def brands_choices(self):
        res = []
        all_brands = AutoRiaBrandModel.objects.all()
        for brand in all_brands:
            res.append((brand.brand_id, brand.brand_name))
        return res