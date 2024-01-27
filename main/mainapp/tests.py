from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from .models import Post, Comment

class PostTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword123')
        self.client.force_authenticate(user=self.user)
        self.post = Post.objects.create(title="test post", text="test text", author=self.user)
    def test_Post_get(self):
        response = self.client.get('/api/v1/post')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_Post_post(self):
        data = {'title': 'Test Title', 'text': 'Test Text', 'author' : self.user.id}
        response = self.client.post('/api/v1/post', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    def test_Post_delete(self):
        response = self.client.delete(f'/api/v1/post/{self.post.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    def test_Post_put(self):
        data = {'title' : 'changed text', 'text' : 'changed text', 'author': self.user.id}
        response = self.client.put(f'/api/v1/post/{self.post.id}', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_Post_logout_get(self):
        self.client.logout()
        response = self.client.get('/api/v1/post')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CommentTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword123')
        #data_post = {'title' : 'Test Title', 'text' : 'Test Text', 'author':self.user.id}
        self.post = Post.objects.create(title='Test title', text='Test text', author=self.user)
        self.client.force_authenticate(user=self.user)
    def test_comment_get(self):
        response = self.client.get('/api/v1/comment')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_comment_post(self):
        data = {'text' : 'test comment', 'author' : self.user.id, 'post' : self.post.id}
        response = self.client.post('/api/v1/comment', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)