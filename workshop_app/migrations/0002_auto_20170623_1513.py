# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-23 09:43
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='department',
            field=models.CharField(choices=[('computer engineering', 'Computer Science'), ('information technology', 'Information Technology'), ('civil engineering', 'Civil Engineering'), ('electrical engineering', 'Electrical Engineering'), ('mechanical engineering', 'Mechanical Engineering'), ('chemical engineering', 'Chemical Engineering'), ('aerospace engineering', 'Aerospace Engineering'), ('biosciences and bioengineering', 'Biosciences and  BioEngineering'), ('electronics', 'Electronics'), ('energy science and engineering', 'Energy Science and Engineering'), ('others', 'Others')], max_length=150),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message="Phone number must be entered                                 in the format: '9999999999'.                                Up to 10 digits allowed.", regex='^.{10}$')]),
        ),
    ]