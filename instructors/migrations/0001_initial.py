# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=120)),
                ('comment', models.TextField(blank=True)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=120)),
                ('date_time', models.DateTimeField()),
                ('reason', models.TextField(default='')),
                ('email', models.EmailField(max_length=254)),
                ('twitter_id', models.CharField(blank=True, default='', max_length=50)),
                ('phone', models.CharField(blank=True, default='', max_length=20)),
                ('approved', models.NullBooleanField()),
                ('sent_1st_reminder', models.BooleanField(default=False)),
                ('sent_2nd_reminder', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, default='', max_length=20)),
                ('office_hours', models.TextField(default='', blank=True)),
                ('department', models.CharField(blank=True, default='', max_length=120)),
                ('school', models.CharField(blank=True, default='', max_length=120)),
                ('twitter_id', models.CharField(blank=True, default='', max_length=50)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='instructor',
            field=models.ForeignKey(to='instructors.Instructor'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='instructor',
            field=models.ForeignKey(to='instructors.Instructor'),
        ),
    ]
