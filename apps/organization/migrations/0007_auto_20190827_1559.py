# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-08-27 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0006_auto_20190827_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='work_position',
            field=models.CharField(max_length=50, verbose_name='公司职位'),
        ),
    ]
