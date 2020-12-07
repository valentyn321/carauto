from django.contrib import admin
from .models import CarModel

class CarModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(CarModel, CarModelAdmin)