from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.conf import settings

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    # def get_profile_img_url(self, obj):
    #     request = self.context.get('request')
    #     return request.build_absolute_uri(obj.profile_img.url)

class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_type']

class UserUpdateSerializer(serializers.ModelSerializer):
    salary = serializers.ChoiceField(choices=[
        ('200', '200만원 이하'),
        ('300', '201만원 ~ 300만원'),
        ('400', '301만원 ~ 400만원'),
        ('500', '401만원 ~ 500만원'),
        ('600', '501만원 ~ 600만원'),
        ('601', '601만원 이상'),
    ], required=False)
    
    class Meta:
        model = User
        fields = ['name', 'email', 'first_name', 'last_name', 'profile_img', 'age', 'gender', 'job', 'salary', 'favorite_bank']
    
    profile_img = serializers.ImageField(required=False)
    age = serializers.IntegerField(required=False)
    gender = serializers.CharField(required=False)
    job = serializers.CharField(required=False)
    salary = serializers.CharField(required=False)
    favorite_bank = serializers.CharField(required=False)
