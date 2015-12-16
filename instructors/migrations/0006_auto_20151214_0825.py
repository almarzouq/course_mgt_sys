# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0005_appointment_instructor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='approved',
            field=models.NullBooleanField(),
        ),
    ]
