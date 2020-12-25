import scrapy
from scrapy.http import Request
from re import findall

from carauto_scraper.items import AutoRiaBrandItem


class AutoriaSpider(scrapy.Spider):
    name = 'brand_scraper'
    allowed_domains = ['auto.ria.com']
    start_urls = [
        'https://auto.ria.com/uk/',
    ]
    custom_settings = {
        'ITEM_PIPELINES': {
            'carauto_scraper.pipelines.AutoRiaBrandPipeline': 200,
        }
    }


    def parse(self, response):
        cars_brands = response.xpath("//div[@id='brandTooltipBrandAutocomplete-brand']//ul[contains(@class, 'autocomplete-select')]/li[@class='list-item']")
        if cars_brands.extract():
            for brand in cars_brands:
                cars_brand = AutoRiaBrandItem()
                cars_brand['brand_id'] = brand.xpath(".//@data-value").get()
                cars_brand['brand_name'] = brand.xpath(".//text()").get()
                yield cars_brand