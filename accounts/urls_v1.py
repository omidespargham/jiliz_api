from django.urls import path
from .views import LoginView

app_name = "accounts_v1"
urlpatterns = [
    path("login/", LoginView.as_view(), name="user_login"),
]
