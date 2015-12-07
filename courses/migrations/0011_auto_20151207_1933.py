# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_auto_20151207_1927'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lecture',
            old_name='lecture',
            new_name='name',
        ),
    ]
