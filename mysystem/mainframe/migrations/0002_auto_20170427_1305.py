# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainframe', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='computer',
            options={'verbose_name': '\u4e3b\u673a', 'verbose_name_plural': '\u4e3b\u673a\u8868'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '\u7528\u6237', 'verbose_name_plural': '\u7528\u6237\u8868'},
        ),
        migrations.AddField(
            model_name='computer',
            name='user',
            field=models.ForeignKey(related_name='user_computer', default=False, to='mainframe.User'),
            preserve_default=False,
        ),
    ]
