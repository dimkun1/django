# Generated by Django 4.2.4 on 2023-09-02 08:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp4', '0008_alter_kicks_kick_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('public_date', models.DateTimeField(auto_now=True)),
                ('category', models.CharField(max_length=100)),
                ('count', models.IntegerField(default=0)),
                ('public', models.BooleanField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp4.author')),
            ],
        ),
        migrations.AlterField(
            model_name='kicks',
            name='kick_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 2, 11, 49, 16, 900996)),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
