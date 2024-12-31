from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
import pytest



@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def authenticate(api_client):
    def do_authenticate(is_staff=False):
        user_model = get_user_model()
        user = user_model.objects.create_user(username='test', email='test@example.com', password='password123', is_staff=is_staff)
        api_client.force_authenticate(user=user)
        return user
    return do_authenticate
