
from django.shortcuts import render, get_object_or_404, redirect
from .models import  Comment
from feedback.serializers import CommentSerializer
from django.utils import timezone
from post.models import PetPost
from rest_framework.viewsets import ModelViewSet, GenericViewSet
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