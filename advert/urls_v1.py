from django.urls import path
from . import views

app_name = 'Advertsv1'

urlpatterns = [
    path('make-advert/', views.MakeAdverb.as_view(), name='MakeAdverb'),
    path('search-in-categorys/<str:category_name>/', views.CategoryChildsView.as_view()),
    path('search-in-khadamati/<str:category_name>/', views.DetailSubCategoryKhadamatiView.as_view(), name='ShowAdverts'),
    


]
