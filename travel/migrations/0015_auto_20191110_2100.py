# Generated by Django 2.2.6 on 2019-11-10 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0014_auto_20191106_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distance',
            name='address',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
