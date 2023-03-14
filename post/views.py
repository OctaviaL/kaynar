from django.shortcuts import render
from rest_framework import  viewsets, generics
from post.models import *
from post.serializers import *
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response


class PetPostListGenericView(generics.ListAPIView):
    queryset = PetPost.objects.all()
    serializer_class = PetPostSerializers
   

class PetPostModelViewset(viewsets.ModelViewSet):
    queryset = PetPost.objects.all()
    serializer_class = PetPostSerializers
    permission_classes = [IsAdminUser]        


class PetImageListGenericView(generics.ListAPIView):
    queryset = PetImage.objects.all()
    serializer_class = PetImageSerializers


class PetImageModelViewSet(viewsets.ModelViewSet):
    queryset = PetImage.objects.all()
    serializer_class = PetImageSerializers
    permission_classes = [IsAdminUser]

