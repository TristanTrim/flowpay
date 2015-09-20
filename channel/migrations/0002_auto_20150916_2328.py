# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='input',
            name='user',
            field=models.ForeignKey(blank=True, to='channel.user', null=True),
        ),
        migrations.AddField(
            model_name='output',
            name='user',
            field=models.ForeignKey(blank=True, to='channel.user', null=True),
        ),
        migrations.AlterField(
            model_name='channel',
            name='channels',
            field=models.ManyToManyField(to='channel.channel', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='channel',
            name='outputs',
            field=models.ManyToManyField(to='channel.output', null=True, blank=True),
        ),
    ]
