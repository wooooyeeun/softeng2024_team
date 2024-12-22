from django.db import models

class ToDoList(models.Model):
    title = models.CharField(max_length=200, unique=True)
    color = models.CharField(max_length=7, default="#000000")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ToDoItem(models.Model):
    list = models.ForeignKey(ToDoList, on_delete=models.CASCADE, related_name='items')
    subtitle = models.CharField(max_length=200)
    color = models.CharField(max_length=7, default="#000000")
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return self.subtitle



