from django.shortcuts import render
from django.views.generic import TemplateView, ListView

# Models
from series.models import Series, Episodes

# Create your views here.

class AllSeries(ListView):
    model = Series
    template_name = 'series/series.html'
    context_object_name = 'series'
    paginate_by = 30