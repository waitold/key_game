from django.urls import path
from . import views

urlpatterns = [
    path('', views.key_game, name='key_game'),
    path('/init/', views.init_game, name='init_game')
]