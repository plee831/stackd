# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 23:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('overflow', '0023_auto_20160629_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='overflow.Question'),
        ),
    ]
