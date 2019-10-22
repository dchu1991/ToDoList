from rest_framework import serializers
from .models import ToDoList

class ToDoSerializer(serializers.ModelSerializer):
    """translate the model infomation into json"""
    
    class Meta:
        """specifying the attributes"""
        model = ToDoList
        fields = ('id', 'title', 'content', 'post_time') # id is automatically generated
