# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='channel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, null=True, blank=True)),
                ('amount', models.FloatField(default=0)),
                ('channels', models.ManyToManyField(to='channel.channel')),
            ],
        ),
        migrations.CreateModel(
            name='destination',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, null=True, blank=True)),
                ('amount', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='source',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, null=True, blank=True)),
                ('amount', models.FloatField(default=0)),
                ('destinations', models.ManyToManyField(to='channel.destination')),
                ('target', models.ForeignKey(to='channel.channel')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, null=True, blank=True)),
                ('givingChannel', models.OneToOneField(related_name='giving_user', to='channel.channel')),
                ('recievingChannel', models.OneToOneField(related_name='recieving_user', to='channel.channel')),
            ],
        ),
        migrations.AddField(
            model_name='source',
            name='user',
            field=models.ForeignKey(blank=True, to='channel.user', null=True),
        ),
        migrations.AddField(
            model_name='destination',
            name='sources',
            field=models.ManyToManyField(to='channel.source'),
        ),
        migrations.AddField(
            model_name='destination',
            name='user',
            field=models.ForeignKey(blank=True, to='channel.user', null=True),
        ),
        migrations.AddField(
            model_name='channel',
            name='destinations',
            field=models.ManyToManyField(to='channel.destination'),
        ),
        migrations.AddField(
            model_name='channel',
            name='sources',
            field=models.ManyToManyField(to='channel.source'),
        ),
    ]
