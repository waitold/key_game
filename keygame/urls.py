from django.urls import path
from . import views

urlpatterns = [
    path('', views.key_game, name='init_key_game'),
]