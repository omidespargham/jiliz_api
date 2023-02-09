from django.urls import path
from . import views

app_name = 'Advertsv1'

urlpatterns = [
    path('make-advert/', views.MakeAdvert.as_view(), name='make_advert'),
    path('make-advert2/', views.MakeAdvert2.as_view(), name='make_advert'),
    path('category-childs/<int:category_id>/', views.CategoryChildsView.as_view(),name='category_childs'),
    path('khadamati-category-childs/<int:category_id>/', views.KhadamatiSubCategorysView.as_view(), name='khadamati_sub_categorys'),
    path('get-good-categorys/', views.GoodCategorysView.as_view(), name='get_good_categorys'),
    path('countrys-made-by/', views.CountrysMakeByView.as_view(), name='country_made_by'),
    path('citys/', views.CityView.as_view(), name='citys'),
    path('brands/', views.BrandView.as_view(), name='brands'),
]
