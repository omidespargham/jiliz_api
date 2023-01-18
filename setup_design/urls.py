from django.urls import path, include

app_name = "setup_design"
urlpatterns = [
    path('v1/', include('setup_design.urls_v1',namespace="setup_design_v1")),

]

