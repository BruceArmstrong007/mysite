# Generated by Django 2.2.6 on 2019-11-05 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0006_auto_20191105_1519'),
    ]

    operations = [
        migrations.RenameField(
            model_name='distance',
            old_name='destination',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='distance',
            name='source',
        ),
    ]
