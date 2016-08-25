# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-16 12:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smartshark', '0021_auto_20160616_1205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.IntegerField()),
                ('status', models.CharField(choices=[('PEND', 'Pending'), ('PROV', 'Dispatched to power-save host'), ('PSUSP', 'Suspended (pending)'), ('RUN', 'Running'), ('USUSP', 'Suspended (running)'), ('SSUSP', 'Suspended (other)'), ('DONE', 'Done'), ('EXIT', 'Exit'), ('UNKWN', 'Unknown'), ('WAIT', 'Waiting'), ('ZOMBI', 'Zombie!!')], max_length=8)),
                ('output_log', models.CharField(max_length=200)),
                ('error_log', models.CharField(max_length=200)),
                ('revision_path', models.CharField(blank=True, max_length=100)),
                ('submission_string', models.CharField(max_length=300)),
            ],
        ),
        migrations.RenameField(
            model_name='pluginexecution',
            old_name='added_at',
            new_name='submitted_at',
        ),
        migrations.RemoveField(
            model_name='pluginexecution',
            name='error_log',
        ),
        migrations.RemoveField(
            model_name='pluginexecution',
            name='job_id',
        ),
        migrations.RemoveField(
            model_name='pluginexecution',
            name='output_log',
        ),
        migrations.RemoveField(
            model_name='pluginexecution',
            name='revision',
        ),
        migrations.RemoveField(
            model_name='pluginexecution',
            name='status',
        ),
        migrations.RemoveField(
            model_name='pluginexecution',
            name='submission_value',
        ),
        migrations.AddField(
            model_name='job',
            name='plugin_execution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smartshark.PluginExecution'),
        ),
    ]