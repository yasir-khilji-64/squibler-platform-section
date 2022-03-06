from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker


class TestSetUp(APITestCase):
    def setUp(self) -> None:
        self.regiter_url = reverse('register')
        self.login_url = reverse('login')
        self.error_required = 'This field is required.'
        self.error_invalid_email = 'Enter a valid email address.'
        self.error_invalid_password = 'Ensure this field has at least 8 characters.'
        self.error_invalid_credentials = 'Invalid credentials.'
        self.faker = Faker()
        self.user_data = {
            "email": self.faker.safe_email(),
            "password": "supersecret",
        }

        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()
