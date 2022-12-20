from django.urls import path 
from . import views

app_name = "Home"

urlpatterns = [
    path("homesearch-view/", views.HomePageSearchView.as_view(), name='SearchViewForHomePAge'),
    path("homedata/", views.HomePageDataView.as_view(), name='HomePageDataView')
]

