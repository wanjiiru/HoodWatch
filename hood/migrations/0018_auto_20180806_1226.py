# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-06 12:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0017_auto_20180806_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='hood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hood.Neighbourhood'),
        ),
    ]
