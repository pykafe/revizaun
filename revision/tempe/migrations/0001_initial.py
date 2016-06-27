# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 02:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aldeia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='SubDistrict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subdistricts', to='tempe.District')),
            ],
        ),
        migrations.CreateModel(
            name='Suco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('subdistrict', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sucos', to='tempe.SubDistrict')),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('nationality', models.CharField(max_length=25)),
                ('aldeias', models.ManyToManyField(related_name='visitors', to='tempe.Aldeia')),
            ],
        ),
        migrations.AddField(
            model_name='aldeia',
            name='suco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aldeias', to='tempe.Suco'),
        ),
    ]
