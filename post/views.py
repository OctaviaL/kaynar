from django.shortcuts import render
from rest_framework import  viewsets
from post.models import *
from post.serializers import *
from rest_framework.permissions import IsAdminUser

class PetPostModelViewset(viewsets.ModelViewSet):
    queryset = PetPost.objects.all()
    serializer_class = PetPostSerializers
    # permission_classes = [IsAdminUser]


class PetImageModelViewSet(viewsets.ModelViewSet):
    queryset = PetImage.objects.all()
    serializer_class = PetImageSerializers
    # permission_classes = [IsAdminUser]


