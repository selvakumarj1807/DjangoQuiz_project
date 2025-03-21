from django.urls import path
from quiz import views
from quiz.views import quiz_page

urlpatterns = [
    path("", quiz_page, name="quiz_page"),
    path("test/", views.test_api, name="test_api"),  # Simple test route
]
