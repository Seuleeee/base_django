from django.urls import path

from api.views import (
    Board
)


urlpatterns = [
    path('v1/boards', Board.as_view()),
]