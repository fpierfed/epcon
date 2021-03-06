# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-02-17 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p3', '0006_remove_p3talk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketconference',
            name='shirt_size',
            field=models.CharField(choices=[(None, 'Please select your shirt size!'), ('fs', 'S (fitted cut)'), ('fm', 'M (fitted cut)'), ('fl', 'L (fitted cut)'), ('fxl', 'XL (fitted cut)'), ('fxxl', 'XXL (fitted cut)'), ('fxxxl', '3XL (fitted cut)'), ('s', 'S (straight cut)'), ('m', 'M (straight cut)'), ('l', 'L (straight cut)'), ('xl', 'XL (straight cut)'), ('xxl', 'XXL (straight cut)'), ('xxxl', '3XL (straight cut)'), ('xxxxl', '4XL (straight cut)')], default=None, max_length=5, null=True),
        ),
    ]
