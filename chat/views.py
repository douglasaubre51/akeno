import json
from django.shortcuts import render,redirect

from authentication.models import Worker
from .models import ChannelGroup,Message


# Create your views here.
def get_chat_page(request,worker_id,room_guid):
    # load chat page
    if request.method == 'GET':
        # load all messages
        worker = Worker.objects.get(id = worker_id)
        user = request.user

        user_messages = list(user.channel_groups.get(channel_guid = room_guid).messages.all().values())

        context = {
                'room_guid': room_guid,
                'messages': user_messages,
                'username': user.username
                }
        return render(request,'chat.html',context)
