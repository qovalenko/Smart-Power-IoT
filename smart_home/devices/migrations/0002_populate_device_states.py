# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-05 07:45
from __future__ import unicode_literals

from django.db import models, migrations

def populate_device_state(apps, schema_editor):
    DeviceState = apps.get_model("devices","DeviceState")
    ds = DeviceState(state="on")
    ds.save()
    ds = DeviceState(state="off")
    ds.save()

class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_device_state)
    ]