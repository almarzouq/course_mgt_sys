# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='days',
            field=models.CharField(max_length=3, choices=[('24', 'Mondays/Wednesdays'), ('135', 'Sundays/Tuesdays/Thursdays'), ('E', 'Everyday')]),
        ),
        migrations.AlterField(
            model_name='course',
            name='semester',
            field=models.CharField(max_length=2, choices=[('FA', 'Fall'), ('SP', 'Spring'), ('SU', 'Summer')]),
        ),
    ]
