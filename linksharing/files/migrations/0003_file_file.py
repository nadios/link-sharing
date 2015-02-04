# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0002_file_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='file',
            field=models.FileField(default=None, upload_to=b'documents/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]
