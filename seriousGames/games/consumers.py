# games/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import GameMessage
from datetime import datetime
from django.db import models
from channels.db import database_sync_to_async
from asgiref.sync import sync_to_async


class GameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Obtén el game_id de la URL
        user = self.scope.get('user')
        self.current_user = "unknown_user"  
        self.current_session = "unknown_session"  
        print(f"User in connect: {user}")
        
        # Acepta la conexión WebSocket
        await self.accept()
        # await self.send(text_data=json.dumps({
        #             'type': 'username',
        #             'message': user.username
        #         }))

    async def disconnect(self, close_code):
        user = self.current_user
        session_id = self.current_session
        game_message = GameMessage(
            user=user,
            session_id=session_id, 
            game_id="Survival Rules",
            event_type="sr-log_out",
            time=datetime.now(),  # Puedes usar la hora que envíes desde el juego o la hora actual
            data=""
        )
        print(game_message)
        try:
            # Intentamos guardar el mensaje
            await database_sync_to_async(game_message.save)()
            print("Mensaje guardado en la base de datos")
        except Exception as e:
        # Si ocurre un error, lo capturamos y lo mostramos
            print(f"Error al guardar el mensaje: {e}")
        pass

    # Recibe un mensaje desde WebSocket
    async def receive(self, text_data):
        # Deserializar el mensaje JSON recibido
        text_data_json = json.loads(text_data)

        # Obtener los datos del mensaje
        user = text_data_json.get('user')
        event_type = text_data_json.get('eventType')
        data = text_data_json.get('data')
        game_id_m = text_data_json.get('gameId')
        session_id = text_data_json.get('sessionId')
        self.current_user = user
        self.current_session = session_id
        time = text_data_json.get('time')

        # Almacenar el mensaje en la base de datos
        game_message = GameMessage(
            user=user,
            session_id=session_id,  # Esto puede venir de la conexión si lo necesitas
            game_id=game_id_m,
            event_type=event_type,
            time=datetime.strptime(time, "%d/%m/%Y %H:%M:%S"),  # Puedes usar la hora que envíes desde el juego o la hora actual
            data=data
        )
        print(game_message)
        try:
            # Intentamos guardar el mensaje
            await database_sync_to_async(game_message.save)()
            print("Mensaje guardado en la base de datos")
        except Exception as e:
        # Si ocurre un error, lo capturamos y lo mostramos
            print(f"Error al guardar el mensaje: {e}")