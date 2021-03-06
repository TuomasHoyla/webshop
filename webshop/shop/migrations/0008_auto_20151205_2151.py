# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-05 21:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20151205_2148'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basket',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='basket',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterUniqueTogether(
            name='basket',
            unique_together=set([('product', 'order')]),
        ),
    ]
