from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>', views.PostContent.as_view(), name="post_content"),
    path('like/<slug:slug>', views.PostLike.as_view(), name="post_like"),
    path('write/', views.UserPost.as_view(), name='post_create'),
]
