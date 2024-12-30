from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from todo.models import Task
from todo.serializers import CategorySerializer, TaskSerializer

# Create your views here.
class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
class CategoryViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = CategorySerializer
    