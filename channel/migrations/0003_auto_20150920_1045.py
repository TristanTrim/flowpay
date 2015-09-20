# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0002_auto_20150916_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='input',
            name='destinations',
            field=models.ManyToManyField(to='channel.output'),
        ),
        migrations.AddField(
            model_name='output',
            name='origins',
            field=models.ManyToManyField(to='channel.input'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='channels',
            field=models.ManyToManyField(to='channel.channel'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='outputs',
            field=models.ManyToManyField(to='channel.output'),
        ),
    ]
