# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 23:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_remove_address_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='first_name',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]