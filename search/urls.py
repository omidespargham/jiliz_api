from django.urls import path, include
app_name = "search"
urlpatterns = [
    path("v1", include("search.urls_v1", namespace="search_v1"))
]
