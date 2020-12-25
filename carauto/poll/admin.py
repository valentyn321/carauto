from django.contrib import admin
from .models import SearchModel, AutoRiaBrandModel

class SearchModelAdmin(admin.ModelAdmin):
    pass

class AutoRiaBrandModelAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(SearchModel, SearchModelAdmin)
admin.site.register(AutoRiaBrandModel, AutoRiaBrandModelAdmin)