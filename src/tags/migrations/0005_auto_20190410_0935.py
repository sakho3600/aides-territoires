# Generated by Django 2.2 on 2019-04-10 07:35

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0004_auto_20181115_1003'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='tag',
            name='tags_tag_name_fe221d_gin',
        ),
        migrations.AddIndex(
            model_name='tag',
            index=django.contrib.postgres.indexes.GinIndex(fields=['name'], name='tag_name_trgm', opclasses=['gin_trgm_ops']),
        ),
    ]
