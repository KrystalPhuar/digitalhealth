# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-02 17:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uclapi', '0003_auto_20170603_1157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='token',
        ),
        migrations.RemoveField(
            model_name='oauthtoken',
            name='private_roombookings',
        ),
        migrations.RemoveField(
            model_name='oauthtoken',
            name='private_timetable',
        ),
        migrations.RemoveField(
            model_name='oauthtoken',
            name='private_uclu',
        ),
        migrations.DeleteModel(
            name='State',
        ),
    ]
