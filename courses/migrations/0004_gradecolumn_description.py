# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='gradecolumn',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
