# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-06 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psw', '0002_auto_20160105_1517'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('userLogin', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=24)),
            ],
            options={
                'verbose_name': 'Klient',
                'verbose_name_plural': 'Klienci',
            },
        ),
        migrations.AlterField(
            model_name='commands',
            name='ip',
            field=models.CharField(max_length=50, verbose_name='IP'),
        ),
        migrations.AlterField(
            model_name='commands',
            name='quote',
            field=models.IntegerField(verbose_name='Quote'),
        ),
        migrations.AlterField(
            model_name='commands',
            name='ram',
            field=models.IntegerField(verbose_name='Ram'),
        ),
        migrations.AlterField(
            model_name='commands',
            name='system',
            field=models.CharField(max_length=50, verbose_name='System'),
        ),
    ]
