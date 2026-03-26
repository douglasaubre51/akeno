from django.db import models
from django.utils.text import slugify

from authentication.models import Account


# Create your choices here.
PROJECT_STATUS = {
        'OPEN': 'Open',
        'SUSPENDED': 'Suspended',
        'CLOSED': 'Closed',
        'EXPIRED': 'Expired',
        'CANCELLED': 'Cancelled'
        }


# Create your models here.
class Project(models.Model):
    account = models.ForeignKey(
            Account,
            related_name = 'projects',
            on_delete = models.CASCADE
            )

    title = models.CharField(max_length=25)

    slug = slugify(title)

    short_description = models.CharField(
            max_length=40,
            null=True
            )
    description = models.TextField()

    no_of_days = models.IntegerField(default=5)

    project_expiry_date = models.DateField()

    reward = models.IntegerField()

    status = models.CharField(
            max_length = 10,
            choices = PROJECT_STATUS,
            default = PROJECT_STATUS['OPEN']
            )
