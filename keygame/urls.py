from django.urls import path
from . import views

urlpatterns = [
    path('', views.init_key_game, name='init_key_game'),
]