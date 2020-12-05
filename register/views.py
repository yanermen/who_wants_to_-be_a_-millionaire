from appdirs import unicode
from .models import User
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ProfileSerializer


class ProfileCreateAPIView(CreateAPIView):
    """
    The class create a new user
    """
    serializer_class = ProfileSerializer


class ProfilesListAPIView(ListAPIView):
    """
    This class show us list of regitered user, but it can shows only if you have administrator permissions
    """
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAdminUser, ]


class ProfileRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    The class vor RUD operation and it can do administrator or user
    """
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAdminUser | permissions.IsAuthenticated]


class ProfileLogin(APIView):
    """
    The class provides signin authentication for user
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': unicode(request.user),
            'auth': unicode(request.auth),
        }
        return Response(content)