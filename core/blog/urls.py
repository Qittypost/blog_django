from django.urls import path
from . import views

urlpatterns = [
    path('get-posts', views.get_posts, name='get-posts'),
    path('post/<int:pk>', views.post_details, name='post'),
    path('author_posts/<int:pk>', views.author_posts, name='posts')
]
