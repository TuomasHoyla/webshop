# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-04 09:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20151204_0929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='num_stars',
        ),
        migrations.RemoveField(
            model_name='catalog',
            name='num_stars',
        ),
    ]
