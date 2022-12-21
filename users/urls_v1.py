from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import *

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("register/", RegisterApiView.as_view(), name='RegisterUrl'),
    path('verfiy_code/', VerifyCodeApiView.as_view(), name='VerifyUrl'),
    path('resend_code/', ResendCodeForRegisterApiView.as_view(), name='ResendCodeUrl'),
]