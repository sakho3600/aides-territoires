# Generated by Django 2.2.7 on 2019-11-18 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aids', '0085_auto_20191118_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='aid',
            name='contact',
            field=models.TextField(blank=True, verbose_name='Contact'),
        ),
    ]