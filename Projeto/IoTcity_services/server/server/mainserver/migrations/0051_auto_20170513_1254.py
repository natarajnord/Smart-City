# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-13 12:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainserver', '0050_auto_20170507_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreport',
            name='attach',
            field=models.ManyToManyField(blank=True, to='mainserver.ReportAttach'),
        ),
    ]
