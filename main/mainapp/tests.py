from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status

class PostTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword123')
    def test_post_get_authenticated(self):
        self.client.force_authenticate(user=self.user)
        response_get = self.client.get('/api/v1/post')
        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
    def test_post_post_authenticated(self):
        self.client.force_authenticate(user=self.user)
        data = {'title': 'Test Title', 'text': 'Test Text', 'author' : self.user.id}
        response_post = self.client.post('/api/v1/post', data)
        self.assertEqual(response_post.status_code, status.HTTP_201_CREATED)
    def test_post_post_notAuthenticated(self):
        data = {'title': 'Test Title', 'text': 'Test Text', 'author' : self.user.id}
        response_post = self.client.post('/api/v1/post', data)
        self.assertEqual(response_post.status_code, status.HTTP_403_FORBIDDEN)

class CommentTest(TestCase):
    def test_comment_get(self):
        response_get = self.client.get('/api/v1/comment')
        self.assertEqual(response_get.status_code, status.HTTP_200_OK)