# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_auto_20151210_0737'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='time_attended',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
