# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_auto_20151215_0838'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together=set([('lecture', 'student')]),
        ),
    ]
