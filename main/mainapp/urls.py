from django.urls import path, include
from . import views

urlpatterns = [
    path('post', views.PostAPIList.as_view(), name="postlist"),
    path('comment', views.CommentAPIList.as_view(), name="commentlist"),
    path('post/<int:pk>', views.PostAPIDetail.as_view(), name="postdetail"),
    path('comment/<int:pk>', views.CommentAPIDetail.as_view(), name="commentdetail"),
]