# Generated by Django 2.2.6 on 2019-11-06 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0012_auto_20191106_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='petrol_price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='travel',
            name='total_cost',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
