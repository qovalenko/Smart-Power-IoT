# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-04 11:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(max_length=200)),
                ('serial_num', models.CharField(max_length=200)),
                ('ip_addr', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='DeviceState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='current_state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.DeviceState'),
        ),
        migrations.AddField(
            model_name='device',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.Location'),
        ),
    ]
