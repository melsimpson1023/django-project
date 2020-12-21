import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatRoomConsumer(AsyncWebsocketConsumer):
  # when we want an asynchronous function in python, we declare it with async def
    async def connect(self):
      # we are defining the room name
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        # we are defining the group name for the chat
        self.room_group_name = 'chat_%s' % self.room_name
        # functionality of the channels package
        # we are adding a new group here
        await self.channel_layer.group_add(
        # constructing a new group
            self.room_group_name,
            self.channel_name
        )
        # we are sending the group a message
        await self.channel_layer.group_send(
          self.room_group_name,
          {
            'type': 'tester_message',
            # we are going to pass in a string called tester
            'tester': 'hello world',
          }
        )
    async def tester_message(self, event):
        # collecting data
        tester = event['tester']

        await self.send(text_data=json.dumps({
          'tester': tester,
        }))

        await self.accept()
        # we are disconnecting from the group chat
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chatroom_message',
                'message': message,
                'username': username,
            }
        )

    async def chatroom_message(self, event):
        message = event['message']
        username = event['username']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
        }))

    pass
