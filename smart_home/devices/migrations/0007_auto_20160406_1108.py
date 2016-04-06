# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-06 09:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0006_auto_20160405_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='ip_addr',
            field=models.GenericIPAddressField(unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='device',
            unique_together=set([('device_name', 'location')]),
        ),
    ]