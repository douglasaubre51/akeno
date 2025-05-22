from django.db import models

from authentication.models import Account


# Create your models here.
class ChannelGroup(models.Model):
    channel_guid = models.CharField(
            max_length = 50
            )

    account = models.ForeignKey(
            Account,
            related_name = 'channel_groups',
            on_delete = models.CASCADE
            )


class Message(models.Model):
    channel_group = models.ForeignKey(
            ChannelGroup,
            on_delete = models.CASCADE,
            related_name = 'messages'
            )

    sender_name = models.CharField(max_length = 50)

    text = models.CharField(max_length = 255)

    sent_at = models.DateTimeField(auto_now_add = True)
