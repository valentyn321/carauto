from django.forms import ModelForm
from poll.models import SearchModel

class SearchModelForm(ModelForm):
    class Meta:
        model = SearchModel
        fields = '__all__'
