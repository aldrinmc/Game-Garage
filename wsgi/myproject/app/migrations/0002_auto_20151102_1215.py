# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 2, 12, 15, 15, 395718, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='game_request',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 2, 12, 15, 15, 397376, tzinfo=utc), null=True, blank=True),
        ),
    ]
