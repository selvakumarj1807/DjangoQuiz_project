from django.urls import path
from quiz import views

urlpatterns = [
    path("test/", views.test_api, name="test_api"),  # Simple test route
]
