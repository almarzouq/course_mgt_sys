# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20151201_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(to='students.Student', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='syllabusURL',
            field=models.URLField(null=True, blank=True),
        ),
    ]
