# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-21 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_coursedetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='owner',
            field=models.CharField(max_length=20),
        ),
    ]
