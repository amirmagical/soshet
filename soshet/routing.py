# chat/routing.py
from django.urls import path


from . import consumer

websocket_urlpatterns = [
  path("chat/<str:username1>/<str:username2>/", consumer.ChatConsumer.as_asgi()),
 
]