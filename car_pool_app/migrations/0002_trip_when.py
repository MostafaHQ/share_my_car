# Generated by Django 2.2.4 on 2022-10-11 11:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_pool_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='when',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 11, 14, 58, 3, 517796)),
        ),
    ]
