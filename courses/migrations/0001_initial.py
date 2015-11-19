# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('tag', models.CharField(max_length=20)),
                ('academic_year', models.CharField(help_text='E.g.: 2015/2016', max_length=120)),
                ('semester', models.CharField(max_length=2, choices=[(b'FA', 'Fall'), (b'SP', 'Spring'), (b'SU', 'Summer')])),
                ('days', models.CharField(max_length=3, choices=[(b'24', 'Mondays/Wednesdays'), (b'135', 'Sundays/Tuesdays/Thursdays'), (b'E', 'Everyday')])),
                ('completed', models.BooleanField(default=False)),
                ('syllabusURL', models.URLField()),
                ('student_registration_open', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.DecimalField(max_digits=5, decimal_places=2)),
                ('column', models.ForeignKey(to='students.Student')),
                ('course', models.ForeignKey(to='courses.Course')),
            ],
        ),
        migrations.CreateModel(
            name='GradeColumn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('total', models.DecimalField(max_digits=5, decimal_places=2)),
                ('course', models.ForeignKey(to='courses.Course')),
            ],
        ),
    ]
