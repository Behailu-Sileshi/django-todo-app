from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import  IsAuthenticated
from .models import Category, Task
from .serializers import CategorySerializer, CreateTaskSerializer, TaskSerializer, UpdateTaskSerializer


class TaskViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Task.objects.filter(user_id=self.request.user.id).all()
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateTaskSerializer
        elif self.request.method == "PATCH":
            return UpdateTaskSerializer
        return TaskSerializer
    
    def get_serializer_context(self):
        return {'user_id': self.request.user.id}
    
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    