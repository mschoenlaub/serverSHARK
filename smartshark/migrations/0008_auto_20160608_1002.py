# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-08 08:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smartshark', '0007_auto_20160608_1001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plugin',
            old_name='zip',
            new_name='archive',
        ),
    ]
