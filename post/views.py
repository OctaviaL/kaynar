from rest_framework import  viewsets, generics
from post.models import *
from post.serializers import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from feedback.models import Like, Rating
from feedback.serializers import RatingSerializer
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from django.db.models import Count
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

class PetsPagePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50


class PetPostListGenericView(generics.ListAPIView):
    queryset = PetPost.objects.all()
    serializer_class = PetPostSerializers
    permission_classes = [AllowAny]

@method_decorator(cache_page(60 * 60), name='dispatch') 
class PetPostModelViewset(viewsets.ModelViewSet):
    queryset = PetPost.objects.all()
    serializer_class = PetPostSerializers
    permission_classes = [IsAuthenticated]        
    pagination_class = PetsPagePagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category', 'gender']
    search_fields = ['category']

    @action(methods=['POST'], detail=True)
    def like(self, request, pk, *args, **kwargs):
        user = request.user
        print(user)
        print(pk)
        like_obj, _ = Like.objects.get_or_create(owner=user, post_id=pk)
        like_obj.is_like = not like_obj.is_like
        like_obj.save()
        status = 'Поглажен'
        if not like_obj.is_like: #m,klfgklgjnhgjndgjnkdg
            status = 'unliked'
        return Response({'status': status})
    
    @action(methods=['POST'], detail=True)
    def rating(self, request, pk, *args, **kwargs):
        serializer = RatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        rating_obj, _ = Rating.objects.get_or_create(owner=request.user, post_id=pk)
        rating_obj.rating = serializer.data['rating']
        rating_obj.save()
        return Response(serializer.data)
    
    @action(methods=['GET'], detail=True)
    def recomendations(self):

        all_ratings = Rating.objects.all()
        grouped_ratings = all_ratings.values('post').annotate(total_votes=Count('id'))
        min_votes = 2
        filtered_ratings = grouped_ratings.filter(total_votes__gte=min_votes)
        top_n_posts = filtered_ratings[:3]
        return Response(top_n_posts)


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    


   

class PetImageListGenericView(generics.ListAPIView):
    queryset = PetImage.objects.all()
    serializer_class = PetImageSerializers
    permission_classes = [AllowAny]

class PetImageModelViewSet(viewsets.ModelViewSet):
    queryset = PetImage.objects.all()
    serializer_class = PetImageSerializers
    pagination_class = PetsPagePagination
    permission_classes = [IsAuthenticated]


