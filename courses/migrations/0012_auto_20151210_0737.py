# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_auto_20151207_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='number_of_students',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='time_of_lecture',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
