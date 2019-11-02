# Generated by Django 2.2.6 on 2019-11-01 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('tid', models.BigAutoField(max_length=5, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=35)),
                ('phone', models.IntegerField(unique=True)),
                ('address', models.CharField(max_length=500, unique=True)),
                ('designation', models.CharField(max_length=50)),
                ('bloodgroup', models.CharField(max_length=5)),
                ('dateofjoining', models.DateTimeField(blank=True)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
    ]
