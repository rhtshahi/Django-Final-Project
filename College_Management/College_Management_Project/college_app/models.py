from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notice(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.TextField()
    posted_date = models.DateField(auto_now=True)
    posted_by = models.ForeignKey(User, related_name='posted_by', on_delete=models.CASCADE, default=None)
    priority = models.CharField(max_length=50, choices=[('Urgent', 'Urgent'), ('Important', 'Important'), ('Basic', 'Basic')], null=True)

    def __str__(self):
        return self.title
