from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Bulletin_post, Bulletin_comment, Consumer_post, Consumer_comment, Challenge_post, Challenge_comment

# 자유게시판
class BulletinPostSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username')
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Bulletin_post
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at']  # user를 read_only로 설정

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None
    
    def update(self, instance, validated_data):
    # Update the instance with the new validated data
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        if 'image' in validated_data:
            instance.image = validated_data['image']
        instance.save()
        return instance


class BulletinPostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bulletin_post
        fields = ('title', 'content', 'image')


class BulletinPostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bulletin_post
        fields = '__all__'


class BulletinCommentSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Bulletin_comment
        fields = '__all__'
        read_only_fields = ('user', 'created_at', 'updated_at')
    # def update(self, instance, validated_data):
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.save()
    #     return instance

# 소비 게시판
class ConsumerPostSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username')
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Bulletin_post
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at']  # user를 read_only로 설정

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None
    
    def update(self, instance, validated_data):
    # Update the instance with the new validated data
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        if 'image' in validated_data:
            instance.image = validated_data['image']
        instance.save()
        return instance


class ConsumerPostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumer_post
        fields = ('title', 'content', 'image')


class ConsumerPostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumer_post
        fields = '__all__'

class ConsumerCommentSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Consumer_comment
        fields = '__all__'
        read_only_fields = ('user', 'created_at', 'updated_at')


# 챌린지 게시판
class ChallengePostSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username')
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Challenge_post
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at']  # user를 read_only로 설정

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None
    
    def update(self, instance, validated_data):
    # Update the instance with the new validated data
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        if 'image' in validated_data:
            instance.image = validated_data['image']
        instance.save()
        return instance


class ChallengePostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge_post
        fields = ('title', 'content', 'image')


class ChallengePostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge_post
        fields = '__all__'


class ChallengeCommentSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Challenge_comment
        fields = '__all__'
        read_only_fields = ('user', 'created_at', 'updated_at')