# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('computername', models.CharField(max_length=100, verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe5\x90\x8d')),
                ('memory', models.CharField(max_length=100, verbose_name=b'\xe5\x86\x85\xe5\xad\x98')),
                ('state', models.BooleanField(verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'verbose_name': '\u4e2a\u4e3b\u673a',
                'verbose_name_plural': '\u4e3b\u673a\u8868',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=100, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('password', models.CharField(max_length=200, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'verbose_name': '\u4e2a\u7528\u6237',
                'verbose_name_plural': '\u7528\u6237\u8868',
            },
            bases=(models.Model,),
        ),
    ]
