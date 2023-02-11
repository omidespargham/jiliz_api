from django.urls import path
from . import views

app_name = "search_v1"

urlpatterns = [
    path("goods-search/<int:range_number>/",views.GoodsSearchView.as_view(),name="goods_search"),
]
