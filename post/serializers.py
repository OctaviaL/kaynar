from rest_framework import serializers
from post.models import *


class PetPostSerializers(serializers.ModelSerializer):

    class Meta:
        model = PetPost
        fields = '__all__'
   
   
    def to_representation(self, instance):
            representation = super().to_representation(instance)
            representation['images'] = PetImageSerializers(instance.images.all(), many=True, context=self.context).data
            return representation 
  

class PetImageSerializers(serializers.ModelSerializer):


    class Meta:
        model = PetImage
        fields = '__all__'

   
    
