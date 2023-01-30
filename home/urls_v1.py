from django.urls import path
from . import views

app_name = "Home"

urlpatterns = [
    # this is for 4 adverts with category view
    path("homedata/", views.HomePageDataView.as_view(), name='HomePageDataView'),
    path("scrol-data/<int:num_post>/<str:category_id>/",views.HomePageCategoryDataView.as_view(), name="HomePageDataByCategory"),
    path("save_cache/<str:key>/<str:value>/", views.SaveDataInCacheView.as_view()),
    path("get_cache/<str:key>/", views.GetDataFromCacheView.as_view()),
]
