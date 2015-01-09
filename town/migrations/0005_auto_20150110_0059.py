# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('town', '0004_auto_20150109_2338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopitem',
            name='shop',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='shop_item',
        ),
        migrations.DeleteModel(
            name='ShopItem',
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
    ]
