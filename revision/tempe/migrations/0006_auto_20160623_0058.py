# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 00:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tempe', '0005_visitor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitor',
            name='aldeia',
        ),
        migrations.AddField(
            model_name='visitor',
            name='aldeias',
            field=models.ManyToManyField(related_name='visitors', to='tempe.Aldeia'),
        ),
    ]
