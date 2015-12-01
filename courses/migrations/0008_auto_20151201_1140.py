# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20151123_1505'),
        ('courses', '0007_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grade',
            name='course',
        ),
        migrations.AddField(
            model_name='grade',
            name='student',
            field=models.ForeignKey(default=1, to='students.Student'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='grade',
            name='column',
            field=models.ForeignKey(to='courses.GradeColumn'),
        ),
    ]
