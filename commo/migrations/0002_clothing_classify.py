# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothing',
            name='classify',
            field=models.ForeignKey(blank=True, to='commo.Classify', null=True),
        ),
    ]
