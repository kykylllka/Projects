# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20160412_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='img',
            field=models.ImageField(upload_to='media/', default=''),
        ),
    ]
