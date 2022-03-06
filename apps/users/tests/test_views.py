from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED

from apps.users.utils import generate_gravatar_url

from .test_setup import TestSetUp


class TestAuthViews(TestSetUp):
    def test_register_raise_error_when_no_data_body_is_provided(self):
        response = self.client.post(
            self.regiter_url
        )

        assert response.status_code == 400
        assert response.data['email'][0] == self.error_required
        assert response.data['password'][0] == self.error_required

    def test_register_raise_error_when_only_invalid_email_is_provided(self):
        response = self.client.post(
            self.regiter_url,
            {
                "email": "testemail.com",
            }
        )

        assert response.status_code == 400
        assert response.data['email'][0] == self.error_invalid_email
        assert response.data['password'][0] == self.error_required

    def test_register_raise_error_when_only_email_is_provided(self):
        response = self.client.post(
            self.regiter_url,
            {
                "email": self.user_data["email"],
            }
        )

        assert response.status_code == 400
        assert response.data['password'][0] == self.error_required

    def test_register_raise_error_when_only_invalid_password_is_provided(self):
        response = self.client.post(
            self.regiter_url,
            {
                "password": "1234"
            }
        )

        assert response.status_code == 400
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

        assert response.status_code == 400
        assert response.data['password'][0] == self.error_invalid_password

    def test_register_raise_error_when_invalid_email_but_valid_password_is_provided(self):
        response = self.client.post(
            self.regiter_url,
            {
                "email": "testemail.com",
                "password": self.user_data["password"],
            }
        )

        assert response.status_code == 400
        assert response.data['email'][0] == self.error_invalid_email

    def test_register_valid_data(self):
        response = self.client.post(
            self.regiter_url,
            {
                "email": self.user_data["email"],
                "password": self.user_data["password"]
            }
        )

        assert response.status_code == HTTP_201_CREATED
        assert response.data['id'] == 1
        assert response.data['email'] == self.user_data["email"]
        assert response.data['gravatar_url'] == generate_gravatar_url(self.user_data["email"])
