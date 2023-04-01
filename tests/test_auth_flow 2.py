# tests/test_auth_flow.py
import pytest
from flask import session
#from translation.authentication.auth import AuthManager
from translation.adapters.memory_repository import MemoryRepository
from translation import create_app
from translation.views.authentication_views import auth_manager


@pytest.fixture
def client(app):
    client = app.test_client()
    app_context = app.app_context()
    app_context.push()
    yield client
    app_context.pop()


@pytest.fixture
def memory_repo():
    return MemoryRepository()


@pytest.fixture
def auth():
    return auth_manager

        

def test_auth_flow(client):
    # Register a user
    register_response = client.post('/register', data={'user_name': 'test_user', 'password': 'test_password'})

    # Check if the response status code is 302 (redirect) and that the user is redirected to the login page
    assert register_response.status_code == 302
    assert register_response.headers['Location'].endswith('/login')
    
    # Check if the user is in the memory_repo
    memory_repo = auth_manager.get_repository()
    user = memory_repo.get_user('test_user')
    assert user is not None

    # Log in
    login_response = client.post('/login', data={'user_name': 'test_user', 'password': 'test_password'})

    # Check if the response status code is 302 (redirect) and that the user is redirected to the profile page
    assert login_response.status_code == 302
    assert login_response.headers['Location'].endswith('/profile')

    # Check if the user has a session
    with client.session_transaction() as session:
        assert session.get('user_id') == user.id
