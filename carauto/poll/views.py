import scrapy

from scrapy.crawler import CrawlerProcess
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.shortcuts import render, reverse

from poll.models import SearchModel
from carauto_scraper.carauto_scraper.spiders.autoria import AutoriaSpider 


class MainPollView(CreateView):
    template_name = 'poll/main_poll.html'
    model = SearchModel
    fields = "__all__"

    def get_last(self):
        poll_result = SearchModel.objects.all().last()
        return poll_result

    def url_generator(self):
        last_poll_result = self.get_last()
        request_url = f"https://auto.ria.com/search/?icategories.main.id=1&\
brand.id[0]={last_poll_result.brand}&\
year[0].gte={last_poll_result.min_year}&\
year[0].lte={last_poll_result.max_year}&\
price.USD.gte={last_poll_result.min_price}&\
price.USD.lte={last_poll_result.max_price}&f\
uel.id[0]={last_poll_result.fuel}&\
rive.id[0]={last_poll_result.fuel}&\
mileage.gte={last_poll_result.min_mileage}&\
mileage.lte={last_poll_result.max_mileage}&\
size=100"
        
        print(request_url)
        try:
            process = CrawlerProcess()
            process.crawl(AutoriaSpider, start_urls=[request_url])
            process.start()
        except:
            print("Crawling did not start")


    def get_success_url(self):
        self.url_generator()
        return reverse('main_poll')

