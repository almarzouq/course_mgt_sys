# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0005_appointment_instructor'),
        ('courses', '0008_auto_20151201_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(blank=True, default=1, to='instructors.Instructor'),
            preserve_default=False,
        ),
    ]
