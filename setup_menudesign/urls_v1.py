from django.urls import path
from . import views

app_name = 'setup_menudesign'

urlpatterns = [
    path('make-advert/', views.MakeAdverb.as_view(), name='MakeSetupMenuDesign'),

    


]
