# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0002_announcement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='phone',
            field=models.CharField(max_length=20, blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='reason',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='twitter_id',
            field=models.CharField(max_length=50, blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='department',
            field=models.CharField(max_length=120, blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='office_hours',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='phone',
            field=models.CharField(max_length=20, blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='school',
            field=models.CharField(max_length=120, blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='twitter_id',
            field=models.CharField(max_length=50, blank=True, default=''),
        ),
    ]
