# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 20:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('motorcycles', '0004_auto_20170906_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statusmotorcyclepart',
            name='entry_order',
        ),
        migrations.AddField(
            model_name='statusmotorcyclepart',
            name='motorcycle_damages',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='motorcycles.MotorcycleDamages'),
            preserve_default=False,
        ),
    ]