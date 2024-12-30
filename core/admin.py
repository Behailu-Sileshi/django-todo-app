from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.contenttypes.admin import GenericTabularInline
from tags.models import TaggedItem
from todo.admin import TaskAdmin
from todo.models import Task
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name'),
        }),
    )

class TagInline(GenericTabularInline):
    autocomplete_fields = ['tag']
    model = TaggedItem


class CustomTaskAdmin(TaskAdmin):
    inlines = [TagInline]


admin.site.unregister(Task)
admin.site.register(Task, TaskAdmin)    