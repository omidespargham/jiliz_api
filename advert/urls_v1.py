from django.urls import path
from . import views

app_name = 'Advertsv1'

urlpatterns = [
    path('make-advert/', views.MakeAdvert.as_view(), name='make_advert'),
    path('category-childs/<id:category_id>/', views.CategoryChildsView.as_view(),name='category_childs'),
    path('khadamati-category-childs/<id:category_id>/', views.KhadamatiSubCategorysView.as_view(), name='khadamati_sub_categorys'),
    
]
