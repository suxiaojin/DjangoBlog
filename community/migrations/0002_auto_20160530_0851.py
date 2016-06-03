# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 08:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='is_publised',
            new_name='is_published',
        ),
        migrations.AlterField(
            model_name='post',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='attachments', verbose_name='附件'),
        ),
    ]