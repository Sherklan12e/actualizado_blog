from django.shortcuts import render, get_list_or_404
from .models import Post

def render_post(request):
    post = Post.objects.all()
    return render(request, 'post.html', {'posts': post})
def post_detail(request, post_id):
    post = get_list_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', {"post": post})
