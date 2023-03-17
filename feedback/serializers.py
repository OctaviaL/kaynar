from rest_framework import serializers
from feedback.models import *
from feedback.models import Favorite


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

  

class FavoriteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Favorite
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    rating = serializers.CharField()

    class Meta:
        model = Rating 
        fields = ('rating', )

