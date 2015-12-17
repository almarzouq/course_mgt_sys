# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '__first__'),
        ('students', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('time_attended', models.DateTimeField(auto_now=True, null=True)),
                ('attended', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('tag', models.CharField(max_length=20)),
                ('academic_year', models.CharField(max_length=120, help_text='E.g.: 2015/2016')),
                ('semester', models.CharField(max_length=2, choices=[('FA', 'Fall'), ('SP', 'Spring'), ('SU', 'Summer')])),
                ('days', models.CharField(max_length=3, choices=[('24', 'Mondays/Wednesdays'), ('135', 'Sundays/Tuesdays/Thursdays'), ('E', 'Everyday')])),
                ('completed', models.BooleanField(default=False)),
                ('syllabusURL', models.URLField(blank=True, null=True)),
                ('student_registration_open', models.BooleanField(default=True)),
                ('instructor', models.ForeignKey(to='instructors.Instructor', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseAnnouncement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('comment', models.TextField(blank=True)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(to='courses.Course')),
            ],
        ),
        migrations.CreateModel(
            name='CourseStudent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('course', models.ForeignKey(to='courses.Course')),
                ('student', models.ForeignKey(to='students.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('value', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='GradeColumn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.TextField(blank=True)),
                ('course', models.ForeignKey(to='courses.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('time_of_lecture', models.DateTimeField(auto_now=True)),
                ('number_of_students', models.BigIntegerField(blank=True, null=True)),
                ('course', models.ForeignKey(to='courses.Course')),
            ],
        ),
        migrations.AddField(
            model_name='grade',
            name='column',
            field=models.ForeignKey(to='courses.GradeColumn'),
        ),
        migrations.AddField(
            model_name='grade',
            name='student',
            field=models.ForeignKey(to='students.Student'),
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(to='students.Student', through='courses.CourseStudent'),
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
        migrations.AlterUniqueTogether(
            name='coursestudent',
            unique_together=set([('course', 'student')]),
        ),
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together=set([('lecture', 'student')]),
        ),
    ]
