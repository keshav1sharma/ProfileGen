# Generated by Django 4.1.5 on 2023-01-20 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
