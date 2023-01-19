from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_token
app_name = 'Advertsv1'

urlpatterns = [
    path('make-advert/', views.MakeAdverb.as_view(), name='MakeAdverb'),
    path('search-data-bas/', views.SearchDataView.as_view(), name='SearchBaseView'),
    path('search-in-categorys/<str:category>/', views.DetailCategoryView.as_view()),
    path('search-in-khadamati/<str:category>/', views.DetailSubCategoryKhadamatiView.as_view(), name='ShowAdverts'),
    path('view-advert/<str:slug>/', views.ShowAdvertApiView.as_view(), name='ShowAdverts'),
    path('multi-search/', views.MultiSearchView.as_view(), name='MultiSearchUrl'),
    path("api_tokenn/",auth_token.obtain_auth_token)
    


]
