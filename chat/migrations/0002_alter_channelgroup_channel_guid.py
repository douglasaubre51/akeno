# Generated by Django 5.2 on 2025-05-21 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channelgroup',
            name='channel_guid',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
