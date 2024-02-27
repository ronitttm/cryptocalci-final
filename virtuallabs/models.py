from django.db import models
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.utils import timezone

class UserImage(models.Model):
    session_key = models.CharField(max_length=40, default='')  # Set a default value
    image = models.ImageField(upload_to='user_images/')
    created_at = models.DateTimeField(auto_now_add=True)

class Code(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Code by {self.user.username}"