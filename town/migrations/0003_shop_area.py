# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('town', '0002_shop'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='area',
            field=models.ForeignKey(default=1, verbose_name='所属の町', to='town.Town'),
            preserve_default=False,
        ),
    ]
