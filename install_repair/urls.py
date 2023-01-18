from django.urls import path, include

app_name = "install_repair"
urlpatterns = [
    path('v1/', include('install_repair.urls_v1',namespace="install_repair_v1")),

]

