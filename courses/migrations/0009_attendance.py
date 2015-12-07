# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20151123_1505'),
        ('courses', '0008_auto_20151201_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lecture', models.CharField(max_length=120)),
                ('time_of_lecture', models.DateTimeField()),
                ('attended', models.BooleanField(default=False)),
                ('course', models.ForeignKey(to='courses.Course')),
                ('student', models.ForeignKey(to='students.Student')),
            ],
        ),
    ]
