# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20151109_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 9, 13, 49, 18, 606000, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='game_request',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 9, 13, 49, 18, 607000, tzinfo=utc), null=True, blank=True),
        ),
    ]
