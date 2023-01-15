from django.urls import path
from . import views

app_name = 'other_adverts_v1'

urlpatterns = [
    path('install_advert_make/', views.InstallRepairMakeView.as_view(), name='InstallAdvertMake'),
]
