from django.contrib import admin

from .models import Questions, Answers, Game, Scores

admin.site.register(Questions)
admin.site.register(Answers)
admin.site.register(Game)
admin.site.register(Scores)
