# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import app.models
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('first_name', models.CharField(max_length=30, null=True, blank=True)),
                ('last_name', models.CharField(max_length=30, null=True, blank=True)),
                ('contact_number', models.CharField(max_length=30, null=True, blank=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField(max_length=300)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2015, 12, 3, 8, 58, 22, 744281, tzinfo=utc), null=True, blank=True)),
                ('published_date', models.DateTimeField(null=True, blank=True)),
                ('rating', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Game_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=30)),
                ('description', models.TextField(max_length=3000)),
                ('redirectlink', models.CharField(max_length=250, null=True, blank=True)),
                ('youtubelink', models.CharField(max_length=250, null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('category_id', models.ManyToManyField(to='app.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Game_request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2015, 12, 3, 8, 58, 22, 746080, tzinfo=utc), null=True, blank=True)),
                ('published_date', models.DateTimeField(null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('thumbnail', models.ImageField(upload_to=app.models.generate_filename)),
                ('img1', models.ImageField(upload_to=app.models.generate_filename)),
                ('img2', models.ImageField(upload_to=app.models.generate_filename)),
                ('img3', models.ImageField(upload_to=app.models.generate_filename)),
                ('img4', models.ImageField(upload_to=app.models.generate_filename)),
                ('game_id', models.ForeignKey(blank=True, to='app.Game_info', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mobile_requirement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('compatible', models.CharField(default=b'', max_length=50, null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PC_requirement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('os_min', models.CharField(default=b'', max_length=50, null=True, blank=True)),
                ('processor_min', models.CharField(default=b'', max_length=50, null=True, blank=True)),
                ('memory_min', models.CharField(default=b'', max_length=50, null=True, blank=True)),
                ('graphics_min', models.CharField(default=b'', max_length=50, null=True, blank=True)),
                ('directx_min', models.CharField(default=b'', max_length=50, null=True, blank=True)),
                ('harddrive_min', models.CharField(default=b'', max_length=50, null=True, blank=True)),
                ('os_rec', models.CharField(default=b'', max_length=50, null=True, blank=True)),
                ('processor_rec', models.CharField(default=b'', max_length=50, null=True, blank=True)),
                ('memory_rec', models.CharField(default=b'', max_length=50, null=True, blank=True)),
                ('graphics_rec', models.CharField(default=b'', max_length=50, null=True, blank=True)),
                ('directx_rec', models.CharField(default=b'', max_length=50, null=True, blank=True)),
                ('harddrive_rec', models.CharField(default=b'', max_length=50, null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='game_info',
            name='mobile_req',
            field=models.OneToOneField(null=True, blank=True, to='app.Mobile_requirement'),
        ),
        migrations.AddField(
            model_name='game_info',
            name='pc_req',
            field=models.OneToOneField(null=True, blank=True, to='app.PC_requirement'),
        ),
        migrations.AddField(
            model_name='game_info',
            name='platform',
            field=models.ManyToManyField(to='app.Platform', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='game',
            field=models.ForeignKey(default=1, to='app.Game_info'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
