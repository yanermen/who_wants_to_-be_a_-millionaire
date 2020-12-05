from rest_framework import status
from rest_framework.test import APITestCase


class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {"first_name": "testcase",
                "last_name": "testcase",
                "username": "testcase",
                "password": "testcase",
                "email": "testcase"}

        response = self.client.post("/api/v1/signup/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

