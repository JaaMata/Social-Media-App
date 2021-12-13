import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ProfileConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.connect()


    async def receive(self, data):
        data = {'test': 'hello'}
        data = json.dumps(data)
        await self.send(text_data=data)


    async def disconnect(self, code):
        pass