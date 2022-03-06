from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED,
                                   HTTP_401_UNAUTHORIZED)

from .test_setup import TestSetUp


class TestSectionViews(TestSetUp):
    def test_sections_raise_error_when_no_auth_header_is_set(self):
        response = self.client.get(
            self.sections_url,
        )

        assert response.status_code == HTTP_401_UNAUTHORIZED

    def test_sections_check_for_number_of_sections(self):
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.access_token
        )

        response = self.client.get(
            self.sections_url,
        )

        assert response.status_code == HTTP_200_OK
        assert len(response.data) == 0
