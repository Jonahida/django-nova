from django.urls import path
from . import views

urlpatterns = [
    path("api/pages/<int:pk>/blocks/", views.blocks_api, name="blocks_api"),
]

