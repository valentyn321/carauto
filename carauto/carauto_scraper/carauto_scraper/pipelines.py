import pymongo
import re

from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from search_result.models import CarModel
from poll.models import AutoRiaBrandModel


class MongoDbPipeline(object):

    def process_item(self, item, spider):
        item["mileage"] = re.sub("[^0-9]", "", item["mileage"])

        CarModel.objects.create(
            link=item["link"],
            name=item["name"],
            price=int(item["price"].replace(" ", "")),
            year=item["year"],
            mileage=int(item["mileage"]),
            fuel=item["fuel"],
            drive_type=item["drive_type"]
        )
        return item


class AutoRiaBrandPipeline(object):
    
    def process_item(self, item, spider):

        AutoRiaBrandModel.objects.create(
            brand_id=item["brand_id"],
            brand_name=item["brand_name"]
        )
        return item