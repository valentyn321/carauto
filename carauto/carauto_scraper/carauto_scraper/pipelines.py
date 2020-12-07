import pymongo
import re

from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from search_result.models import CarModel


class MongoDbPipeline(object):

    # def __init__(self):
    #     client = pymongo.MongoClientclient = pymongo.MongoClient("mongodb+srv://valentyn:valentyn24@carauto.7j760.mongodb.net/<dbname>?retryWrites=true&w=majority")
    #     db = client.get_database("carauto")
    #     self.collection = db.cars
        

    def process_item(self, item, spider):
        # valid = True
        # for data in item:
        #     if not data:
        #         valid = False
        #         raise DropItem(f"Missing {data}!")
        # if valid:
        #         old_item = self.collection.find_one({"link": item["link"]})
        #         if old_item:
        #             print("This car is already in DB!")
        #         else:
        #             item['year'] = item['year'].strip()
        #             item['mileage'] = item['mileage'].strip()
        #             item['fuel'] = item['fuel'].strip()
        #             item['drive_type'] = item['drive_type'].strip()

        #             self.collection.insert_one(dict(item))
        #             print(f"{item['name']} was added to MongoDB database!")
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