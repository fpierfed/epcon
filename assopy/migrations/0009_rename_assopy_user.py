# Generated by Django 1.11.16 on 2018-10-27 10:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('assopy', '0008_remove_user_oauth_info_model'),
        ('p3', '0002_remove_unused_models'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='AssopyUser',
        ),
    ]
