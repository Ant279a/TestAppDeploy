# tests/test_auth.py
import pytest

def test_auth_manager_register_user(auth_manager):
    new_user = auth_manager.register_user('test_user', 'test_password')
    assert new_user is not None
    assert new_user.username == 'test_user'
    assert new_user.password == 'test_password'

def test_auth_manager_register_existing_user(auth_manager):
    auth_manager.register_user('test_user', 'test_password')
    with pytest.raises(ValueError, match="User already exists"):
        auth_manager.register_user('test_user', 'test_password')

def test_auth_manager_authenticate_user(auth_manager):
    auth_manager.register_user('test_user', 'test_password')
    assert auth_manager.authenticate_user('test_user', 'test_password') == True
    assert auth_manager.authenticate_user('test_user', 'wrong_password') == False
    assert auth_manager.authenticate_user('nonexistent_user', 'test_password') == False
