from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import User


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer class for Profile
    """
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']

    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.
        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)

