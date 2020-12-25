from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.shortcuts import render, reverse

from poll.models import SearchModel

class MainPollView(CreateView):
    template_name = 'poll/main_poll.html'
    model = SearchModel
    fields = "__all__"

    def start_crawling(self):
        poll_result = SearchModel.objects.all().last()
        print(poll_result.mileage)

    def get_success_url(self):
        self.print_google()
        return reverse('main_poll')
