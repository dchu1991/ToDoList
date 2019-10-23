from django.db import models

# for redirecting after blog post
from django.urls import reverse

# Create your models here.
class ToDoList(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    post_time = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    # to the detailed page
    def get_absolute_url(self):
        return reverse('todo_detail', kwargs={'pk':self.pk} )