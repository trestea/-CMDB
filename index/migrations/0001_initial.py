# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-08 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JifangGroup',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('jifang', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Quyu',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('quyu', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('caption', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=64)),
            ],
        ),
    ]
