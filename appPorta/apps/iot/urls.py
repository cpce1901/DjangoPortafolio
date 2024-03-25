from django.urls import path
from .views import MqttLogin, MqttLogout, MqttDashboard, MqttRecive

app_name = 'iot_app'

#URLs app CORE
urlpatterns = [
    path('mqtt/login/', MqttLogin.as_view(), name='mqtt-login'),
    path('mqtt/logout/', MqttLogout.as_view(), name='mqtt-logout'),
    path('mqtt/dashboard/', MqttDashboard.as_view(), name='mqtt-dash'),
    path('mqtt/<int:place>/<int:sen>/', MqttRecive.as_view(), name='mqtt-place-sen'),
]

