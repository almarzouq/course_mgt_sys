# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0002_announcement'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='instructor',
            field=models.ForeignKey(default=1, to='instructors.Instructor'),
            preserve_default=False,
        ),
    ]
