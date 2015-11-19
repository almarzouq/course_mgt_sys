# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('date_time', models.DateTimeField()),
                ('reason', models.TextField(default=b'')),
                ('email', models.EmailField(max_length=254)),
                ('twitter_id', models.CharField(default=b'', max_length=50, blank=True)),
                ('phone', models.CharField(default=b'', max_length=20, blank=True)),
                ('approved', models.BooleanField(default=False)),
                ('sent_1st_reminder', models.BooleanField(default=False)),
                ('sent_2nd_reminder', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(default=b'', max_length=20, blank=True)),
                ('office_hours', models.TextField(default=b'', blank=True)),
                ('department', models.CharField(default=b'', max_length=120, blank=True)),
                ('school', models.CharField(default=b'', max_length=120, blank=True)),
                ('twitter_id', models.CharField(default=b'', max_length=50, blank=True)),
            ],
        ),
    ]
