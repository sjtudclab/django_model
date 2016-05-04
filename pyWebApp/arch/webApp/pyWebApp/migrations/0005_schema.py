# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160413143217 on 2016-04-29 04:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyWebApp', '0004_auto_20160429_1237'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('tenantId', models.CharField(default=b'0000000000', max_length=14, unique=True)),
                ('capacity', models.IntegerField(default=0)),
                ('registertime', models.DateField(default=datetime.date.today)),
                ('lifetime', models.IntegerField(default=0)),
                ('isolation', models.SmallIntegerField(default=0)),
                ('status', models.SmallIntegerField(default=0)),
            ],
        ),
    ]