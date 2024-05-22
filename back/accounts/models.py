from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
  GENDER_CHOICES = [
    ("남성", "M"),
    ("여성", "F") 
  ]

  BANK_CHOICES = [
    ("SC제일은행", "SC제일은행"),
    ("경남은행", "경남은행"),
    ("광주은행", "광주은행"),
    ("국민은행", "국민은행"),
    ("기업은행", "기업은행"),
    ("농협은행", "농협은행"),
    ("대구은행", "대구은행"),
    ("부산은행", "부산은행"),
    ("수협은행", "수협은행"),
    ("신한은행", "신한은행"),
    ("외환은행", "외환은행"),
    ("우리은행", "우리은행"),
    ("전북은행", "전북은행"),
    ("제주은행", "제주은행"),
    ("카카오뱅크", "카카오뱅크"),
    ("케이뱅크", "케이뱅크"),
    ("토스뱅크", "토스뱅크"),
    ("하나은행", "하나은행"),
    ("한국산업은행", "한국산업은행"),
    ("한국스탠다드차타드은행", "한국스탠다드차타드은행"),
    ("한국시티은행", "한국시티은행"),
    ("기타", "기타")
  ]

  JOB_CHOICES = [
        ('직장인', '직장인'),
        ('학생', '학생'),
        ('자영업', '자영업'),
        ('프리랜서', '프리랜서'),
        ('주부', '주부'),
        ('은퇴자', '은퇴자'),
        ('무직', '무직'),
        ('기타', '기타'),
    ]

  SALARY_CHOICES = [
      ('200', '200만원 이하'),
      ('300', '201만원 ~ 300만원'),
      ('400', '301만원 ~ 400만원'),
      ('500', '401만원 ~ 500만원'),
      ('600', '501만원 ~ 600만원'),
      ('601', '601만원 이상'),
  ]

  user_id = models.AutoField(primary_key=True)
  username = models.CharField(max_length=20, unique=True) # 아이디
  name = models.CharField(max_length=20, null=True, blank=True) # 닉네임 or 이름
  profile_img = models.ImageField(blank=True, upload_to='user/', null=True) # 사용자 프로필 이미지
  email = models.EmailField(max_length=255, blank=True, null=True)
  age = models.IntegerField(blank=True, null=True)
  gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
  job = models.CharField(max_length=10, choices=JOB_CHOICES, blank=True, null=True)
  salary = models.CharField(max_length=10, choices=SALARY_CHOICES, blank=True, null=True)
  favorite_bank = models.CharField(max_length=20, choices=BANK_CHOICES, blank=True, null=True)
  user_type = models.CharField(max_length=10, blank=True, null=True)
  saving_amount = models.IntegerField(blank=True, null=True)
  deposit_amount = models.IntegerField(blank=True, null=True)
  my_goal = models.TextField(blank=True, null=True)


