# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-12 22:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='status',
            field=models.CharField(choices=[('s', 'Secret'), ('p', 'Public')], default='p', max_length=1),
            preserve_default=False,
        ),
    ]
