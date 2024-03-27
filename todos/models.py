from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    deadline = models.DateTimeField(null=True, blank=True)
    ordering = ('title','body','completed','created_at', 'updated_at','completed','important','deadline')
    
    def __str__(self):
        return self.title