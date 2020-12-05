from django.db.models import F

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import renderers
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Questions, Answers, Game, Scores
from .serializers import QuestionsSerializer


class QuizList(APIView):
    """
    This class check user is authenticated or no, if yes you can play the game
    Also this class show question, answer, and sum all your points and in the end it shows you.
    When you answer not correct, it notices you and show the correct answer
    """
    authentication_classes = [BasicAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    serializer_class = QuestionsSerializer
    renderer_classes = [renderers.JSONRenderer, ]

    def get(self, request, format=None):
        scores = Scores.objects.get(user=request.user)
        score_point = scores.score
        random_question = str(Questions.objects.filter(used_questions=False).order_by('?')[1])
        Questions.objects.filter(title=random_question).update(used_questions=True)
        answers = list(Answers.objects.filter(question__title=random_question))
        ans = []
        for answer in answers:
            ans.append(answer)
        content = {"random_question": random_question,
                   "A": str(ans[0]),
                   "B": str(ans[1])
                   }
        if Game.objects.filter(count=5):
            score_user = list(Scores.objects.filter(user=request.user))
            Game.objects.all().update(count=0)
            Questions.objects.all().update(used_questions=False)
            return Response(f"You game is over. Your score is {score_point}. Thank You.")
        else:
            Game.objects.all().update(count=F('count') + 1)
        return Response(content)

    def post(self, request):
        data = request.data
        question = data.get("question")
        answer = data.get("answer")
        question_obj = Questions.objects.get(title=question)
        answer_objs = Answers.objects.filter(question=question_obj)
        for answer_obj in answer_objs:
            if answer_obj.answer == answer and answer_obj.true_answer:
                # scores = Scores.objects.filter(user=request.user).get(has_finished=False)
                scores = Scores.objects.get(user=request.user)
                scores.score += question_obj.point
                scores.save()
                return Response("Congratulation! Your answer is correct")
            else:
                return Response(f"I'm sorry. Your answer is wrong. Correct answer is {answer_obj.answer}")


class TopTenProfiles(APIView):
    """
    This class show top 10 users which has the max.scores
    """
    def get(self, request):
        top10 = Scores.objects.all()[:10].values_list("user__username", "score")
        return Response({"top10": list(top10)})


