import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from authentication.models import Account
from .models import ChannelGroup,Message


class CustomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # get room guid from url
        self.room_guid = self.scope['url_route']['kwargs']['room_guid']
        self.room_group_name = self.room_guid

        await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
                )

        # connect to websocket
        await self.accept()

        self.account = None
        self.channel_group = None


    async def receive(self,text_data):
        # json payload
        json_text = json.loads(text_data)
        message = json_text['message']
        username = json_text['username']

        if self.account is None:
            self.account = await sync_to_async(Account.objects.get)(username = username)
        
        if self.channel_group is None:
            self.channel_group = await sync_to_async(self.account.channel_groups.get)(channel_guid = self.room_guid)

        # save msg to db
        await sync_to_async(Message.objects.create)(
                channel_group = self.channel_group,
                sender_name = username,
                text = message
                )

        # send to all groups
        await self.channel_layer.group_send(
                # message pipeline
                self.room_group_name,
                {
                    'type':'sender',
                    'message':message,
                    'username':username
                    })

        print(f'room name : {self.room_group_name}')


    async def sender(self,event):
        print('sending message!')
        await self.send(text_data = json.dumps({ 
                                                'message':event['message'],
                                                'username':event['username']
                                                }))
