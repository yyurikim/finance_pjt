# Generated by Django 4.2.11 on 2024-05-20 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0003_usersavings_userdeposit'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='is_meaningout',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='saving',
            name='is_meaningout',
            field=models.BooleanField(default=False),
        ),
    ]
