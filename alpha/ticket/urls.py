from django.urls import path
from .views import (
    Home,
    Create,
    FillOs,
    Preview,
)
urlpatterns = [
    path("", Home.as_view()),
    path("create", Create.as_view()),
    path("fill.os", FillOs.as_view()),
    path("preview", Preview.as_view()),
]
