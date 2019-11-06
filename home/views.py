from django.shortcuts import render
from django.views.generic import TemplateView

from series.models import Series, Episodes

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        series = Series.objects.all()
        context = {'series': series}
        
        return context

