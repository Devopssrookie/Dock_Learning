from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        #return self.body[0:50]
        return f"Title: {self.title}, Body: {self.body[0:50]}"