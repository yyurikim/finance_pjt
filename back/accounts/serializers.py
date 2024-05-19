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
