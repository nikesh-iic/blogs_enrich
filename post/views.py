from django.shortcuts import render, redirect, get_object_or_404
from .models import Post


def post_list(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'post_list.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})


def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post(title=title, content=content)
        post.save()
        return redirect('post_detail', post_id=post.id)
    return render(request, 'post_form.html')
