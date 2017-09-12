# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-12 12:30
from __future__ import unicode_literals

from django.db import migrations

def create_initial_schools(apps, schema_editor):
    School = apps.get_model('api', 'School')

    School(name='SVHS', description='S.V.H.S').save()
    School(name='PENHS', description='P.E.N.H.S').save()
    School(name='GBHS', description='G.B.H.S').save()
    School(name='BGS', description='B.G.S').save()
    School(name='Little Angel', description='Little Angel').save()
    School(name='CTS', description='C.T.S').save()

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20170912_1136'),
    ]

    operations = [
        migrations.RunPython(create_initial_schools),
    ]
