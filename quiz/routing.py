from django.urls import path
from quiz.consumers import QuizConsumer

websocket_urlpatterns = [
    path("ws/quiz/", QuizConsumer.as_asgi()),
]
