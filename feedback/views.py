
from django.shortcuts import render, get_object_or_404, redirect
from .models import  *
from feedback.serializers import CommentSerializer,FavoriteSerializer
from rest_framework.viewsets import  GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated


class CommentModelViewSet(mixins.CreateModelMixin, #создает
                   mixins.RetrieveModelMixin, #
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


def add_comment_to_post(request, pk):
    post = get_object_or_404(PetPost, pk=pk)
    if request.method == 'POST':
        form = CommentSerializer(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('yourapp:post_detail', pk=post.pk)
    else:
        form = CommentSerializer()
    return render(request, 'yourapp/add_comment_to_post.html', {'form': form})





class FavoriteModelViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        return queryset
