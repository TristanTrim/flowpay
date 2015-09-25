# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0003_auto_20150920_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='inputChannel',
            field=models.OneToOneField(related_name='input_user', default=0, to='channel.channel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='outputChannel',
            field=models.OneToOneField(related_name='output_user', default=0, to='channel.channel'),
            preserve_default=False,
        ),
    ]
