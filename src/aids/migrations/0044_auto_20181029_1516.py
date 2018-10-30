# Generated by Django 2.1.2 on 2018-10-29 14:16

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aids', '0043_auto_20181026_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aid',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50), blank=True, default=list, size=16, verbose_name='Tags'),
        ),
    ]
