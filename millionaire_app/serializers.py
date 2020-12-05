from rest_framework import serializers

from .models import Questions, Answers, Scores


class QuestionsSerializer(serializers.ModelSerializer):
    """
    Serializers class for Questions
    """
    class Meta:
        model = Questions
        fields = '__all__'


class AnswersSerializer(serializers.ModelSerializer):
    """
    Serializers class for Answers
    """
    title = serializers.ReadOnlyField(source='question.title', read_only=True)

    class Meta:
        model = Answers
        fields = '__all__'


class ScoresSerializer(serializers.ModelSerializer):
    """
    Serializers class for Scores of Users
    """
    class Meta:
        model = Scores
        fields = '__all__'