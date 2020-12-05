from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Questions(models.Model):
    """
    This model for question,point of question and which question was used during the game
    """
    title = models.CharField(max_length=255)
    point = models.SmallIntegerField(default=5, validators=[MinValueValidator(5), MaxValueValidator(20)])
    used_questions = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title


class Answers(models.Model):
    """
    Here we can save all answers, also correct answers and it's connecting with question via ForeignKey
    """
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    true_answer = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.answer


class Scores(models.Model):
    """
    Here we save scores all users, it also connects via ForeignKey
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    class Meta:
        ordering = ['-score']

    def __str__(self):
        return f'Score of {self.user.username} is {self.score}'


class Game(models.Model):
    """
    This class count number of question and after he set default value a couple of row in different table
    """
    count = models.SmallIntegerField(default=0)

    def __str__(self):
        return f'{self.count} cycles of your game'
