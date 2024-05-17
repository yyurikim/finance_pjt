from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, Comment


# class PostSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Post
#         fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username')
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Post
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
        instance.category = validated_data.get('category', instance.category)
        if 'image' in validated_data:
            instance.image = validated_data['image']
        instance.save()
        return instance


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'image')


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user', 'post',)