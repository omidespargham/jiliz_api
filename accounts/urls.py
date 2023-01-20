from django.urls import path,include
app_name = "accounts"

urlpatterns = [
    path("v1/",include("accounts.urls_v1",namespace="accounts_v1")),
]