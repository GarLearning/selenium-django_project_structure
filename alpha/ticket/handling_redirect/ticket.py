from ticket.actions import CallFunctions
from .config import Description
import asyncio
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class SharedData:
    data = []

class TicketRedirect(AsyncWebsocketConsumer):
    def __init__(self, form={}, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form = form
    
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({"type": "websocket.receive", "text": f"Step completed"}))
    
    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        await self.send(text_data=json.dumps({'data': SharedData.data}))
    
    async def create(self):
        await asyncio.sleep(5)
        ...
