from channels.generic.websocket import AsyncWebsocketConsumer

from chat.models import ChannelGroup


class DashboardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # fetch room guid from re_path
        self.room_guid = self.scope[ 'url_route' ][ 'kwargs' ][ 'room_guid' ]
        print(f'room_guid : {self.room_guid}')

        # add user to group
        await self.channel_layer.group_add(
                self.room_guid,
                self.channel_name
                )

        # accept connection
        await self.accept()


    async def disconnect(self,close_code):
        # kick user from group
        await self.channel_layer.group_discard(
                self.room_guid,
                self.channel_name
                )


    # dashboard notification pipeline
    # called from chat consumers.py
    async def user_send_notification(self,e):
        print('user send notifications')

        json_payload = json.dumps({
            'message':e['message'],
            'username':e['username'],
            'time':e['time']
            })


        await self.send(text_data = json_payload)
