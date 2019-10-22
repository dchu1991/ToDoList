from django.shortcuts import render
from django.contrib import messages
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
    )
from .models import ToDoList

# Create your views here.
class ToDoListView(ListView):
    model = ToDoList
    paginate_by = 10
    ordering = ['-post_time']


class ToDoDetailView(DetailView):
    model = ToDoList

class ToDoCreateView(CreateView):
    model = ToDoList
    fields = ['title', 'content']

    def form_valid(self, form):
        return super().form_valid(form)

class ToDoUpdateView(UpdateView):
    model = ToDoList
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(request, f'Deletion of {title} is successful.')
        return super().form_valid(form)

class ToDoDeleteView(DeleteView):
    model = ToDoList
    success_url = '/'


