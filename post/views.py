from django.shortcuts import render
from rest_framework import  viewsets, generics
from post.models import *
from post.serializers import *
from rest_framework.permissions import IsAdminUser
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class PetsPagePagination(PageNumberPagination):
    page_size = 20
    page_query_param = 'page_size'
    max_page_size = 100



class PetPostListGenericView(generics.ListAPIView):
    queryset = PetPost.objects.all()
    serializer_class = PetPostSerializers
    
   
class PetPostModelViewset(viewsets.ModelViewSet):
    queryset = PetPost.objects.all()
    serializer_class = PetPostSerializers
    permission_classes = [IsAdminUser] 
    pagination_class = PetsPagePagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category', 'gender']
    search_fields = ['category']




class PetImageListGenericView(generics.ListAPIView):
    queryset = PetImage.objects.all()
    serializer_class = PetImageSerializers



class PetImageModelViewSet(viewsets.ModelViewSet):
    queryset = PetImage.objects.all()
    serializer_class = PetImageSerializers
    pagination_class = PetsPagePagination
    permission_classes = [IsAdminUser]



