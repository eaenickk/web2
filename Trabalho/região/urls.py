from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="cuida"),
    path("regiões", views.index, name="index")
]