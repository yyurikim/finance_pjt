from django.db import models

class ExchangeRates(models.Model):
  cur_unit = models.CharField(max_length=10)
  cur_nm = models.CharField(max_length=30)
  ttb = models.FloatField()
  tts = models.FloatField()
  deal_bas_r = models.FloatField()
  bkpr = models.CharField(max_length=15)
  yy_efee_r = models.CharField(max_length=15)
  ten_dd_efee_r = models.CharField(max_length=15)
  kftc_deal_bas_r = models.CharField(max_length=15)
  kftc_bkpr = models.CharField(max_length=15)