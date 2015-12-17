# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_user'),
        ('courses', '0011_auto_20151217_1834'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseStudent',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(to='students.Student', through='courses.CourseStudent'),
        ),
        migrations.AddField(
            model_name='coursestudent',
            name='course',
            field=models.ForeignKey(to='courses.Course'),
        ),
        migrations.AddField(
            model_name='coursestudent',
            name='student',
            field=models.ForeignKey(to='students.Student'),
        ),
        migrations.AlterUniqueTogether(
            name='coursestudent',
            unique_together=set([('course', 'student')]),
        ),
    ]
