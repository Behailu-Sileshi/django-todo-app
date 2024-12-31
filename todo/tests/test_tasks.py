import pytest
from rest_framework import status
from todo.models import Category, Task
from model_bakery import baker

@pytest.fixture
def create_task(api_client):
    def do_create_task(data):
        return api_client.post('/todo/tasks/', data)
    return do_create_task

@pytest.fixture
def retrieve_task(api_client):
    def do_retrieve_task(task_id):
        return api_client.get(f'/todo/tasks/{task_id}/')
    return do_retrieve_task

@pytest.fixture
def update_task(api_client):
    def do_update_task(task_id, data):
        return api_client.patch(f'/todo/tasks/{task_id}/', data)
    return do_update_task

@pytest.fixture
def delete_task(api_client):
    def do_delete_task(task_id):
        return api_client.delete(f'/todo/tasks/{task_id}/')
    return do_delete_task

@pytest.mark.django_db
class TestCreateTask:
    def test_if_user_is_anonymous_returns_401(self, create_task):
        response = create_task({'title': 'a'})
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_data_is_invalid_returns_400(self, authenticate, create_task):
        authenticate()
        
        response = create_task({'title': ''})
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data is not None

    def test_if_data_is_valid_returns_201(self, authenticate, create_task):
        authenticate()
        
        category = baker.make(Category)
        response = create_task({
            'title': 'a',
            'description': 'a',
            'deadline': '2025-01-01T23:59:59Z',
            'category': category.id,
        })
        
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['title'] == 'a'
       

    def test_if_category_is_invalid_returns_400(self, authenticate, create_task):
        authenticate()
        
        response = create_task({
            'title': 'a',
            'description': 'a',
            'deadline': '2024-12-31T23:59:59Z',
            'category': 999  # Non-existent category ID.
        })
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.django_db
class TestRetrieveTask:
    def test_if_user_is_anonymous_returns_401(self, retrieve_task):
        response = retrieve_task(task_id=5)
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_if_task_does_not_exists_return_404(self, retrieve_task, authenticate):
        authenticate()
        
        response = retrieve_task(task_id=5)
       
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_if_task_exists_return_200(self, retrieve_task, authenticate):
        user = authenticate()
        
        category = baker.make(Category)
        task = baker.make(Task, category=category, user=user)
        
        response = retrieve_task(task_id=task.id)
        
        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == task.id
        
@pytest.mark.django_db
class TestUpdateTask:
    def test_if_user_is_anonymous_returns_401(self, update_task):
        response = update_task(5, {'status': 'a'})
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_if_task_does_not_exists_return_404(self, update_task, authenticate):
        authenticate()
        
        response = update_task(5, {'status': 'a'})
        
        assert response.status_code == status.HTTP_404_NOT_FOUND
    
    def test_if_data_is_invalid_returns_400(self, authenticate, update_task):
        user = authenticate()
        
        category = baker.make(Category)
        task = baker.make(Task, category=category, user=user)
        
        
        response = update_task(task.id,  {'status': 'x'})
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data is not None
    
    def test_if_data_is_valid_returns_200(self, authenticate, update_task):
        user = authenticate()
        
        category = baker.make(Category)
        task = baker.make(Task, category=category, user=user)
        response = update_task(task.id,  {'status': 'C'})
        
        assert response.status_code == status.HTTP_200_OK
        assert response.data['status'] ==  'C'
        
@pytest.mark.django_db
class TestDeleteTask:
    def test_if_user_is_anonymous_returns_401(self, delete_task):
        response = delete_task(5)
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_if_task_does_not_exists_return_404(self, delete_task, authenticate):
        authenticate()
        
        response = delete_task(5)
        
        assert response.status_code == status.HTTP_404_NOT_FOUND
    
    def test_if_task_exists_returns_204(self, authenticate, delete_task):
        user = authenticate()
        
        category = baker.make(Category)
        task = baker.make(Task, category=category, user=user)
        response = delete_task(task.id)
        
        assert response.status_code == status.HTTP_204_NO_CONTENT
        
        
    
    
    
    
        