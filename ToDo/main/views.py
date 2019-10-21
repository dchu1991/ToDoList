from django.shortcuts import render
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


class ToDoDetailView(ListView):
    model = ToDoList

class ToDoUpdateView(UpdateView):
    model = ToDoList

class ToDoCreateView(CreateView):
    model = ToDoList
