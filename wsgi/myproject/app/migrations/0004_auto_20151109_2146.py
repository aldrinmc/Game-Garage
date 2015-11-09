# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20151107_0902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='multimedia',
            name='game',
        ),
        migrations.AddField(
            model_name='game_info',
            name='dlink',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='game_info',
            name='img',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AddField(
            model_name='game_info',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AddField(
            model_name='game_info',
            name='vlink',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 9, 13, 46, 16, 626000, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='game_request',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 9, 13, 46, 16, 627000, tzinfo=utc), null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='Multimedia',
        ),
    ]
