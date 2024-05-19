# Generated by Django 4.2.11 on 2024-05-19 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('deposit_id', models.AutoField(primary_key=True, serialize=False)),
                ('fin_prdt_cd', models.CharField(max_length=50, unique=True)),
                ('kor_co_nm', models.CharField(max_length=50)),
                ('fin_prdt_nm', models.TextField(max_length=50)),
                ('spcl_cnd', models.TextField(blank=True, null=True)),
                ('join_deny', models.IntegerField(blank=True, null=True)),
                ('join_way', models.TextField(blank=True, null=True)),
                ('etc_note', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Saving',
            fields=[
                ('saving_id', models.AutoField(primary_key=True, serialize=False)),
                ('fin_prdt_nm', models.CharField(max_length=50)),
                ('fin_prdt_cd', models.CharField(max_length=50, unique=True)),
                ('kor_co_nm', models.CharField(max_length=50)),
                ('mtrt_int', models.TextField(blank=True, null=True)),
                ('spcl_cnd', models.TextField(blank=True, null=True)),
                ('join_deny', models.IntegerField(blank=True, null=True)),
                ('etc_note', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Saving_option',
            fields=[
                ('saving_option_id', models.AutoField(primary_key=True, serialize=False)),
                ('fin_prdt_cd', models.CharField(max_length=50)),
                ('intr_rate_type_nm', models.CharField(max_length=2)),
                ('rsrv_type_nm', models.CharField(max_length=10)),
                ('save_trm', models.CharField(max_length=3)),
                ('intr_rate', models.FloatField(null=True)),
                ('intr_rate2', models.FloatField(null=True)),
                ('saving_product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banks.saving')),
            ],
        ),
        migrations.CreateModel(
            name='Deposit_options',
            fields=[
                ('deposit_option_id', models.AutoField(primary_key=True, serialize=False)),
                ('fin_prdt_cd', models.CharField(max_length=50)),
                ('intr_rate_type_nm', models.CharField(max_length=2)),
                ('save_trm', models.IntegerField(max_length=3)),
                ('intr_rate', models.FloatField(null=True)),
                ('intr_rate2', models.FloatField(null=True)),
                ('deposit_product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banks.deposit')),
            ],
        ),
    ]
