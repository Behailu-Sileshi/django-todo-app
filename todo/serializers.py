from django.utils.timezone import now
from rest_framework import serializers
from djoser.serializers import (
    UserSerializer as BaseUserSerializer,
    UserCreateSerializer as BaseUserCreateSerializer,
)
from .models import Category, Task


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ["id", "username", "password", "email", "first_name", "last_name"]


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ["id", "username", "email", "first_name", "last_name"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "title", "description"]
    
    


class TaskSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "created_at",
            "deadline",
            "status",
            "priority",
            "category",
        ]


class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "created_at",
            "deadline",
            "status",
            "priority",
            "category",
        ]

    def validate_deadline(self, value):
        if value < now():
            raise serializers.ValidationError("Deadline cannot be in the past and now.")
        return value

    def create(self, validated_data):
        user_id = self.context["user_id"]
        return Task.objects.create(user_id=user_id, **validated_data)


class UpdateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["status", "task_priority"]

    def validate_status(self, value):
        if value not in ["C", "P", "F"]:
            raise serializers.ValidationError("The status must be in [C, P, F].")
        return value
    
    def validate_priority(self, value):
        if value not in ["L", "M", "H"]:
            raise serializers.ValidationError("The priority must be in [L, M, H].")
        return value
    
