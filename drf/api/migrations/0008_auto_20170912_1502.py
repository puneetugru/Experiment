# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-12 15:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20170912_1230'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='school',
            options={'ordering': ('id',)},
        ),
    ]