from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Question(models.Model):
    text = models.TextField()

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    questions = models.ManyToManyField(Question)
    total_score = models.IntegerField()
    duration = models.IntegerField()  # Duration in minutes

class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=50)

class Response(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(Option, on_delete=models.CASCADE)
    correct = models.BooleanField()
