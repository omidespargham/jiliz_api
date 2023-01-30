from django.urls import path, include 
from .views import returnthestudentview,OneView

app_name = 'testt'

urlpatterns = [
    path('students/',returnthestudentview.as_view()),
    path('ones/',OneView.as_view()),
]


