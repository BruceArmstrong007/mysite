# Generated by Django 2.2.6 on 2019-11-10 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0002_auto_20191110_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='log',
            field=models.IntegerField(null=True),
        ),
    ]
