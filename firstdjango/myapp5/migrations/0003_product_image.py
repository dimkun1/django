# Generated by Django 4.2.4 on 2023-09-05 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp5', '0002_alter_client_nummer_tel'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to=''),
        ),
    ]
