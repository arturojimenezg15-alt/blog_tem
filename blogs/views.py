from django.shortcuts import render
from .models import Publication
from django.views.generic import ListView
from django.views.generic.edit import CreateView
# Create your views here.


class PublicationListView(ListView):
    model = Publication
    template_name = 'home.html'

class PublicationCreteView(CreateView):
    model = Publication
    template_name = 'create.html'
    fields = ['title', 'content', 'author']
    