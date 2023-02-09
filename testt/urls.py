from django.urls import path, include 
from .views import returnthestudentview,OneView,CreateOneView

app_name = 'testt'

urlpatterns = [
    path('students/',returnthestudentview.as_view()),
    path('ones/',OneView.as_view()),
    path('onecreate/',CreateOneView.as_view()),
]


