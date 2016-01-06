# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-05 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psw', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commands',
            name='ip',
            field=models.CharField(choices=[('1', '192.168.0.10'), ('2', '192.168.0.11')], max_length=50, verbose_name='IP'),
        ),
        migrations.AlterField(
            model_name='commands',
            name='quote',
            field=models.IntegerField(choices=[('1', '5'), ('2', '10'), ('3', '15')], verbose_name='Quote'),
        ),
        migrations.AlterField(
            model_name='commands',
            name='ram',
            field=models.IntegerField(choices=[('1', '64'), ('2', '128'), ('3', '256')], verbose_name='Ram'),
        ),
        migrations.AlterField(
            model_name='commands',
            name='system',
            field=models.CharField(choices=[('U', 'Ubuntu'), ('D', 'Debian')], max_length=50, verbose_name='System'),
        ),
    ]
