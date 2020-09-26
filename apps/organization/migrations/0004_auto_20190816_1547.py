# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-08-16 15:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20190814_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseorg',
            name='index',
        ),
        migrations.AddField(
            model_name='courseorg',
            name='courses_nums',
            field=models.IntegerField(default=0, verbose_name='课程数'),
        ),
        migrations.AddField(
            model_name='courseorg',
            name='students',
            field=models.IntegerField(default=0, verbose_name='学习人数'),
        ),
    ]
