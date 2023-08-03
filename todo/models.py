from django.db import models

class Todo(models.Model):
    todo = models.CharField(max_length=60)

    def  __str__(self):
        return self.todo