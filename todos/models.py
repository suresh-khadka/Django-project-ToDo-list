from django.db import models

class Task(models.Model):
    task = models.TextField(max_length=100)
    Is_completed=models.BooleanField(default=False)
    Created_at=models.DateTimeField(auto_now_add=True)
    Updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task
