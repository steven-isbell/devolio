# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-05 20:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_responsreaction'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ResponsReaction',
            new_name='ResponseReaction',
        ),
    ]
