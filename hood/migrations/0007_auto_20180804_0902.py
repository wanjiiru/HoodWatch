# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-04 09:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0006_auto_20180804_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
