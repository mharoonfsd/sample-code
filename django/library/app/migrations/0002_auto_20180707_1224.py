# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-07-07 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookmodel',
            options={'verbose_name': 'Book', 'verbose_name_plural': 'Books'},
        ),
        migrations.AlterModelOptions(
            name='rackmodel',
            options={'verbose_name': 'Rack', 'verbose_name_plural': 'Racks'},
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='published',
            field=models.DateTimeField(),
        ),
    ]
