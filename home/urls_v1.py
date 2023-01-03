from django.urls import path 
from . import views

app_name = "Home"

urlpatterns = [
    path("homesearch-view/", views.HomePageSearchView.as_view(), name='SearchViewForHomePAge'),
    path("homedata/", views.HomePageDataView.as_view(), name='HomePageDataView'),
    path("load-data-all/<int:num_post>/", views.HomePageAllCategoriesView.as_view(), name="AllDataViewHomePage"),
    path("scrol-data/<int:num_post>/<str:category_id>/", views.HomePageCategoryDataView.as_view(), name="HomePageDataByCategory"),
]

