# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-30 15:06
from __future__ import unicode_literals

from django.db import migrations, models
import smartshark.models


class Migration(migrations.Migration):

    dependencies = [
        ('smartshark', '0025_job_revision_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='submission_string',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='plugin',
            name='archive',
            field=models.FileField(upload_to='uploads/plugins/', validators=[smartshark.models.FileValidator(content_types=('application/x-tar', 'application/octet-stream'), max_size=524288000)]),
        ),
    ]
