from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostAPIList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentAPIList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class PostAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = CommentSerializer