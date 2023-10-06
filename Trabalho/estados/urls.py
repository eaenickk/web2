from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("regiões", views.index, name="index"),
    path("nordeste", views.nordeste, name="nordeste"),
    path("norte", views.norte, name="norte"),
    path('ceara', views.ceara, name ="ceara"),
    path('pernambuco', views.pernambuco, name ="pernambuco")

]

