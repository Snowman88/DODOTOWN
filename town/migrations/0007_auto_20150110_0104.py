# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('town', '0006_item_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='item',
            field=models.OneToOneField(to='town.Item'),
            preserve_default=True,
        ),
    ]
