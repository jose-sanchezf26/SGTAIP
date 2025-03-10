from django.urls import path
from . import views

urlpatterns = [
    path('game_selection', views.game_selection, name='game_selection'),  
    path('<str:game_name>/', views.play_game, name='play_game'),  
]