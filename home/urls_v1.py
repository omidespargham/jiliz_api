from django.urls import path 
from . import views

app_name = "Home"

urlpatterns = [
    path("homesearch-view/", views.HomePageSearchView.as_view(), name='SearchViewForHomePAge'),
    # this is for 4 adverts with category view
    path("homedata/", views.HomePageDataView.as_view(), name='HomePageDataView'),
    path("scrol-data/<int:num_post>/<str:category_id>/", views.HomePageCategoryDataView.as_view(), name="HomePageDataByCategory"),
]

