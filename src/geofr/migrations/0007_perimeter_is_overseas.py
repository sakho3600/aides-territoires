# Generated by Django 2.1.1 on 2018-09-06 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geofr', '0006_auto_20180905_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='perimeter',
            name='is_overseas',
            field=models.BooleanField(default=False, verbose_name='Is overseas?'),
        ),
    ]
