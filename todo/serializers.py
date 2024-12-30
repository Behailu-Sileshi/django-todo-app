from datetime import timezone
from rest_framework import serializers
from .models import Category, Task


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'description']
        
class TaskSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'created_at', 'deadline', 'status', 'category']

class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'created_at', 'deadline', 'status', 'category']
    
    def validate_deadline(self, value):
        if value <= timezone.now():
            raise serializers.ValidationError("Deadline cannot be in the past and now.")
        return value

    
    def create(self, validated_data):
        user_id = self.context['user_id']
        return Task.objects.create(user_id=user_id, **validated_data)

class UpdateTaskSerializer(serializers.ModelSerializer):
     class Meta:
        model = Task
        fields = ['status']
    