# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20151123_1505'),
        ('courses', '0009_course_instructor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_attended', models.DateTimeField(auto_now=True, null=True)),
                ('attended', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('time_of_lecture', models.DateTimeField(auto_now=True)),
                ('number_of_students', models.BigIntegerField(null=True, blank=True)),
                ('course', models.ForeignKey(to='courses.Course')),
            ],
        ),
        migrations.AddField(
            model_name='attendance',
            name='lecture',
            field=models.ForeignKey(to='courses.Lecture'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(to='students.Student'),
        ),
    ]
