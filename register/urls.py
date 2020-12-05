from django.urls import path
from .views import ProfileCreateAPIView, ProfileRetrieveUpdateDestroyAPIView, ProfilesListAPIView, ProfileLogin


urlpatterns = [
    path('signup/', ProfileCreateAPIView.as_view(), name='signup'),
    path('signin/', ProfileLogin.as_view(), name='signin'),
    path('signin/<int:pk>/', ProfileRetrieveUpdateDestroyAPIView.as_view(), name='signin'),
    path('profiles/', ProfilesListAPIView.as_view(), name='profiles'),
]