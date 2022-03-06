from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker


class TestSetUp(APITestCase):
    def setUp(self) -> None:
        self.regiter_url = reverse('register')
        self.login_url = reverse('login')
        self.sections_url = reverse('sections')

        self.faker = Faker()
        self.user_data = {
            "email": self.faker.safe_email(),
            "password": "supersecret",
        }

        self.client.post(
            self.regiter_url,
            self.user_data
        )
        resp = self.client.post(
            self.login_url,
            self.user_data,
        )

        self.access_token = resp.data['access']

        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()
