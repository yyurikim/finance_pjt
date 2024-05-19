# Generated by Django 4.2.11 on 2024-05-19 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeRates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cur_unit', models.CharField(max_length=10)),
                ('cur_nm', models.CharField(max_length=30)),
                ('ttb', models.FloatField()),
                ('tts', models.FloatField()),
                ('deal_bas_r', models.FloatField()),
                ('bkpr', models.CharField(max_length=15)),
                ('yy_efee_r', models.CharField(max_length=15)),
                ('ten_dd_efee_r', models.CharField(max_length=15)),
                ('kftc_deal_bas_r', models.CharField(max_length=15)),
                ('kftc_bkpr', models.CharField(max_length=15)),
            ],
        ),
    ]
