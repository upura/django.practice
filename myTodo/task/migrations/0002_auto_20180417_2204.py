# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-17 22:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]
