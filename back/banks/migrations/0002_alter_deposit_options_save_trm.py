# Generated by Django 4.2.11 on 2024-05-19 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit_options',
            name='save_trm',
            field=models.CharField(max_length=3),
        ),
    ]
