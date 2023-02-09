
from django.urls import path, include
from .views import post_detail, render_post
app_name = 'blog'
urlpatterns = [
    
    path('', render_post, name='posts'),
    path('<int:post_id>', post_detail, name='post_detail'),
 
]
