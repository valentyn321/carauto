import scrapy
from scrapy_djangoitem import DjangoItem
from search_result.models import CarModel


class CarautoScraperItem(DjangoItem):
    django_model = CarModel
    link = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    year = scrapy.Field()
    mileage = scrapy.Field()
    fuel = scrapy.Field()
    drive_type = scrapy.Field()