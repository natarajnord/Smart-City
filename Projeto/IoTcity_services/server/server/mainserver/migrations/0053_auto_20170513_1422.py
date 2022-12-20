# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-13 14:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainserver', '0052_auto_20170513_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='sensor_type',
            field=models.CharField(choices=[('TE', 'Temperature'), ('AI', 'Air'), ('WA', 'Waste'), ('SO', 'Noise'), ('PE', 'People'), ('IL', 'Lighting'), ('RA', 'Radiation')], max_length=2),
        ),
    ]