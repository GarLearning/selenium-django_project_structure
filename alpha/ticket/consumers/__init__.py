import json
from channels.generic.websocket import AsyncWebsocketConsumer

class SharedData:
    data = []

class PreviewConsumer(AsyncWebsocketConsumer):    
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({"type": "websocket.receive", "text": f"Step completed"}))
    
    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        await self.send(text_data=json.dumps({'data': SharedData.data}))