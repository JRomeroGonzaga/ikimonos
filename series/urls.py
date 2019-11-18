# Django
from django.urls import path, re_path

# views
from . import views

urlpatterns = [
    path(route='series',
        view=views.AllSeries.as_view(),
        name='series'
    ),

    # re_path(route='search',
    #     view=views.search,
    #     name='search-series'
    # ),
    
    path(route='<slug>/',
        view=views.SerieProfile.as_view(),
        name='serie'
    ),

]