from django.urls import path
from .views import QuizList, TopTenProfiles

urlpatterns = [
    path('quiz/', QuizList.as_view(), name='quiz'),
    path('profiles/top10/', TopTenProfiles.as_view(), name='top10_profiles'),
]