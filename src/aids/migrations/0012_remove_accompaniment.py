# Generated by Django 2.1 on 2018-08-28 13:41

from django.db import migrations


def remove_accompaniment_values(apps, schema_editor):
    """Replace "accompaniment" in aid types with "guidance"."""
    Aid = apps.get_model('aids', 'Aid')
    aids = Aid.objects.all().filter(aid_types__contains=['accompaniment'])
    for aid in aids:
        aid.aid_types.remove('accompaniment')
        aid.aid_types.append('guidance')
        aid.save()


class Migration(migrations.Migration):

    dependencies = [
        ('aids', '0011_auto_20180828_1427'),
    ]

    operations = [
        migrations.RunPython(remove_accompaniment_values)
    ]
