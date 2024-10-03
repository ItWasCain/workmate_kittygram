from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from cats.models import Breed, Cat, Rating

User = get_user_model()


class TestApi(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.owner = User.objects.create(username='testUserOwner')
        cls.reader = User.objects.create(username='testUserReader')
        cls.breed = Breed.objects.create(name='Порода1')
        cls.cat = Cat.objects.create(
            name='TestName',
            color='TestColor',
            age='10',
            description='TestDescription',
            breed=cls.breed,
            owner=cls.owner,
        )
        cls.rating = Rating.objects.create(
            user=cls.owner,
            cat=cls.cat,
            rate=5
        )

    def test_url_unauthorized(self):
        urls = (
            ('api:cats-list', None),
            ('api:cats-detail', (self.cat.id,)),
            ('api:breeds-list', None),
            ('api:breeds-detail', (self.breed.id,)),
            # ('api:rating-list', None),
            # ('api:rating-detail', (self.rating.id,)),
        )
        for name, args in urls:
            with self.subTest(name=name):
                response = self.client.get(reverse(name, args=args))
                self.assertEqual(response.status_code, HTTPStatus.UNAUTHORIZED)

    def test_availability_for_edit_and_delete(self):
        users_statuses = (
            (self.owner, HTTPStatus.OK),
            # (self.reader, HTTPStatus.OK),
        )
        urls = (
            ('api:cats-detail', (self.cat.id,)),
            ('api:rating-detail', (self.cat.id, self.rating.id,)),
        )
        for user, status in users_statuses:
            self.client = APIClient()
            self.client.force_authenticate(user=user)
            for name, args in urls:
                with self.subTest(user=user, name=name):
                    response = self.client.get(reverse(name, args=args))
                    self.assertEqual(response.status_code, status)

    def test_create(self):
        urls = (
            (
                'api:cats-list', None,
                {
                    'name': 'TestName',
                    'color': 'TestColor',
                    'age': '10',
                    'description': 'TestDescription',
                    'breed': self.owner.id,
                    'owner': self.reader.id,
                }
            ),
            (
                'api:rating-list', (self.cat.id,),
                {
                    'rate': 5,
                }
            ),
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.reader)
        for name, args, data in urls:
            with self.subTest(user=self.reader, name=name):
                response = self.client.post(
                    reverse(name, args=args), data=data
                )
                self.assertEqual(response.status_code, HTTPStatus.CREATED)
