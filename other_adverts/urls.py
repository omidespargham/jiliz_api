from django.urls import path, include

app_name = "other_adverts"
urlpatterns = [
    path('v1/', include('other_adverts.urls_v1',namespace="other_adverts_v1")),

]

