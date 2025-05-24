import json
import datetime
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer
from asgiref.sync import sync_to_async

from authentication.models import Account
from .models import ChannelGroup,Message


class CustomConsumer(AsyncWebsocketConsumer):
    account = None
    channel_group = None

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
        model = await sync_to_async(Message.objects.create)(
                channel_group = self.channel_group,
                sender_name = username,
                text = message
                )

        time = model.sent_at.strftime('%Y-%m-%d  %H:%M')

        # message pipeline
        await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type':'sender',
                    'message':message,
                    'username':username,
                    'time':time
                    })

        # dashboard notification pipeline
#        dashboard_layer = await sync_to_async(get_channel_layer)()
#        await dashboard_layer.group_send(
#                self.room_group_name,
#                {
#                    'type': 'user_send_notification',
#                    'message': message,
#                    'username': username,
#                    'time': time
#                    }
#                )


    async def sender(self,event):
        await self.send(text_data = json.dumps({ 
                                                'message':event['message'],
                                                'username':event['username'],
                                                'time':event['time']
                                                }))
