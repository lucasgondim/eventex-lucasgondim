# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-05 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('start', models.TimeField()),
                ('description', models.TextField()),
                ('speakers', models.ManyToManyField(to='core.Speaker')),
            ],
        ),
    ]