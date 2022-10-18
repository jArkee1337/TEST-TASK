from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Follower
from .serializers import ListByFollowerSerializer, UserOpSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class PostListTests(APITestCase):
    def setUp(self):
        self.first_user = User.objects.create_user(username='oleg_1', password='oleg')
        self.second_user = User.objects.create_user(username='oleg_2', password='oleg')
        self.first_user_token = Token.objects.create(user=self.first_user)
        Follower.objects.create(user=self.second_user, subscriber=self.first_user)
        Follower.objects.create(user=self.first_user, subscriber=self.second_user)

    def test_follower_list_unauth(self):
        url = reverse('followers')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_follower_list_auth(self):
        url = reverse('followers')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.first_user_token.key)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['subscriber']['username'], self.second_user.username)


    def test_create_follower_unauth(self):
        url = reverse('change_follower', kwargs={'pk':1})
        data = {
            'ok':'ok'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_follower_auth(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.first_user_token.key)
        url = reverse('change_follower', kwargs={'pk': User.objects.get(username='oleg_2').id})

        response = self.client.post(url,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(str(Follower.objects.all()[2].user) == self.second_user.username)
        self.assertTrue(str(Follower.objects.all()[2].subscriber) == self.first_user.username)

    def test_delete_follower_unauth(self):
        url = reverse('change_follower', kwargs={'pk': 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_follower_auth(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.first_user_token.key)
        url = reverse('change_follower', kwargs={'pk': User.objects.get(username='oleg_2').id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
