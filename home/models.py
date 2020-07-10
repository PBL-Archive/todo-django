from django.db import models

# Create your models here.

class Todo(models.Model):
    todo_id = models.AutoField(primary_key=True)
    todo = models.TextField(max_length=100)
    checked = models.CharField(max_length=20, default="not_checked")
    todotext = models.CharField(max_length=20, default="cannot_edit")
    edit = models.CharField(max_length=20, default="edit")
    remove = models.CharField(max_length=20, default="remove")
    add = models.CharField(max_length=20, default="add")

    def __str__(self):
        return self.todo