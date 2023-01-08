from django.urls import path, include 
from .views import returnthestudentview

app_name = 'testt'

urlpatterns = [
    path('students/',returnthestudentview.as_view()),

]


