from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet, OptionViewSet, QuizViewSet, ParticipantViewSet, ResponseViewSet

router = DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'options', OptionViewSet)
router.register(r'quizzes', QuizViewSet)
router.register(r'participants', ParticipantViewSet)
router.register(r'responses', ResponseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
