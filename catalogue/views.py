from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from catalogue.models import Content


class ContentListView(ListView):
    model = Content
    template_name = 'home.html'

    def get_data(self):
        data = [{
            'title': content.title,
            'score': content.score
        } for content in self.object_list]
        return data

    def get_queryset(self):
        queryset = super(ContentListView, self).get_queryset()
        return queryset