from apps.users.utils import generate_gravatar_url
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED,
                                   HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED)

from .test_setup import TestSetUp


class TestAuthViews(TestSetUp):
    def test_register_raise_error_when_no_data_body_is_provided(self):
        response = self.client.post(
            self.regiter_url
        )

        assert response.status_code == HTTP_400_BAD_REQUEST
        assert response.data['email'][0] == self.error_required
        assert response.data['password'][0] == self.error_required

    def test_register_raise_error_when_only_invalid_email_is_provided(self):
        response = self.client.post(
            self.regiter_url,
            {
                "email": "testemail.com",
            }
        )

        assert response.status_code == HTTP_400_BAD_REQUEST
        assert response.data['email'][0] == self.error_invalid_email
        assert response.data['password'][0] == self.error_required

    def test_register_raise_error_when_only_email_is_provided(self):
        response = self.client.post(
            self.regiter_url,
            {
                "email": self.user_data["email"],
            }
        )

        assert response.status_code == HTTP_400_BAD_REQUEST
        assert response.data['password'][0] == self.error_required

    def test_register_raise_error_when_only_invalid_password_is_provided(self):
        response = self.client.post(
            self.regiter_url,
            {
                "password": "1234"
            }
        )

        assert response.status_code == HTTP_400_BAD_REQUEST
        assert response.data['email'][0] == self.error_required
        assert response.data['password'][0] == self.error_invalid_password

    def test_register_raise_error_when_valid_email_but_invalid_password_is_provided(self):
        response = self.client.post(
            self.regiter_url,
            {
                "email": self.user_data["email"],
                "password": "1234",
            }
        )

        assert response.status_code == HTTP_400_BAD_REQUEST
        assert response.data['password'][0] == self.error_invalid_password

    def test_register_raise_error_when_invalid_email_but_valid_password_is_provided(self):
        response = self.client.post(
            self.regiter_url,
            {
                "email": "testemail.com",
                "password": self.user_data["password"],
            }
        )

        assert response.status_code == HTTP_400_BAD_REQUEST
        assert response.data['email'][0] == self.error_invalid_email

    def test_register_valid_data(self):
        response = self.client.post(
            self.regiter_url,
            self.user_data,
        )

        assert response.status_code == HTTP_201_CREATED
        assert response.data['id'] == 1
        assert response.data['email'] == self.user_data["email"]
        assert response.data['gravatar_url'] == generate_gravatar_url(self.user_data["email"])

    def test_login_raise_error_when_no_data_body_is_provided(self):
        response = self.client.post(
            self.regiter_url,
            self.user_data,
        )

        assert response.status_code == HTTP_201_CREATED
        assert response.data['id'] == 1
        assert response.data['email'] == self.user_data["email"]
        assert response.data['gravatar_url'] == generate_gravatar_url(self.user_data["email"])

        response = self.client.post(
            self.login_url,
        )

        assert response.status_code == HTTP_400_BAD_REQUEST
        assert response.data['email'][0] == self.error_required
        assert response.data['password'][0] == self.error_required

    def test_login_raise_error_when_only_invalid_email_is_provided(self):
        response = self.client.post(
            self.regiter_url,
            self.user_data,
        )

        assert response.status_code == HTTP_201_CREATED
        assert response.data['id'] == 1
        assert response.data['email'] == self.user_data["email"]
        assert response.data['gravatar_url'] == generate_gravatar_url(self.user_data["email"])

        response = self.client.post(
            self.login_url,
            {
                "email": "testemail.com",
            }
        )

        assert response.status_code == HTTP_400_BAD_REQUEST
        assert response.data['email'][0] == self.error_invalid_email
        assert response.data['password'][0] == self.error_required

    def test_login_raise_error_when_only_valid_email_is_provided(self):
        response = self.client.post(
            self.regiter_url,
            self.user_data,
        )

        assert response.status_code == HTTP_201_CREATED
        assert response.data['id'] == 1
        assert response.data['email'] == self.user_data["email"]
        assert response.data['gravatar_url'] == generate_gravatar_url(self.user_data["email"])

        response = self.client.post(
            self.login_url,
            {
                "email": self.user_data['email'],
            }
        )

        assert response.status_code == HTTP_400_BAD_REQUEST
        assert response.data['password'][0] == self.error_required

    def test_login_raise_error_when_only_valid_password_is_provided(self):
        response = self.client.post(
            self.regiter_url,
            self.user_data,
        )

        assert response.status_code == HTTP_201_CREATED
        assert response.data['id'] == 1
        assert response.data['email'] == self.user_data["email"]
        assert response.data['gravatar_url'] == generate_gravatar_url(self.user_data["email"])

        response = self.client.post(
            self.login_url,
            {
                "password": self.user_data['password'],
            }
        )

        assert response.status_code == HTTP_400_BAD_REQUEST
        assert response.data['email'][0] == self.error_required

    def test_login_raise_error_when_valid_email_but_password_is_short(self):
        response = self.client.post(
            self.regiter_url,
            self.user_data,
        )

        assert response.status_code == HTTP_201_CREATED
        assert response.data['id'] == 1
        assert response.data['email'] == self.user_data["email"]
        assert response.data['gravatar_url'] == generate_gravatar_url(self.user_data["email"])

        response = self.client.post(
            self.login_url,
            {
                "email": self.user_data['email'],
                "password": "!234"
            }
        )

        assert response.status_code == HTTP_400_BAD_REQUEST
        assert response.data['password'][0] == self.error_invalid_password

    def test_login_raise_error_when_valid_email_but_invalid_password_is_provided(self):
        response = self.client.post(
            self.regiter_url,
            self.user_data,
        )

        assert response.status_code == HTTP_201_CREATED
        assert response.data['id'] == 1
        assert response.data['email'] == self.user_data["email"]
        assert response.data['gravatar_url'] == generate_gravatar_url(self.user_data["email"])

        response = self.client.post(
            self.login_url,
            {
                "email": self.user_data['email'],
                "password": "hackme1234"
            }
        )

        assert response.status_code == HTTP_401_UNAUTHORIZED
        assert response.data['detail'] == self.error_invalid_credentials

    def test_login_valid_data(self):
        response = self.client.post(
            self.regiter_url,
            self.user_data,
        )

        assert response.status_code == HTTP_201_CREATED
        assert response.data['id'] == 1
        assert response.data['email'] == self.user_data["email"]
        assert response.data['gravatar_url'] == generate_gravatar_url(self.user_data["email"])

        response = self.client.post(
            self.login_url,
            self.user_data
        )

        assert response.status_code == HTTP_200_OK
        assert response.data['email'] == self.user_data['email']
        assert response.data['gravatar_url'] == generate_gravatar_url(self.user_data['email'])
        assert "refresh" in response.data
        assert "access" in response.data
