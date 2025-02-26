from django.test import TestCase
from .models import Question, Option, Quiz, Participant, Response

class QuizTestCase(TestCase):
    def setUp(self):
        self.question = Question.objects.create(text='What is the capital of France?')
        self.option1 = Option.objects.create(question=self.question, text='Paris', is_correct=True)
        self.option2 = Option.objects.create(question=self.question, text='London', is_correct=False)
        self.quiz = Quiz.objects.create(title='Geography Quiz', total_score=20, duration=10)
        self.quiz.questions.add(self.question)
        self.participant = Participant.objects.create(user=None, quiz=self.quiz, score=None, status='in-progress')
        self.response = Response.objects.create(participant=self.participant, question=self.question, selected_option=self.option1, correct=True)

    def test_question_creation(self):
        self.assertEqual(self.question.text, 'What is the capital of France?')

    def test_option_creation(self):
        self.assertTrue(self.option1.is_correct)
        self.assertFalse(self.option2.is_correct)

    def test_quiz_creation(self):
        self.assertEqual(self.quiz.title, 'Geography Quiz')
        self.assertEqual(self.quiz.total_score, 20)
        self.assertEqual(self.quiz.duration, 10)
        self.assertEqual(self.quiz.questions.count(), 1)

    def test_participant_creation(self):
        self.assertEqual(self.participant.quiz, self.quiz)
        self.assertEqual(self.participant.status, 'in-progress')

    def test_response_creation(self):
        self.assertEqual(self.response.selected_option, self.option1)
        self.assertTrue(self.response.correct)
