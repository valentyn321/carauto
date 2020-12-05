import scrapy
from scrapy.item import Item, Field


class CarautoScraperItem(Item):
    _id = Field()
    link = Field()
    name = Field()
    price = Field()
    year = Field()
    mileage = Field()
    fuel = Field()
    drive_type = Field()