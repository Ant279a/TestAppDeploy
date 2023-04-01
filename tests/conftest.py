# tests/conftest.py
import pytest
from translation.adapters.memory_repository import MemoryRepository
from translation.authentication.auth import AuthManager

@pytest.fixture
def memory_repo():
    return MemoryRepository()

@pytest.fixture
def auth_manager():
    return AuthManager()
