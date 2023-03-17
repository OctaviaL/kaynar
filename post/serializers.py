from rest_framework import serializers
from post.models import *
from post.serializers import *
from feedback.serializers import *

class PetImageSerializers(serializers.ModelSerializer):


    class Meta:
        model = PetImage
        fields = '__all__'

class PetPostSerializers(serializers.ModelSerializer):

    class Meta:
        model = PetPost
        fields = '__all__'
   
   
    def to_representation(self, instance):
            representation = super().to_representation(instance)
            representation['images'] = PetImageSerializers(instance.images.all(), many=True, context=self.context).data
            return representation 
    
    rating = RatingSerializer(many=True, read_only=True)
    images = PetImageSerializers (many=True, read_only=True)
    likes = LikeSerializer(many=True,read_only=True)
    owner = serializers.ReadOnlyField(source='owner.email')

    likes_count = serializers.SerializerMethodField()

    def get_likes_count(self, post):
        return Like.objects.filter(post_id=post).count()


    def create(self, validated_data):
        post = PetPost.objects.create(**validated_data)
        request = self.context.get('request')
        data = request.FILES
        # for i in data.getlist('images'):
        #     PostImage.objects.create(post=post, image=i)
        image_objects = []
        for i in data.getlist('images'):
            image_objects.append(PetImage(post=post,image=i))
        PetImage.objects.bulk_create(image_objects)

        return post




   
    
