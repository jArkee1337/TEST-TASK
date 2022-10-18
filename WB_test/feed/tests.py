from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Post
from follower.models import Follower
from api.serializers import PostSerializer, UsersSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class FeedTests(APITestCase):

    def setUp(self):
        self.first_user = User.objects.create_user(username='oleg_1', password='oleg')
        self.second_user = User.objects.create_user(username='oleg_2', password='oleg')
        self.first_user_token = Token.objects.create(user=self.first_user)
        self.first_post = Post.objects.create(title='Python', content="Python is the best language ever",
                                              author=self.second_user)
        self.second_post = Post.objects.create(title='Java', content="I don't think so", author=self.second_user)
        Follower.objects.create(user=self.second_user, subscriber=self.first_user)
        Follower.objects.create(user=self.first_user, subscriber=self.second_user)


    def test_feed_list_unauth(self):
        url = reverse('feed')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_feed_list_auth(self):
        url = reverse('feed')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.first_user_token.key)
        response = self.client.get(url)
        data_1 = Post.objects.filter(author__owner__subscriber=self.first_user).order_by('-created_at').select_related(
            'author').get(pk=1)
        data_2 = Post.objects.filter(author__owner__subscriber=self.first_user).order_by('-created_at').select_related(
            'author').get(pk=2)
        serializer_data = PostSerializer([data_2, data_1], many=True).data
        print(serializer_data)
        print(response.data['results'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], serializer_data)