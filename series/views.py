from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.http import HttpResponse, request
from django.core import serializers
from django.db.models import Q
import json

# Models
from series.models import Series, Episodes

# Create your views here.

class AllSeries(ListView):
    model = Series
    template_name = 'series/series.html'
    context_object_name = 'series'
    paginate_by = 1

class SerieProfile(DetailView):
    template_name = 'series/serie-profile.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    queryset = Series.objects.all()
    context_object_name = 'serie'