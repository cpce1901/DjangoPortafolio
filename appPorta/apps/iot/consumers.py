from django.conf import settings
from channels.generic.websocket import AsyncWebsocketConsumer
import asyncio
import json
import paho.mqtt.client as mqtt

class MqttConsumer(AsyncWebsocketConsumer):

    topic=None
    
    async def connect(self):

        # Obtener los valores de la URL
        self.place_id = self.scope['url_route']['kwargs']['place']
        self.sen_id = self.scope['url_route']['kwargs']['sen']

        self.topic = f"place/{self.place_id}/sen/{self.sen_id}"

        await self.accept()

        # Conexión MQTT
        self.mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=settings.MQTT_ID)
        self.mqtt_client.username_pw_set(username=settings.MQTT_USERNAME, password=settings.MQTT_PASSWORD)
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_message = self.on_message
        self.mqtt_client.connect(settings.MQTT_BROKER, settings.MQTT_PORT, 60)
        self.mqtt_client.loop_start()

        await self.send(text_data=json.dumps({
            'topic': self.topic,

        }))

    async def disconnect(self, close_code):
        # Detener el bucle MQTT
        self.mqtt_client.loop_stop()

    def on_connect(self, client, userdata, flags, reason_code, properties):
        # Suscribirse a un topic MQTT
        client.subscribe(self.topic)

    def on_message(self, client, userdata, msg):
        # Manejar los mensajes MQTT recibidos
        message = msg.payload.decode()
        # Enviar el mensaje al WebSocket
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.send_message_to_group(message))

    async def send_message_to_group(self, message):
        # Enviar mensaje al WebSocket
        await self.send(text_data=json.dumps({
            'message': message,

        }))

        
        
      
 


        
   


        
       
       
