from django.db import models
from django.utils import timezone

# Create your models here.

class  Todo(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    date = models.TextField()

    def __str__(self):
        return self.title

class Todos(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title