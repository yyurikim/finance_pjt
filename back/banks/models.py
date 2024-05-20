from django.db import models
from django.conf import settings

# Create your models here.
class Deposit(models.Model) :
    deposit_id = models.AutoField(primary_key=True)
    fin_prdt_cd = models.CharField(max_length=50, unique=True)
    kor_co_nm = models.CharField(max_length=50)
    fin_prdt_nm = models.TextField(max_length=50)
    spcl_cnd = models.TextField(blank=True, null=True)
    join_deny = models.IntegerField(blank=True, null=True)
    join_way = models.TextField(blank=True, null=True)
    etc_note = models.TextField(blank=True, null=True)
    user_deposit = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='user_deposits', blank=True)
    liked_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_deposits', blank=True)


class Deposit_options(models.Model) :
    deposit_option_id = models.AutoField(primary_key=True)
    deposit_product_id = models.ForeignKey(Deposit, on_delete = models.CASCADE)
    fin_prdt_cd = models.CharField(max_length=50)
    intr_rate_type_nm = models.CharField(max_length=2)
    save_trm = models.CharField(max_length=3)
    intr_rate = models.FloatField(null=True)
    intr_rate2 = models.FloatField(null=True)

class Saving(models.Model):
    saving_id = models.AutoField(primary_key=True)
    fin_prdt_nm = models.CharField(max_length=50)
    fin_prdt_cd  = models.CharField(max_length=50, unique=True)
    kor_co_nm = models.CharField(max_length=50)
    mtrt_int = models.TextField(blank=True, null=True)
    spcl_cnd = models.TextField(blank=True, null=True)
    join_deny = models.IntegerField(blank=True, null=True)
    etc_note = models.TextField(blank=True, null=True)
    user_saving = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='user_savings', blank=True)
    liked_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_savings', blank=True)

class Saving_option(models.Model):
    saving_option_id = models.AutoField(primary_key=True)
    saving_product_id = models.ForeignKey(Saving, on_delete=models.CASCADE)
    fin_prdt_cd = models.CharField(max_length=50)
    intr_rate_type_nm = models.CharField(max_length=2)
    rsrv_type_nm = models.CharField(max_length=10)
    save_trm = models.CharField(max_length=3)
    intr_rate = models.FloatField(null=True)
    intr_rate2 = models.FloatField(null=True)
