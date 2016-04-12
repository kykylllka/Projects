# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_projects_new_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='new_field',
        ),
        migrations.AddField(
            model_name='projects',
            name='img',
            field=models.ImageField(default='img', upload_to='img/'),
        ),
    ]
