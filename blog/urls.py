from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('like/<slug:slug>', views.PostLike.as_view(), name="post_like"),
    path('write/', views.UserPost.as_view(), name='post_create'),
    path('update/<slug:slug>', views.UpdatePost.as_view(), name="post_update"),
    path('<slug:slug>', views.PostContent.as_view(), name="post_content"),
]
