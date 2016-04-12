# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='new_field',
            field=models.CharField(max_length=140, default='SOME STRING'),
        ),
    ]
