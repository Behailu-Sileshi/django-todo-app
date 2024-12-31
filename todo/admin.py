from django.contrib import admin
from django.db.models import Count
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Category, Task, User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "usable_password",
                    "password1",
                    "password2",
                    "email",
                    "first_name",
                    "last_name",
                ),
            },
        ),
    )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "status", "user", "category"]
    list_per_page = 10

    def category(self, category: Category):
        return category.title


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "tasks_count"]
    list_per_page = 10

    def tasks_count(self, category):
        return category.tasks.count()

    tasks_count.description = "tasks"
