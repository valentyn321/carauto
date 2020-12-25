import scrapy
from scrapy.http import Request
from re import findall

from carauto_scraper.items import CarautoScraperItem


class AutoriaSpider(scrapy.Spider):
    name = 'autoria'
    allowed_domains = ['auto.ria.com']
    start_urls = [
        'https://auto.ria.com/search/?categories.main.id=1&price.currency=1&price.USD.lte=5000&indexName=auto&brand.id[0]=6&size=100&page=0',
        "https://auto.ria.com//search/?icategories.main.id=1&brand.id[0]=6&year[0].gte=2000&year[0].lte=2015&price.USD.gte=4000&price.USD.lte=6997&fuel.id[0]=1&drive.id[0]=2&size=100&mileage.gte=25000&mileage.lte=99995"
    ]
    custom_settings = {
        'ITEM_PIPELINES': {
            'carauto_scraper.pipelines.MongoDbPipeline': 200,
        }
    }

    def parse(self, response):
        searchResults = response.xpath("//div[@id='searchResults']")
        cars = searchResults.xpath("//section[contains(@class, 'ticket-item')]")
        if cars.extract():
            for car in cars:
                car_item = CarautoScraperItem()
                car_item['link'] = car.xpath(".//a[@class='address']/@href").get()
                car_item['name'] = car.xpath(".//a[@class='address']/@title").get()
                car_item['price'] = car.xpath(".//span[@data-currency='USD']/text()").get()
                car_item['year'] = car.xpath(".//a[@class='address']/text()")[1].get()
                car_item['mileage'] = car.xpath(".//i[@title='Пробег']/following-sibling::text()").get()
                car_item['fuel'] = car.xpath(".//i[@title='Тип топлива']/following-sibling::text()").get()
                car_item['drive_type'] = car.xpath(".//i[@title='Тип коробки передач']/following-sibling::text()").get()
                yield car_item 

            current_page_number = int(findall(r'&page=(.*)', response.url)[0])
            current_page_url = findall(r'(.*)&page=', response.url)[0]
            next_page_number = current_page_number + 1
            next_page_url = f"{current_page_url}&page={next_page_number}"
            yield Request(next_page_url, callback=self.parse)