# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-03 08:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Online',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'online',
            },
        ),
        migrations.AddField(
            model_name='dreamreal',
            name='online',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='firstapp.Online'),
        ),
    ]
