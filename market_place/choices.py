from django.db import models
from django.utils.translation import gettext_lazy as _

class Status(models.IntegerChoices):

    READY = 1,_('ready')
    ON_PROJECT = 2,_('on project')
    UNAVAILABLE = 3,_('unavailable')

