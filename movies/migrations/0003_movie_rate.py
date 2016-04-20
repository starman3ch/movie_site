# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_remove_movie_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='rate',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
