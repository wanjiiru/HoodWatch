# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-06 12:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0016_profile_hood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='hood',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='hood.Neighbourhood'),
        ),
        migrations.AlterField(
            model_name='post',
            name='hood',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='hood.Neighbourhood'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='hood',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='hood.Neighbourhood'),
        ),
    ]
