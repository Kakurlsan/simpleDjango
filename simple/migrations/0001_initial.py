# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=48, verbose_name='\u540d\u79f0', db_index=True)),
                ('foreign_name', models.CharField(default=b'', max_length=48, verbose_name='\u5916\u6587\u540d\u79f0', blank=True)),
            ],
            options={
                'db_table': 'publisher',
                'verbose_name': '\u53d1\u884c\u65b9/\u64ad\u51fa\u53f0',
                'verbose_name_plural': '\u53d1\u884c\u65b9/\u64ad\u51fa\u53f0',
            },
            bases=(models.Model,),
        ),
    ]
