# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-18 01:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tempe', '0002_subdistrict'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('subdistrict', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tempe.SubDistrict')),
            ],
        ),
    ]
