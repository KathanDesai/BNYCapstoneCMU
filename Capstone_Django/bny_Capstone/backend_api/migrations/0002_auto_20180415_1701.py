# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-15 21:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='fields',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='node',
            name='name',
            field=models.TextField(default=''),
        ),
    ]