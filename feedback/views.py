from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Like, Comment

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

@login_required
def post_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    action = request.POST.get('action')

    if action == 'like':
        Like.objects.create(post=post, user=request.user)
    elif action == 'unlike':
        Like.objects.filter(post=post, user=request.user).delete()

    return redirect('post_detail', pk=post.pk)

@login_required
def post_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        content = request.POST.get('content')
        Comment.objects.create(post=post, author=request.user, content=content)
        messages.success(request, 'Your comment was added.')
        return redirect('post_detail', pk=post.pk)

    return render(request, 'post_detail.html', {'post': post})

