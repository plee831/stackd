# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overflow', '0015_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
