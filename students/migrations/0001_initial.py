# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('university_id', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('twitter_id', models.CharField(default=b'', max_length=50, blank=True)),
            ],
        ),
    ]
