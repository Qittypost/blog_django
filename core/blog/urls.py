from django.urls import path
from . import views

urlpatterns = [
    path('get-posts', views.get_posts, name='get-posts')
]
