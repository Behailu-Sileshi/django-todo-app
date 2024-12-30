# Generated by Django 5.1.4 on 2024-12-30 10:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='category',
        ),
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='todo.category'),
            preserve_default=False,
        ),
    ]