from django.db import models

# Create your models here.

class Todo(models.Model):
    todo_id = models.AutoField(primary_key=True)
    todo = models.TextField(max_length=100)
    
    def __str__(self):
        return self.todo