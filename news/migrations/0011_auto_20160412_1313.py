# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_auto_20160412_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='asfasf',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AlterField(
            model_name='projects',
            name='img',
            field=models.ImageField(upload_to='photos'),
        ),
    ]
