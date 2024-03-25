from django.urls import path
from .consumers import MqttConsumer

websocket_urlpatterns = [
    path('mqtt/<int:place>/<int:sen>/', MqttConsumer.as_asgi()),
]

