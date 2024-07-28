# the empty string routes to ChatConsumer, which manages the chat functionality.
from django.urls import path
from .consumer import ChatConsumer

websocket_urlpatterns = [
    path("", ChatConsumer.as_asgi()),
]