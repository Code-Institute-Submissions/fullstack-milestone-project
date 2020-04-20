# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-20 20:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20200420_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('baby', 'BABY'), ('christening', 'CHRISTENING'), ('communion', 'COMMUNION'), ('engagement', 'ENGAGEMENT'), ('family', 'FAMILY'), ('fathersday', 'FATHERSDAY'), ('fingerprint', 'FINGERPRINT'), ('mothersday', 'MOTHERSDAY'), ('teacher', 'TEACHER'), ('wedding', 'WEDDING')], default='', max_length=30),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]