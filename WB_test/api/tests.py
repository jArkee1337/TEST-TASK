from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Post
from .serializers import PostSerializer, UsersSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class PostListTests(APITestCase):
    def setUp(self):
        self.first_user = User.objects.create_user(username='oleg_1', password='oleg')
        self.second_user = User.objects.create_user(username='oleg_2', password='oleg')
        self.first_user_token = Token.objects.create(user=self.first_user)
        self.first_post = Post.objects.create(title='Python', content="Python is the best language ever",
                                              author=self.first_user)
        self.second_post = Post.objects.create(title='Java', content="I don't think so", author=self.first_user)

    def test_create_post_unauth(self):
        url = reverse('create_post')
        serializer_data = PostSerializer(self.first_post).data
        response = self.client.post(url, serializer_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_post_auth(self):
        url = reverse('create_post')
        serializer_data = PostSerializer(self.first_post).data
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.first_user_token.key)
        response = self.client.post(url, serializer_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.get(pk=3).title, PostSerializer(self.first_post).data['title'])

    def test_list_of_users(self):
        url = reverse('profiles')
        response = self.client.get(url)
        serializer_data = UsersSerializer([self.first_user, self.second_user], many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer_data)
        self.assertTrue(len(response.data[0]['posts']) > len(response.data[1]['posts']) )

    def test_others_users_posts_unauth(self):
        url = reverse('other-users-posts')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_others_users_posts_auth(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.first_user_token.key)
        url = reverse('other-users-posts')
        data = Post.objects.all().exclude(author=self.first_user).order_by('created_at')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(data) == 0)




