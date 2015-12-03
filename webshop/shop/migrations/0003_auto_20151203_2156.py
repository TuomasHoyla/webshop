# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-03 21:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20151203_2140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='catalog',
            name='amount',
        ),
        migrations.AddField(
            model_name='basket',
            name='name',
            field=models.CharField(default='basketti', max_length=128, unique=True),
        ),
        migrations.AddField(
            model_name='catalog',
            name='name',
            field=models.CharField(default='catalogi', max_length=128, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='product', max_length=128, unique=True),
        ),
    ]
