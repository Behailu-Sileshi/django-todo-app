from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('tasks', views.TaskViewSet, basename='task')
router.register('categories', views.CategoryViewSet, basename='category')

urlpatterns = router.urls