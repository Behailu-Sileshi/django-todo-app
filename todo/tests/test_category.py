import pytest
from rest_framework import status
from todo.models import Category
from model_bakery import baker


@pytest.fixture
def create_category(api_client):
    def do_create_category(data):
        return api_client.post("/todo/categories/", data)

    return do_create_category


@pytest.fixture
def retrieve_category(api_client):
    def do_retrieve_category(category_id):
        return api_client.get(f"/todo/categories/{category_id}/")

    return do_retrieve_category


@pytest.fixture
def update_category(api_client):
    def do_update_category(category_id, data):
        return api_client.patch(f"/todo/categories/{category_id}/", data)

    return do_update_category


@pytest.fixture
def delete_category(api_client):
    def do_delete_category(category_id):
        return api_client.delete(f"/todo/categories/{category_id}/")

    return do_delete_category


@pytest.mark.django_db
class TestCreateCategory:
    def test_if_user_is_anonymous_returns_401(self, create_category):
        response = create_category({"title": "a"})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def if_user_is_not_admin_return_403(self, authenticate,  delete_category):
        authenticate()

        response = delete_category(5)

        assert response.status_code == status.HTTP_403_FORBIDDEN
        
    def test_if_data_is_invalid_returns_400(self, authenticate, create_category):
        authenticate(is_staff=True)

        response = create_category({"title": ""})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data is not None

    def test_if_data_is_valid_returns_201(self, authenticate, create_category):
        authenticate(is_staff=True)

        response = create_category(
            {
                "title": "a",
                "description": "a",
            }
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["title"] == "a"


@pytest.mark.django_db
class TestRetrieveCategory:
    def test_if_user_is_anonymous_returns_401(self, retrieve_category):
        response = retrieve_category(5)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_category_does_not_exists_return_404(
        self, retrieve_category, authenticate
    ):
        authenticate()

        response = retrieve_category(5)

        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_if_category_exists_return_200(self, retrieve_category, authenticate):
        user = authenticate()

        category = baker.make(Category)

        response = retrieve_category(category.id)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["id"] == category.id


@pytest.mark.django_db
class TestUpdateCategory:
    def test_if_user_is_anonymous_returns_401(self, update_category):
        response = update_category(5, {"title": "a"})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        
    def if_user_is_not_admin_return_403(self, authenticate,  delete_category):
        authenticate()

        response = delete_category(5)

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_category_does_not_exists_return_404(
        self, update_category, authenticate
 ):
        authenticate(is_staff=True)

        response = update_category(5, {"title": "a"})

        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_if_data_is_invalid_returns_400(self, authenticate, update_category):
        user = authenticate(is_staff=True)

        category = baker.make(Category)
        response = update_category(category.id, {"title": ""})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data is not None

    def test_if_data_is_valid_returns_200(self, authenticate, update_category):
        user = authenticate(is_staff=True)

        category = baker.make(Category)
        response = update_category(category.id, {"title": "X"})

        assert response.status_code == status.HTTP_200_OK
        assert response.data["title"] == "X"


@pytest.mark.django_db
class TestDeleteCategory:
    def test_if_user_is_anonymous_returns_401(self, delete_category):
        response = delete_category(5)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def if_user_is_not_admin_return_403(self, authenticate,  delete_category):
        authenticate()

        response = delete_category(5)

        assert response.status_code == status.HTTP_403_FORBIDDEN
        
    def test_if_category_does_not_exists_return_404(
        self, delete_category, authenticate
    ):
        authenticate(is_staff=True)

        response = delete_category(5)

        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_if_category_exists_returns_204(self, authenticate, delete_category):
        user = authenticate(is_staff=True)

        category = baker.make(Category)
        response = delete_category(category.id)

        assert response.status_code == status.HTTP_204_NO_CONTENT
