from django.urls import path
from .consumers import MqttConsumer, MqttDashConsumer

websocket_urlpatterns = [
    path('mqtt/dashboard/', MqttDashConsumer.as_asgi()),
    path('mqtt/<int:place>/<int:sen>/', MqttConsumer.as_asgi()),
]

