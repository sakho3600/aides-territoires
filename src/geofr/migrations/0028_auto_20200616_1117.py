# Generated by Django 2.2.13 on 2020-06-16 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geofr', '0027_update_basins'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perimeter',
            name='contained_in',
            field=models.ManyToManyField(blank=True, related_name='contains', to='geofr.Perimeter', verbose_name='Contained in'),
        ),
    ]