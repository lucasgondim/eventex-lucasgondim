# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-23 21:20
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0003_auto_20160916_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='hashId',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
