from rest_framework import serializers
from post.models import *


class PetPostSerializers(serializers.ModelSerializer):

    class Meta:
        model = PetPost
        fields = '__all__'


class PetImageSerializers(serializers.ModelSerializer):


    class Meta:
        model = PetImage
        fields = '__all__'