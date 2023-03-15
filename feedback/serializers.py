from rest_framework import serializers
from feedback.models import *
# class PostSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Post
#         fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

