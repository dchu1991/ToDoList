from django.urls import path, include
from .views import (
    ToDoListView,
    ToDoDetailView,
    ToDoUpdateView,
    ToDoCreateView,
    ToDoDeleteView,
    ToDoAPIView
)

from rest_framework import routers

router = routers.DefaultRouter()
router.register('posts', ToDoAPIView)

urlpatterns = [
    path('', ToDoListView.as_view(), name='todo_listview'),
    path('<int:pk>/', ToDoDetailView.as_view(), name='todo_detail'),
    path('create/', ToDoCreateView.as_view(), name='todo_create'),
    path('update/<int:pk>/', ToDoUpdateView.as_view(), name='todo_update'),
    path('delete/<int:pk>/', ToDoDeleteView.as_view(), name='todo_delete'),
    path('api/', include(router.urls), name='todo_api')
]