from django.urls import path
from . import views


urlpatterns = [
    path('make-adverb/', views.MakeAdverb.as_view(), name='MakeAdverb'),
    path('view-advert/<str:slug>/', views.ShowAdvertApiView.as_view(), name='ShowAdverts'),


]