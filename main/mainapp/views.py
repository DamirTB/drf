from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from .permissions import IsOwnerOrReadOnly

class PostAPIList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

class CommentAPIList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer

class PostAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostSerializer

class CommentAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentSerializer