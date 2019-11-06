# Django
from django.urls import path

# views
from . import views

urlpatterns = [
    path(route='series/',
        view=views.AllSeries.as_view(),
        name='series'
    ),
    
]