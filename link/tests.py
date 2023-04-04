from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from shortlink.settings import SHORT_URL_SIZE
from .models import Link

factory = APITestCase()


class LinkTest(APITestCase):

    def test_create_link(self):
        url = reverse('create_link')
        data = {'url': 'https://www.django-rest-framework.org/api-guide/testing/'}
        response1 = self.client.post(url, data, format='json')
        response2 = self.client.post(url, data, format='json')
        self.assertEqual(response1.json()['post']['short_url'], response2.json()['post']['short_url'])
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response1.json()['post']['short_url']), SHORT_URL_SIZE)
        self.assertEqual(Link.objects.count(), 1)



