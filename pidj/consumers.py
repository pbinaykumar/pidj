from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        room_name = 'newroom'
        self.group_name=room_name
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, code):
        pass

    async def receive(self, text_data=None, bytes_data=None):
        print('receive')
        await self.channel_layer.group_send(
            self.group_name,
            {
                "type":"process_chat_data",
                "value":text_data,
            }
        )

    async def process_chat_data(self,event):
        print(event["value"])
        message = event["value"]

        await self.send(message)
