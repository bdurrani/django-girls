# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-21 13:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20171220_1738'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='elvis',
            options={'verbose_name_plural': 'Elvises'},
        ),
        migrations.RenameField(
            model_name='elvis',
            old_name='deviceid',
            new_name='device_id',
        ),
        migrations.RenameField(
            model_name='elvis',
            old_name='hasDisplay',
            new_name='has_display',
        ),
        migrations.RenameField(
            model_name='elvis',
            old_name='deviceip',
            new_name='ip_address',
        ),
        migrations.RenameField(
            model_name='elvis',
            old_name='serialnumber',
            new_name='serial_number',
        ),
    ]
