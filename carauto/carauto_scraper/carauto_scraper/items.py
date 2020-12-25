import scrapy
from scrapy_djangoitem import DjangoItem
from search_result.models import CarModel
from poll.models import AutoRiaBrandModel


class CarautoScraperItem(DjangoItem):
    django_model = CarModel
    link = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    year = scrapy.Field()
    mileage = scrapy.Field()
    fuel = scrapy.Field()
    drive_type = scrapy.Field()

class AutoRiaBrandItem(scrapy.Item):
    brand_id = scrapy.Field()
    brand_name = scrapy.Field()