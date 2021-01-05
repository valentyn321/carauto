from django.db import models
from django.contrib.auth.models import User


class AutoRiaBrandModel(models.Model):
    brand_id = models.CharField(max_length=8)
    brand_name = models.CharField(max_length=128)

class SearchModel(models.Model):
    brand = models.ForeignKey(AutoRiaBrandModel,on_delete=models.CASCADE)
    min_price = models.DecimalField(max_digits=8, decimal_places=2)
    max_price = models.DecimalField(max_digits=8, decimal_places=2)
    min_year = models.IntegerField()
    max_year = models.IntegerField()
    min_mileage = models.IntegerField()
    max_mileage = models.IntegerField()
    fuel = models.CharField(
        max_length=64,
        choices=[
            ("1", "Бензин"),
            ("2", "Дизель"),
            ("3", "Газ"),
            ("4", "Газ / Бензин"),
            ("5", "Гібрид"),
            ("6", "Електро"),
            ("7", "Інше"),
            ("8", "Газ метан"),
            ("9", "Газ пропан-бутан")
            ]
        )
    drive_type = models.CharField(
        max_length=128,
        choices=[
            ("1", "Повний"),
            ("2", "Передній"),
            ("3", "Задній"),
            ("4", "Кардан"),
            ("5", "Ремінь"),
            ("6", "Ланцюг")
            ]
        )
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def brands_choices(self):
        res = []
        all_brands = AutoRiaBrandModel.objects.all()
        for brand in all_brands:
            res.append((brand.brand_id, brand.brand_name))
        return res