from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import SAFE_METHODS

from .models import Category, Task
from .serializers import (
    CategorySerializer,
    CreateTaskSerializer,
    TaskSerializer,
    UpdateTaskSerializer,
)


class TaskViewSet(ModelViewSet):
    http_method_names = ["get", "post", "patch", "delete"]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'priority', 'status']
    search_fields = ['title']
    ordering_fields = ['created_at', 'deadline']

    def get_queryset(self):
        return Task.objects.filter(user_id=self.request.user.id).all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateTaskSerializer
        elif self.request.method == "PATCH":
            return UpdateTaskSerializer
        return TaskSerializer

    def get_serializer_context(self):
        return {"user_id": self.request.user.id}


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticated()]
        return [IsAdminUser()]
    
    
