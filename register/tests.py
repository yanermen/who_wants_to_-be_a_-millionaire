from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class RegistrationTestCase(APITestCase):

    def test_registration(self) -> None:
        data = {"first_name": "testcase",
                "last_name": "testcase",
                "username": "testcase",
                "password": "testcase",
                "email": "testcase"}

        response = self.client.post("/api/v1/signup/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LoginTestCase(APITestCase):

    def test_login(self) -> None:
        client = APIClient()
        client.login(username='testcase', password='testcase')



