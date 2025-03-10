# games/routing.py

from django.urls import re_path
from .consumers import GameConsumer

websocket_urlpatterns = [
    re_path(r'ws/game-events', GameConsumer.as_asgi()),  # Ruta WebSocket
]
