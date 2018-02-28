# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-28 04:17
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('iban', '0003_auto_20180227_2049'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ibanaccount',
            options={'ordering': ['created_at'], 'verbose_name_plural': 'IBAN accounts'},
        ),
        migrations.AlterField(
            model_name='ibanaccount',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('dc98dfd5-3e0f-4a1a-afc5-23417e3fb01b'), editable=False),
        ),
    ]
