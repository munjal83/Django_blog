# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-06 09:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_auto_20160906_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='blogpost',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.Topic'),
        ),
    ]