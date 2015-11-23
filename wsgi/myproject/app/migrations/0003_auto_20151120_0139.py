# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20151116_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='game',
            field=models.ForeignKey(default=1, to='app.Game_info'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 20, 1, 39, 50, 323659, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='game_request',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 20, 1, 39, 50, 324661, tzinfo=utc), null=True, blank=True),
        ),
    ]
