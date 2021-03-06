# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-19 08:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Время и дата создания')),
                ('primary_url', models.URLField(verbose_name='Начальный URL')),
                ('shorten_url', models.URLField(verbose_name='Сокращенный URL')),
                ('counter', models.PositiveIntegerField(default=0, verbose_name='Количество переходов')),
            ],
            options={
                'verbose_name_plural': 'URLs',
                'verbose_name': 'URL',
            },
        ),
    ]
