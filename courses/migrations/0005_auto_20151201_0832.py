# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_gradecolumn_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(to='students.Student', null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='syllabusURL',
            field=models.URLField(null=True),
        ),
    ]
