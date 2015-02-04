# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import files.models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0003_file_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='file',
        ),
        migrations.AlterField(
            model_name='file',
            name='created',
            field=models.DateTimeField(default=files.models.created, verbose_name=b'Creation date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='token',
            name='created',
            field=models.DateTimeField(default=files.models.created, verbose_name=b'Creation date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='token',
            name='expires',
            field=models.DateTimeField(default=files.models.expires, verbose_name=b'Expiration date'),
            preserve_default=True,
        ),
    ]
