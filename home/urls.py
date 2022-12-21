from django.urls import path, include 

urlpatterns = [
    path('v1/', include('home.urls_v1')),

]


