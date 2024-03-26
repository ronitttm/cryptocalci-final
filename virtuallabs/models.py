from django.db import models
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.utils import timezone

# class UserImage(models.Model):
#     session_key = models.CharField(max_length=40, default='')  # Set a default value
#     image = models.ImageField(upload_to='user_images/')
#     created_at = models.DateTimeField(auto_now_add=True)
class UploadedImage(models.Model):
    url = models.URLField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Code(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Code by {self.user.username}"
    
from django.db import models

# Create your models here.
class QuesModel(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
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
