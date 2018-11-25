# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-09 21:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('float_plugin', '0002_auto_20180809_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='floatmodel',
            name='float_breakpoint',
            field=models.CharField(choices=[('', 'very small'), ('sm-', 'small'), ('md-', 'medium'), ('lg-', 'large'), ('xl-', 'very large')], default='', help_text='At which bootstrap4 breakpoint should the float behaviour start, starting from smallest.', max_length=256),
        ),
    ]