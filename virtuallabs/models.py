from django.db import models
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# class UserImage(models.Model):
#     session_key = models.CharField(max_length=40, default='')  # Set a default value
#     image = models.ImageField(upload_to='user_images/')
#     created_at = models.DateTimeField(auto_now_add=True)

class Experiments(models.Model):
    title = models.CharField(max_length=150)
    aim = models.CharField(max_length=200)
    theory = models.TextField()
    conclusion = models.CharField(max_length=225)



class UploadedImage(models.Model):
    url = models.URLField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Code(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Code by {self.user.username}"

class ExperimentSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    experiment = models.ForeignKey(Experiments, on_delete=models.CASCADE, null=True)
    experiment_name = models.CharField(max_length=100)
    code = models.TextField()
    image = models.URLField()
    timestamp = models.DateTimeField(default=timezone.now)
    submission_count = models.IntegerField(default=0)

    def __str__(self):
        return f"Experiment Submission by {self.user.username} - {self.title}"
    

class QuesModel(models.Model):
    experiment = models.ForeignKey(Experiments, on_delete=models.CASCADE, null=True)
    question = models.CharField(max_length=200, null=True)
    Option_1 = models.CharField(max_length=200, null=True)
    Option_2 = models.CharField(max_length=200, null=True)
    Option_3 = models.CharField(max_length=200, null=True)
    Option_4 = models.CharField(max_length=200, null=True)
    Answer = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.question

    
class QuizScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    time_taken = models.IntegerField()  # Time taken to complete the quiz in seconds
    correct_answers = models.IntegerField()
    wrong_answers = models.IntegerField()
    percent_correct = models.FloatField()  # Percentage of correct answers
    total_questions = models.IntegerField()
    timestamp = models.DateTimeField(default=timezone.now)
