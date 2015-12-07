# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_attendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lecture', models.CharField(max_length=120)),
                ('time_of_lecture', models.DateTimeField()),
                ('course', models.ForeignKey(to='courses.Course')),
            ],
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='course',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='time_of_lecture',
        ),
        migrations.AlterField(
            model_name='attendance',
            name='lecture',
            field=models.ForeignKey(to='courses.Lecture'),
        ),
    ]
