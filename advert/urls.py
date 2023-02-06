from django.urls import path, include


urlpatterns = [
    path('v1/', include('advert.urls_v1',namespace="advert_v1")),

]

