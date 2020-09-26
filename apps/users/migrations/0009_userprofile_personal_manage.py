# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-08-30 16:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20190830_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='personal_manage',
            field=models.CharField(choices=[('my_info', '我的信息'), ('my_courses', '我的课程'), ('my_fav', '我的收藏'), ('my_message', '我的消息')], default='my_info', max_length=50, verbose_name='个人中心类别'),
        ),
    ]
