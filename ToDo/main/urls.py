from django.urls import path
from .views import (
    ToDoListView,
    ToDoDetailView,
    ToDoUpdateView,
    ToDoCreateView
)

urlpatterns = [
    path('', ToDoListView.as_view(), name='todo_listview'),
    path('<slug:slug>/', ToDoCreateView.as_view(), name='todo_detail'),
    path('create/', ToDoCreateView.as_view(), name='todo_create'),
]