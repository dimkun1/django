# Generated by Django 4.2.4 on 2023-09-05 19:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp4', '0018_alter_kicks_kick_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kicks',
            name='kick_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 5, 22, 40, 43, 719772)),
        ),
    ]