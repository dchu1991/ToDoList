from django.urls import path
from .views import (
    ToDoListView,
    ToDoDetailView,
    ToDoUpdateView,
    ToDoCreateView,
    ToDoDeleteView
)

urlpatterns = [
    path('', ToDoListView.as_view(), name='todo_listview'),
    path('<int:pk>/', ToDoDetailView.as_view(), name='todo_detail'),
    path('create/', ToDoCreateView.as_view(), name='todo_create'),
    path('update/<int:pk>/', ToDoUpdateView.as_view(), name='todo_update'),
    path('delete/<int:pk>/', ToDoDeleteView.as_view(), name='todo_delete')
]