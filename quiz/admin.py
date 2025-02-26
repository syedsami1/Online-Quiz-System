from django.contrib import admin
from .models import Question, Option, Quiz, Participant, Response

admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Quiz)
admin.site.register(Participant)
admin.site.register(Response)
