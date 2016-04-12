# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_auto_20160412_1313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='asfasf',
        ),
    ]
